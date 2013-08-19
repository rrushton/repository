
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
	autotools.configure ("--prefix=/usr\
						  --docdir=/usr/share/doc/python-dbus")

def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
