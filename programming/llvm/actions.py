#!/usr/bin/python

# Created For SolusOS

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
                            --disable-expensive-checks \
                            --enable-experimental-targets=R600")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fix permissions of the static files
    shelltools.chmod("%s/usr/lib/llvm/*.a" % get.installDIR(), mode=0644)

    # Fix the llvm link
    pisitools.dosym("/usr/lib/llvm/libLLVM-3.2.so", "/usr/lib/libLLVM-3.2.so")
