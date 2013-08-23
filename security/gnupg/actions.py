#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools, get, pisitools


def setup():
    autotools.configure("--libexecdir=/usr/lib/GnuPG")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING")
