#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.configure("--disable-static \
                         --with-package-name=\"GStreamer Base Plugins 1.4.1 Evolve OS\" \
                         --with-package-origin=\"https://evolve-os.com\"")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
