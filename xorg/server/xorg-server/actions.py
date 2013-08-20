
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure ("--with-xkb-output=/var/lib/xkb \
						  --enable-install-setuid\
						  --prefix=/usr\
						  --disable-static")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
