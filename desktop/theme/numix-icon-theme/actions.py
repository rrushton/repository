#!/usr/bin/python

from pisi.actionsapi import shelltools, get, autotools, pisitools

def install():
    pisitools.insinto("/usr/share/icons/Numix", "Numix/*")
    shelltools.system("chmod a+r -R %s/usr/share/icons/Numix" % get.installDIR())
