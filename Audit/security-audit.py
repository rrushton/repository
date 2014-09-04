#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  security-audit.py
#
#  Note this is Work In Progress!
#  Uses the National Vulnerability Database to discover CVEs
#  and the affected software. Currently this script is limited
#  to direct matches for package names, and could do with
#  some fuzzy checking or mapping.
#  Also note the tool cannot currently determine whether the repo
#  package has already been patched against a vulnerability, and
#  certain versioning schemes may generate false positives here.
#
#  Copyright 2013 Ikey Doherty <ikey@solusos.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os
import os.path
import sys
import shutil
from xml.dom.minidom import parse as parse_xml

us = us = os.path.dirname(os.path.abspath(__file__))
repo_base = "/".join(us.split("/")[:-1])

from distutils.version import LooseVersion

# Append dloader to the path
sys.path.append(os.path.join(repo_base, "Scripts"))
from dloader import download_file


packages = dict()
NVDCVE_DB = "http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-modified.xml"


''' XML Helpers '''
gall = lambda x, y: x.getElementsByTagName(y)
get_value = lambda x, y: x.getElementsByTagName(y)[0].firstChild.nodeValue
get_attr = lambda x, y: x.getAttribute(y)


class Vulnerability:
    ''' Reusable object describing a vulnerability '''
    def __init__(self):
        self.vendor = None
        self.affected_versions = []
        self.product = None
        self.cve_id = None
        self.description = None
        self.web_links = []


class NVDCVEDB:
    ''' Represents the current CVE Database '''

    def __init__(self):
        self.db_file = os.path.join(os.environ["HOME"], "nvdcve_db.xml")
        self.vulnerabilities = []

    def check_installation(self):
        if not os.path.exists(self.db_file):
            # Do nothing
            try:
                cwd = os.getcwd()
                dirname = os.path.dirname(self.db_file)
                os.chdir(os.path.dirname(self.db_file))
                download_file(NVDCVE_DB)
                shutil.move(os.path.join(dirname, "nvdcve-2.0-modified.xml"),
                            "nvdcve_db.xml")
                os.chdir(cwd)
            except Exception, e:
                print e

    def load_db(self):
        ''' Load the database '''
        xml = parse_xml(self.db_file)
        entries = xml.getElementsByTagName("entry")
        for entry in entries:
            vuln = Vulnerability()
            vuln.cve_id = get_attr(entry, "id")
            # Find the vulnerable software for this cve_id
            affected_xml = gall(entry, "vuln:vulnerable-software-list")
            if len(affected_xml) == 0:
                continue
            affected = affected_xml[0]
            vuln.description = get_value(entry, "vuln:summary")
            for link in gall(entry, "vuln:references"):
                type_ref = get_attr(link, "reference_type")
                href = get_attr(gall(link, "vuln:reference")[0], "href")
                source = get_value(link, "vuln:source")
                vuln.web_links.append("%s [%s]  - %s" %
                                      (source, type_ref, href))
            for product in gall(affected, "vuln:product"):
                value = product.firstChild.nodeValue
                # Parse the field
                fld = value.split("cpe:/")
                #print value
                fields = fld[1].split(":")
                vendor = fields[1]
                product = fields[2]
                version = None
                try:
                    version = fields[3]
                    vuln.affected_versions.append(version)
                except:
                    pass
                if vuln.vendor is None:
                    vuln.vendor = vendor
                if vuln.product is None:
                    vuln.product = product
                #print vendor, product, version
            self.vulnerabilities.append(vuln)


def print_report(vuln):
    print "## %s" % vuln.cve_id
    print "## %s:%s" % (vuln.vendor, vuln.product)
    print "## --------\n %s" % vuln.description
    print "# Links:"
    print "\n".join(vuln.web_links)
    print "##\n"


def parse_pspec(location):
    spec = parse_xml(location)
    source_name = get_value(gall(spec, "Source")[0], "Name")
    updates = gall(gall(spec, "History")[0], "Update")
    highest_release = 0
    version = None
    for update in updates:
        release = int(get_attr(update, "release"))
        if release > highest_release:
            highest_release = release
            version = get_value(update, "Version")
    return (source_name, version)


def main():
    # filter..
    filters = list()
    if len(sys.argv) > 2 and sys.argv[1] == "-f":
        t_filters = sys.argv[2].split(",")
        for f in t_filters:
            filters.append(f.strip())

    # Walk the tree to find all packages
    print "Discovering all source files..."
    for root, dirs, files in os.walk(repo_base):
        if "pspec.xml" in files and "actions.py" in files:
            package_name = root.split("/")[-1]
            packages[package_name] = root

    our_packages = dict()
    print "Parsing all source files..."
    for package in packages:
        spec = os.path.join(packages[package], "pspec.xml")
        pkg, version = parse_pspec(spec)
        our_packages[pkg] = (version,packages[package])

    vdb = NVDCVEDB()
    vdb.check_installation()
    print "Loading database, please wait"
    vdb.load_db()
    print "%d vulnerabilities in latest report" % len(vdb.vulnerabilities)

    reports = 0
    for vulnerability in vdb.vulnerabilities:
        if vulnerability.product in our_packages:
            package,basedir = our_packages[vulnerability.product]
            for applicable in vulnerability.affected_versions:
                if LooseVersion(applicable) == LooseVersion(package):
                    # Check we haven't already patched this
                    patch = os.path.join(basedir, "files/security/%s.patch" % vulnerability.cve_id.lower())
                    if not os.path.exists(patch):
                        reports += 1
                        name = "%s:%s" % (vulnerability.vendor, vulnerability.product)
                        if name in filters:
                            continue
                        else:
                            print_report(vulnerability)

    print "Discovered %d potentially insecure packages" % reports


if __name__ == "__main__":
    main()
