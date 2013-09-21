#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    shelltools.system("qmake")


def build():
    autotools.make()


def install():
    autotools.rawInstall("INSTALL_ROOT=%s/usr" % get.installDIR())
    pisitools.dodoc("LGPL_EXCEPTION.TXT")

