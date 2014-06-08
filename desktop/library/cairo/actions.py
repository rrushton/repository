
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    # We need to --enable-gl in the future for Wayland
    autotools.configure("--disable-static \
                         --enable-xlib-xcb \
                         --enable-tee")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
