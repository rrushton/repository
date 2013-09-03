#!/usr/bin/python

# Created For SolusOS
from pisi.actionsapi import pisitools

ThemeDir = "solusos-solusos-branding-8e7c5dcc956e/"  # v0.2


def install():
    pisitools.insinto("/usr/share", "gnome-background-properties")
    pisitools.insinto("/usr/share", "backgrounds")

    pisitools.insinto("/usr/share/themes", "%s/themes/SolusOS-Darker" % ThemeDir)
    pisitools.insinto("/usr/share/icons", "%s/icons/SolusOS" % ThemeDir)
