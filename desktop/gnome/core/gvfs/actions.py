
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ("--disable-gphoto2 \
                          --disable-documentation \
                          --libexecdir=/usr/lib/gvfs")
						  
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
	pisitools.dodoc ("AUTHORS", "ChangeLog", "COPYING")
	
	

