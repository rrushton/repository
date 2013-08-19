
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    autotools.autoreconf ("-vfi")
    autotools.configure ("--prefix=/usr\
                          --with-pcre=system")
						  
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
