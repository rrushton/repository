
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import pisitools, waftools

def setup():
    waftools.configure ()
						
def build():
	waftools.make ()
	
def install():
    waftools.install ()

    pisitools.dodoc ("AUTHORS", "COPYING")



