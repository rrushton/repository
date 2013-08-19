
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure()
					  
def build():
	autotools.make()
	
def install():
	autotools.install()
	pisitools.domove("/usr/lib/libmagic.*", "/lib/")
	pisitools.dosym("/lib/libmagic.so.1.0.0", "/usr/lib/libmagic.so")
