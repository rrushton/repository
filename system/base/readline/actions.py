#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created for SolusOS

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def get_multiarch_host ():
	if get.ARCH() == "x86_64":
		return "x86_64-linux-gnu"
	else:
		return "i386-linux-gnu"
		
def setup():
    autotools.configure("--with-curses --disable-static"  )
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.removeDir("/usr/bin")

    pisitools.dohtml("doc/")
    pisitools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS")
