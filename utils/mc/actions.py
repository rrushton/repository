#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools, shelltools, get

def setup():
	autotools.autoconf()
	shelltools.system("aclocal")
	#autotools.autoreconf()
	autotools.configure("--with-screen=ncurses")

def build():
	autotools.automake("--add-missing")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
