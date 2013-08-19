#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools, get, shelltools, pisitools

def setup():
	autotools.configure()

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "ChangeLog", "NEWS",
					"PROJECTS", "README", "THANKS", "TODO", "VERSION")
	pisitools.domove("/usr/share/gnupg/FAQ", "/usr/share/doc/")
