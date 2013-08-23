#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.configure("--enable-pluggable-dialogs \
                         --enable-sound-settings \
                         --enable-xrandr \
                         --enable-libnotify \
                         --enable-gio-unix \
                         --enable-libxklavier \
                         --enable-xcursor")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
