#!/usr/bin/python
# Created for SolusOS

from pisi.actionsapi import pisitools, autotools,get

def setup():
	autotools.rawConfigure("--prefix=/usr --enable-shared")

def build():
	autotools.make()


def install():
	autotools.rawInstall("DESTDIR='%s'" % get.installDIR())

	pisitools.dodoc("change.log","README","example.c","*.txt")


