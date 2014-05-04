#!/usr/bin/python

# Created for SolusOS

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

    # Remove some empty directories.
    os.removedirs("%s/usr/bin" % get.installDIR())
    os.removedirs("%s/usr/share/man/man1" % get.installDIR())

    pisitools.dodoc ("README", "NEWS", "COPYING")
