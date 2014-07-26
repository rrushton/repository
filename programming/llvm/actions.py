#!/usr/bin/python

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    autotools.rawConfigure("--prefix=/usr              \
                            --sysconfdir=/etc          \
                            --libdir=/usr/lib/llvm     \
                            --enable-libffi            \
                            --enable-optimized         \
                            --enable-shared            \
                            --disable-assertions       \
                            --disable-debug-runtime    \
                            --disable-expensive-checks")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fix permissions of the static files
    shelltools.chmod("%s/usr/lib/*.a" % get.installDIR(), mode=0644)

    pisitools.domove("/usr/docs", "/usr/share/", "doc")
