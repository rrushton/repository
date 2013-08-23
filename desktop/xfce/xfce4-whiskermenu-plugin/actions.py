#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import get, cmaketools, pisitools


def setup():
    cmaketools.configure()


def build():
    cmaketools.make()


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING")
