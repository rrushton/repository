#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib/gedit")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR() )

    pisitools.dodoc("AUTHORS", "ChangeLog", "BUGS", "COPYING")
