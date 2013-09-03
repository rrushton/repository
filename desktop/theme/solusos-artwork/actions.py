#!/usr/bin/python

# Created For SolusOS
from pisi.actionsapi import pisitools

ThemeDir = "solusos-solusos-branding-8f5ff16b690d/themes"  # v0.1


def install():
    pisitools.insinto("/usr/share", "gnome-background-properties")
    pisitools.insinto("/usr/share", "backgrounds")

    pisitools.insinto("/usr/share/themes", "%s/SolusOS-Darker" % ThemeDir)
