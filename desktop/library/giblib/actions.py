
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.rawConfigure ("--prefix=/usr \
                                                     --disable-static")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir('/usr/doc')

    pisitools.dodoc("README","AUTHORS","COPYING","ChangeLog")
