#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import pisitools

WorkDir = "."


# Don't strip or modify the binaries in any way
NoStrip = ["/usr/bin/flash-player-properties",
           "/usr/lib/mozilla/plugins/libflashplayer.so"]


def install():
    pisitools.insinto("/", "usr")

    # Not currently interested in the KDE component
    pisitools.remove("/usr/lib/kde4/kcm_adobe_flash_player.so")
    pisitools.removeDir("/usr/lib")
    pisitools.removeDir("/usr/share/kde4/")

    # Make the plugin available to Firefox
    pisitools.insinto("/usr/lib/mozilla/plugins", "libflashplayer.so")
