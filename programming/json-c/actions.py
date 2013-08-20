
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure("--disable-static")

def build():
    # Package fails parallel make
    autotools.make("-j1")

def install():
    autotools.install ()
    pisitools.dodoc ("COPYING", "AUTHORS", "ChangeLog", "README")
