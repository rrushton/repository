#!/usr/bin/python
# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools, libtools

def setup():
        autotools.autoreconf("-vfi")
        autotools.configure()


def build():
        autotools.make()


def install():
        autotools.install()
        pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog",
                        "NEWS", "README")
