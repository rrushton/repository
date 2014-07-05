#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                          --enable-systemd \
                          --disable-documentation \
                          --libexecdir=/usr/lib/gnome-control-center")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR() )

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
