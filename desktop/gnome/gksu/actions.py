#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import autotools, pisitools


def setup():
    # Go back and enable this when we split up nautilus a bit
    autotools.configure("--disable-nautilus-extension")


def build():
    autotools.make()


def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
