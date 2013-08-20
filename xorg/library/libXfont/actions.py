
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure ("--disable-devel-docs")
						
def build():
	autotools.make ()
	
def install():
	autotools.install ()
	
