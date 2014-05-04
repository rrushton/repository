
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    autotools.configure ("--libexecdir=/usr/lib/polkit-gnome \
                                              --disable-static")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc ("README", "NEWS", "COPYING", "AUTHORS")
