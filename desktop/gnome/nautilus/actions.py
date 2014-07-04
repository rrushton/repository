#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-tracker \
                         --disable-static \
                         --enable-packagekit \
                         --libexecdir=/usr/lib/nautilus")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING")

    # Cleanup
    for item in ["XMLnamespaces", "mime.cache", "icons", "aliases", \
                 "types", "magic", "generic-icons", "subclasses", "globs", \
                 "version", "globs2", "treemagic"]:
        pisitools.remove("/usr/share/mime/%s" % item)
