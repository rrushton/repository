#!/usr/bin/python

from pisi.actionsapi import pisitools, shelltools, get

def install():
    pisitools.insinto("/usr/share/icons/Faba","*")
    shelltools.system("chmod a+r -R %s/usr/share/icons/Faba" % get.installDIR())
