#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools, shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j",""))
shelltools.export("DESTDIR", get.installDIR())

def setup():
    autotools.configure()


def build():
    shelltools.system("make")


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    
