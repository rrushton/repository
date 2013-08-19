
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    # TODO: Add GStreamer video support
    autotools.configure ()
						  
def build():
	autotools.make ()
	
def install():
	autotools.install ()
	
	pisitools.dodoc ("AUTHORS", "ChangeLog", "COPYING")
	
	

