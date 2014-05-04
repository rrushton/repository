
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doman("%s/usr/share/gc/gc.man" % get.installDIR())
    shelltools.move("%s/usr/share/gc/" % get.installDIR(), "%s/usr/share/doc/bdwgc/" % get.installDIR())
    pisitools.rename("/usr/share/doc/bdwgc/README.linux", "README")
    pisitools.remove("/usr/share/doc/bdwgc/README.*")
    pisitools.dodoc ("ChangeLog")
