#!/usr/bin/python

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def build_config():
    cflags = get.CFLAGS().replace("-ggdb3","")
    cxxflags = get.CXXFLAGS().replace("-gddb3", "")
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cxxflags)


def setup():
    if not get.canClang(): build_config()
    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib/WebKitGTK \
                         --with-gstreamer=1.0 \
                         --enable-introspection \
                         --disable-geolocation \
                         --disable-gtk-doc-html")

def build():
    if not get.canClang(): build_config()
    autotools.make()

def install():
    if not get.canClang(): build_config()
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
