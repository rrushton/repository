#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import pythonmodules, pisitools


def build():
    pythonmodules.compile()


def install():
    pythonmodules.install()

    # Copy in our data files
    pisitools.insinto("/usr/share/os-installer", "data/*")

    # Change log
    pisitools.insinto("/usr/share/os-installer", "changes")

    # Icons
    pisitools.insinto("/usr/share/icons", "dist/logo.png", "os-installer.png")
    pisitools.insinto("/usr/share/icons/gnome/scalable/action", "dist/icons/*")

    # Desktop file
    pisitools.insinto("/usr/share/applications", "dist/os-installer.desktop")
    pisitools.dosym("/usr/share/applications/os-installer.desktop", \
                    "/etc/xdg/autostart/os-installer.desktop")
    pisitools.dosym("/usr/share/applications/os-installer.desktop", \
                    "/etc/skel/Desktop/os-installer.desktop")
                    
    # Configuration file
    pisitools.insinto("/etc/os-installer", "dist/install.conf")

    # PolicyKit conf
    pisitools.insinto("/usr/share/polkit-1/actions", "dist/*.policy")

