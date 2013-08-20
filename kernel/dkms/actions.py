#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import pisitools, autotools, get

def build():
    autotools.make ()

def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR()),
