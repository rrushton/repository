
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/lib/*.a")
    pisitools.domove("/usr/lib/libusb*", "/lib/")
    pisitools.dosym("/lib/libusb-1.0.so.0.1.0", "/usr/lib/libusb.1.0.so")
