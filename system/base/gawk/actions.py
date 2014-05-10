
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.autoconf()
    autotools.rawConfigure("--prefix=/usr \
                            --libexecdir=/usr/lib\
                            --bindir=/bin")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove hard numbered versions
    pisitools.remove("/bin/*awk-*")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "LIMITATIONS", "NEWS",
                                    "PROBLEMS", "README")
