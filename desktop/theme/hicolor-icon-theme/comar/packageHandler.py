#!/usr/bin/python

import piksemel
import os

def updateIconThemes (filepath):
    parse = piksemel.parse (filepath)
    for xmlfile in parse.tags("File"):
        path = xmlfile.getTagData ("Path")
        if "/share/icons/" in path:
            theme_dir = path.split("/")[4]
            os.system ("/usr/bin/gtk-update-icon-cache -ft \"/usr/share/icons/%s\"" % theme_dir) 
            break

def setupPackage (metapath, filepath):
    updateIconThemes (filepath)

def postCleanupPackage (metapath, filepath):
    updateIconThemes (filepath)
