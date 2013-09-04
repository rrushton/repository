#!/usr/bin/python

# Created For SolusOS
from pisi.actionsapi import pisitools

ThemeDir = "solusos-solusos-branding-4cf04b1275a6/"  # v0.3


def install():
    pisitools.insinto("/usr/share", "gnome-background-properties")
    pisitools.insinto("/usr/share", "backgrounds")

    pisitools.insinto("/usr/share/themes", "%s/themes/SolusOS-Darker" % ThemeDir)
    pisitools.insinto("/usr/share/icons", "%s/icons/SolusOS" % ThemeDir)

    pisitools.insinto("/usr/share/plymouth/themes", "%s/plymouth" % ThemeDir, "solusos")
    
