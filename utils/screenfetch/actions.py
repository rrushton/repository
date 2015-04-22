#!/usr/bin/python


from pisi.actionsapi import get, autotools, pisitools, shelltools

def install():
    pisitools.dobin("screenfetch-dev")
    shelltools.system("mv \"%s/usr/bin/screenfetch-dev\" \"%s/usr/bin/screenfetch\"" % (get.installDIR(),get.installDIR()))
    pisitools.doman("screenfetch.1")
    pisitools.dodoc("COPYING", "CHANGELOG")
