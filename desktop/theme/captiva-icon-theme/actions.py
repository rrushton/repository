#!/usr/bin/python

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/icons","Captiva")
    shelltools.system("chmod a+r -R %s/usr/share/icons/Captiva" % get.installDIR())
