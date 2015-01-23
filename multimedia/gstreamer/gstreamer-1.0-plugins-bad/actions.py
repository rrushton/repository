#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())


def setup():
    autotools.configure("--disable-static \
                         --with-package-name=\"GStreamer Bad Plugins 1.4.5 Evolve OS\" \
                         --with-package-origin=\"https://evolve-os.com\"")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "AUTHORS")
