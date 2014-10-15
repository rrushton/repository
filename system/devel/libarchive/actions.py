#!/usr/bin/python

# Created for Evolve OS

from pisi.actionsapi import autotools, get, pisitools
import os

def setup():
    autotools.configure("--prefix=/usr \
                         --disable-bsdtar \
                         --disable-bsdcpio \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share/man/man1")

    pisitools.dodoc ("README", "NEWS", "COPYING")
