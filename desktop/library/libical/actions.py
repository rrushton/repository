
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, cmaketools, pisitools


def setup():
	cmaketools.configure ("-DCMAKE_BUILD_TYPE=Release")
						
def build():
	cmaketools.make ()
	
def install():
	cmaketools.install ()
	
	pisitools.dodoc ("LICENSE", "AUTHORS", "ChangeLog", "COPYING")
	
	

