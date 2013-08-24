#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.configure("--disable-alsaconf \
                         --disable-xmlto")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING")
