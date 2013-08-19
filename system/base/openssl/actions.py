
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	shelltools.system ("./config --prefix=/usr\
						--openssldir=/etc/ssl\
						shared\
						zlib-dynamic")
						  
def build():
	autotools.make ("-j1")
	
def install():
	autotools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())
