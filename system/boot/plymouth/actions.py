#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools, libtools


def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-pango \
                         --enable-gtk \
                         --enable-drm \
                         --enable-systemd-integration \
                         --with-logo=/usr/share/pixmaps/SolusOS_Splash.png")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
