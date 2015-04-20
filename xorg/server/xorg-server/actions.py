#!/usr/bin/python

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    # TODO: Check systemd integration
    autotools.configure("--with-xkb-output=/var/lib/xkb \
                         --enable-install-setuid \
                         --enable-suid-wrapper \
                         --with-xkb-path=/usr/share/X11/xkb \
                         --with-fontrootdir=/usr/share/fonts \
                         --enable-glamor \
                         --enable-xwayland \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
