#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    # TODO: Investigate build failure with GJS
    autotools.configure("--disable-static \
                         --enable-python2 \
                         --disable-gjs \
                         --enable-gtk \
                         --disable-compile-warnings")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
