#!/usr/bin/python

from pisi.actionsapi import shelltools, get, autotools, pisitools, cmaketools

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build-web")
    shelltools.cd("build-web")
    cmaketools.configure("-DPORT=GTK")

def build():
    shelltools.cd("build-web")
    autotools.make()

def install():
    shelltools.cd("build-web")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
