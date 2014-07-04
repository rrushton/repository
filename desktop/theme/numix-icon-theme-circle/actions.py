#!/usr/bin/python

from pisi.actionsapi import pisitools, shelltools, get

def install():
    pisitools.insinto("/usr/share/icons/Numix-Circle", "Numix-Circle/*")
    shelltools.system("chmod a+r -R %s/usr/share/icons/Numix-Circle" % get.installDIR())
