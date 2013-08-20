
#!/usr/bin/python

#Created For SolusOS

from pisi.actionsapi import shelltools, get, cmaketools, pisitools


def setup():
    cmaketools.configure()


def build():
    cmaketools.make()


def install():
    cmaketools.install()

    #EXTRADOCS#
