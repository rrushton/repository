#!/usr/bin/python

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/icons","Pacifica")
    pisitools.insinto("/usr/share/icons","Pacifica-U")
    shelltools.system("chmod a+r -R %s/usr/share/icons/Pacifica" % get.installDIR())
    shelltools.system("chmod a+r -R %s/usr/share/icons/Pacifica-U" % get.installDIR())
