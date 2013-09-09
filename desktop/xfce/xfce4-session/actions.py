#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.configure("--enable-systemd")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "BUGS", "COPYING")
