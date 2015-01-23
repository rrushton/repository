#!/usr/bin/python

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --with-package-name=\"GStreamer Base Plugins 1.4.5 Evolve OS\" \
                         --with-package-origin=\"https://evolve-os.com\"")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
