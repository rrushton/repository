/* main.c - security audit
 * 
 * Note this is Work In Progress!
 * Uses the National Vulnerability Database to discover CVEs
 * and the affected software. Currently this script is limited
 * to direct matches for package names, and could do with
 * some fuzzy checking or mapping.
 *
 * Copyright 2013 Ikey Doherty <ikey@solusos.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <libxml/xmlreader.h>
#include <stdbool.h>
#include <string.h>
#include <stdint.h>
#include <glib.h>
#include <gio/gio.h>

#include "main.h"

#define PATCH_PREFIX "files/security/"

struct vulnerability_t {
        gchar *product;
        gchar *vendor;
        gchar *version;
};

struct cve_entry_t {
        gchar *id;
        gchar *summary;
        GList *uris;
};

struct source_package_t {
        xmlChar *name;
        xmlChar *version;
        gchar *path;
        int release;
        GList *issues;
        GList *patched;
};

static bool in_list = false;
static bool in_entry = false;
static bool in_product = false;
static bool in_summary = false;

static GHashTable *db = NULL;
static GHashTable *cdb = NULL;

static inline void package_free(void *p)
{
        if (!p) {
                return;
        }
        struct source_package_t *t = p;
        if (t->issues) { /* bless you */
                g_list_free_full(t->issues, xmlFree);
        }
        if (t->patched) {
                g_list_free_full(t->patched, xmlFree);
        }
        g_free(t->path);
        xmlFree(t->name);
        xmlFree(t->version);
        free(t);
}

static bool parse_vuln(const xmlChar* inp, struct vulnerability_t *vuln)
{
        gchar *product = NULL;
        gchar *vendor = NULL;
        gchar *version = NULL;
        int len = 0;
        /* Example: cpe:/a:oracle:siebel_crm:8.1.1 */
        gchar **splits = g_strsplit((const gchar*)inp, ":", 10);
        if ((len = g_strv_length(splits)) < 4) {
                g_strfreev(splits);
                return false;
        }

        vendor = g_strdup(splits[2]);
        product = g_strdup(splits[3]);
        if (len > 4) {
                version = g_strdup(splits[4]);
        }
        g_strfreev(splits);

        vuln->vendor = vendor;
        vuln->product = product;
        vuln->version = version;

        return true;
}

static xmlChar *cur_id = NULL;
static xmlChar *summary = NULL;
static bool had_interest = false;

static bool in_link = false;
static GList *uris = NULL;

static void process_node(xmlTextReaderPtr r)
{
        const xmlChar *name = NULL;
        const xmlChar *value = NULL;
        struct vulnerability_t vuln = { 0 };
        struct source_package_t *t = NULL;
        xmlChar *uri = NULL;

        name = xmlTextReaderConstName(r);
        if (!name) {
                return;
        }
        /* New entry */
        if (xmlStrEqual(name, BAD_CAST "entry")) {
                in_entry = !in_entry;
                if (!in_entry) {
                        if (had_interest) {
                                struct cve_entry_t *ent = NULL;

                                ent = calloc(1, sizeof(struct cve_entry_t));
                                gchar *tmpk = NULL, *tmpv = NULL;
                                tmpk = g_strdup((const gchar*)cur_id);
                                tmpv = g_strdup((const gchar*)summary);
                                /* Force overwrite/free correctly */
                                if (g_hash_table_contains(cdb, tmpk)) {
                                        g_hash_table_remove(cdb, tmpk);
                                }
                                ent->id = tmpk;
                                ent->summary = tmpv;
                                ent->uris = uris;
                                g_hash_table_insert(cdb, tmpk, ent);
                                uris = NULL;
                        } else {
                                if (uris) {
                                        g_list_free_full(uris, xmlFree);
                                        uris = NULL;
                                }
                        }
                        if (cur_id) {
                                xmlFree(cur_id);
                                cur_id = NULL;
                        }
                        if (summary) {
                                xmlFree(summary);
                                summary = NULL;
                        }
                        had_interest = false;
                        return;
                }
                if (cur_id) {
                        xmlFree(cur_id);
                }
                cur_id  = xmlTextReaderGetAttribute(r, BAD_CAST "id");
                if (!cur_id) {
                        return;
                }
                return;
        }
        if (xmlStrEqual(name, BAD_CAST "vuln:references")) {
                in_link = !in_link;
                return;
        }
        if (in_link && xmlStrEqual(name, BAD_CAST "vuln:reference")) {
                uri = xmlTextReaderGetAttribute(r, BAD_CAST "href");
                if (!uri) {
                        return;
                }
                uris = g_list_append(uris, uri);
                uri = NULL;
        }
        if (xmlStrEqual(name, BAD_CAST "vuln:vulnerable-software-list")) {
                in_list = !in_list;
                return;
        }
        if (in_list && xmlStrEqual(name, BAD_CAST "vuln:product")) {
                in_product = !in_product;
                return;
        }
        if (in_list && in_product) {
                value = xmlTextReaderConstValue(r);
                if (!value) {
                        return;
                }
                if (!parse_vuln(value, &vuln)) {
                        return;
                }
                t = g_hash_table_lookup(db, vuln.product);
                if (!t) {
                        goto clean;
                }
                if (!(vuln.version && xmlStrEqual(t->version, BAD_CAST vuln.version))) {
                        goto clean;
                }
                /* Determine if its patched. */
                gchar *pnamet = g_ascii_strdown((gchar*)cur_id, -1);
                gchar *pname = g_strdup_printf("%s.patch", pnamet);
                gchar *tpath = g_build_filename(G_DIR_SEPARATOR_S, t->path, PATCH_PREFIX, pname, NULL);

                if (g_file_test(tpath, G_FILE_TEST_EXISTS)) {
                        if (!g_list_find_custom(t->patched, cur_id, (GCompareFunc)strcmp)) {
                                gchar *tmp = g_strdup((const gchar*)cur_id);
                                if (!tmp) {
                                        abort();
                                }
                                t->patched = g_list_append(t->patched, tmp);
                                had_interest = true;
                        }
                } else {
                        if (!g_list_find_custom(t->issues, cur_id, (GCompareFunc)strcmp)) {
                                gchar *tmp = g_strdup((const gchar*)cur_id);
                                if (!tmp) {
                                        abort();
                                }
                                t->issues = g_list_append(t->issues, tmp);
                                had_interest = true;
                        }
                }
                g_free(tpath);
                g_free(pname);
                g_free(pnamet);
clean:
                g_free(vuln.vendor);
                g_free(vuln.product);
                if (vuln.version) {
                        g_free(vuln.version);
                }
                return;
        }
        if (in_entry && xmlStrEqual(name, BAD_CAST "vuln:summary")) {
                in_summary = !in_summary;
                if (in_summary && summary) {
                        xmlFree(summary);
                        summary = NULL;
                }
                return;
        }
        if (in_summary) {
                summary = xmlTextReaderValue(r);
                return;
        }
}

static bool parse_file(const char *fname)
{
        xmlTextReaderPtr r = xmlReaderForFile(fname, NULL, 0);
        int ret;

        while ((ret = xmlTextReaderRead(r)) > 0) {
                process_node(r);
        }
        xmlFreeTextReader(r);

        return false;
}

static bool inspect_spec(const gchar *filename)
{
        xmlDocPtr doc = NULL;
        xmlNodePtr root = NULL;
        xmlNodePtr nxt = NULL;
        xmlNodePtr child = NULL;
        xmlChar *tmp = NULL;
        bool ret = false;
        struct source_package_t *t = NULL;

        xmlChar *source_name = NULL;
        int release = -1;
        xmlChar *version = NULL;

        doc = xmlReadFile(filename, NULL, 0);
        if (!doc) {
                return false;
        }

        root = xmlDocGetRootElement(doc);
        if (!root) {
                goto clean;
        }

        if (!xmlStrEqual(root->name, BAD_CAST "PISI")) {
                printf("Invalid root node\n");
                goto clean;
        }

        for (nxt = root->children; nxt; nxt = nxt->next) {
                if (nxt->type != XML_ELEMENT_NODE) {
                        continue;
                }
                if (xmlStrEqual(nxt->name, BAD_CAST "Source")) {
                        /* Grab child with "Source" name */
                        for (child = nxt->children; child; child = child->next) {
                                if (!(child->type == XML_ELEMENT_NODE && xmlStrEqual(child->name, BAD_CAST "Name"))) {
                                        continue;
                                }
                                if (!child->children) {
                                        /* Screwed */
                                        break;
                                }
                                if (child->children->type != XML_TEXT_NODE) {
                                        /* Moar screwed */
                                        break;
                                }
                                source_name = child->children->content;
                                break;
                        }
                } else if (xmlStrEqual(nxt->name, BAD_CAST "History")) {
                        for (child = nxt->children; child; child = child->next) {
                                if (!(child->type == XML_ELEMENT_NODE && xmlStrEqual(child->name, BAD_CAST "Update"))) {
                                        continue;
                                }
                                tmp = xmlGetProp(child, BAD_CAST "release");
                                if (!tmp) {
                                        g_warning("Missing release property");
                                        continue;
                                }
                                int t_release = atoi((const char*)tmp);
                                if (t_release > release) {
                                        release = t_release;
                                        if (version) {
                                                version = NULL;
                                        }
                                        for (xmlNodePtr sub = child->children; sub; sub = sub->next) {
                                                if (!(sub->type == XML_ELEMENT_NODE && xmlStrEqual(sub->name, BAD_CAST "Version"))) {
                                                        continue;
                                                }
                                                if (sub->children && sub->children->type == XML_TEXT_NODE) {
                                                        version = sub->children->content;
                                                }
                                                break;
                                        }
                                }
                                xmlFree(tmp);
                        }
                }
        }

        if (!version || !source_name) {
                goto clean;
        }

        t = calloc(1, sizeof(struct source_package_t));
        if (!t) {
                goto clean;
        }
        t->name = xmlStrdup(source_name);
        t->version = xmlStrdup(version);
        t->release = release;
        t->path = g_path_get_dirname(filename);

        g_hash_table_insert(db, t->name, t);

        //printf("%s is at version %s, release %d\n", source_name, version, release);
        ret = true;
clean:
        xmlFreeDoc(doc);
        return ret;
}

static int sources = 0;

static void find_sources(const char *directory)
{
        GFile *root = g_file_new_for_path(directory);
        GFileInfo *info = NULL;
        GFileEnumerator *enu = NULL;
        gchar *tpath = NULL;
        const gchar* name = NULL;
        GFileType type;

        enu = g_file_enumerate_children(root, G_FILE_ATTRIBUTE_STANDARD_NAME "," G_FILE_ATTRIBUTE_STANDARD_TYPE, G_FILE_QUERY_INFO_NOFOLLOW_SYMLINKS, NULL, NULL);
        if (!enu) {
                return;
        }
        while ((info = g_file_enumerator_next_file(enu, NULL, NULL)) != NULL) {
                type = g_file_info_get_file_type(info);
                name = g_file_info_get_name(info);
                tpath = g_build_path(G_DIR_SEPARATOR_S, directory, g_file_info_get_name(info), NULL);
                if (!tpath) {
                        abort();
                }

                switch (type) {
                case G_FILE_TYPE_DIRECTORY:
                        find_sources(tpath);
                        break;
                case G_FILE_TYPE_REGULAR:
                        if (g_str_equal(name, "pspec.xml")) {
                                if (inspect_spec((const gchar*)tpath)) {
                                        ++sources;
                                }
                        }
                        break;
                default:
                        /* gtfo */
                        break;
                }
                g_free(tpath);

                g_object_unref(info);
        }
        g_file_enumerator_close(enu, NULL, NULL);
        g_object_unref(enu);
        g_object_unref(root);

        root = NULL;
}

static inline void cve_free(void *v)
{
        if (!v) {
                return;
        }
        struct cve_entry_t *t = v;
        if (t->uris) {
                g_list_free_full(t->uris, xmlFree);
        }
        g_free(t->id);
        g_free(t->summary);
        g_free(t);
}

int main(int argc, char **argv)
{
        GHashTableIter iter;
        gchar *key = NULL;
        struct source_package_t *v = NULL;
        GList *c = NULL, *t = NULL;
        struct cve_entry_t *entry = NULL;
        bool hide_patched = false;
        gchar *path = NULL;

        LIBXML_TEST_VERSION
        db = g_hash_table_new_full(g_str_hash, g_str_equal, NULL, package_free);
        cdb = g_hash_table_new_full(g_str_hash, g_str_equal, NULL, cve_free);

        /* Make configurable.. */
        path = g_strdup_printf("%s/EvolveOS/repository", g_get_home_dir());
        find_sources(path);
        g_free(path);
        printf("Scanned %d packages\n", sources);

        if (argc > 1) {
                for (uint i = 1; i < argc; i++) {
                        if (g_str_equal(argv[i], "-n")) {
                                hide_patched = true;
                                break;
                        }
                }
        }

        for (int i = 2002; i <= 2015; i++) {
                gchar *s = g_strdup_printf("nvdcve-2.0-%d.xml", i);
                printf("Parsing %s\n", s);
                parse_file(s);
                printf("Parsed %s\n", s);
                g_free(s);
        }

        g_hash_table_iter_init(&iter, db);
        while (g_hash_table_iter_next(&iter, (void**)&key, (void**)&v)) {
                if (!v->issues && !v->patched) {
                        continue;
                }
                if (!v->issues && hide_patched) {
                        continue;
                }
                printf("%s %s (%u patched, %u issues)\n"C_WHITE"------------"C_RESET"\n", key, v->version, g_list_length(v->patched), g_list_length(v->issues));
                for (c = v->issues; c; c = c->next) {
                        entry = g_hash_table_lookup(cdb, (gchar*)c->data);
                        printf(" * "C_RED"%s"C_RESET" : %s\n\n", (char*)c->data, entry->summary);
                        /* Print links.. */
                        bool p = false;
                        for (t = entry->uris; t; t = t->next) {
                                printf("     - %s\n", (char*)t->data);
                                p = true;
                        }
                        if (p) {
                                printf("\n");
                        }
                }
                if (!hide_patched) {
                        for (c = v->patched; c; c = c->next) {
                                entry = g_hash_table_lookup(cdb, (gchar*)c->data);
                                printf(" * "C_BLUE"%s [PATCHED]"C_RESET" : %s\n\n", (char*)c->data, entry->summary);
                        }
                }
                printf("\n");
        }

        g_hash_table_unref(db);
        g_hash_table_unref(cdb);

        xmlCleanupParser();
        return EXIT_SUCCESS;
}
