#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def install():
    pisitools.insinto("/usr/share/icons/Numix", "Numix/*")
