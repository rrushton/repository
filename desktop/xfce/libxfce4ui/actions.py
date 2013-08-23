#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.configure("--enable-startup-notification \
                         --with-vendor-info=SolusOS")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
