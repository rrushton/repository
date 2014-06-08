#!/usr/bin/python
# Created for SolusOS

from pisi.actionsapi import pisitools, autotools,get

def setup():
    autotools.configure("--prefix=/usr \
                         --mandir=/usr/share/man \
                         --with-jpeg8 \
                         --disable-static")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
