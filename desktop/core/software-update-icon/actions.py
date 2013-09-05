#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import get, shelltools, pisitools


def install():
    pisitools.dobin("software-update-icon.py")
    shelltools.move("%s/usr/bin/software-update-icon.py" % get.installDIR(), "%s/usr/bin/software-update-icon" % get.installDIR())
    pisitools.insinto("/etc/xdg/autostart", "software-update-icon.desktop")
