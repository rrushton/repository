#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools, shelltools

def setup():
    shelltools.system("./configure --prefix=/usr --disable-manualupdatecheck --disable-autoupdatecheck --disable-static --with-tinyxml=builtin")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog")
