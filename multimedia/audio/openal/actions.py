#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, cmaketools, autotools, pisitools


def setup():
    cmaketools.configure()


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    
