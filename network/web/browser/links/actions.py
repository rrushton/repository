#!/usr/bin/python

from pisi.actionsapi import autotools, pisitools, get

def setup():
	autotools.configure ("--prefix=/usr \
						  --enable-graphics \
						  --with-gpm \
						  --without-svgalib \
						  --without-atheos")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	
	pisitools.dodoc("AUTHORS", "NEWS","README", "ChangeLog")
