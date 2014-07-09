#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    # We need to --enable-cogl in the future for cogl surface support
    # Also want libdrm once we update it and mesa
    autotools.configure("--disable-static \
                         --enable-xlib-xcb \
                         --enable-tee \
                         --enable-gl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
