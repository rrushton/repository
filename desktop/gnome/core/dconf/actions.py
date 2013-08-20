
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export ("HOME", get.workDIR())

def setup():
	autotools.configure ("--prefix=/usr \
						  --sysconfdir=/etc \
						  --libexecdir=/usr/lib/dconf \
						  --disable-man \
						  --disable-static")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
		
	pisitools.dodoc ("NEWS", "COPYING")
