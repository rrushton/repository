#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import autotools, get


def build():
    autotools.make()


def install():
    autotools.install("PREFIX=%s/usr" % get.installDIR())
