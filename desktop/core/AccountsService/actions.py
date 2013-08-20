
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export ("HOME", get.workDIR())

def setup():
	autotools.configure ("--prefix=/usr \
						  --sysconfdir=/etc \
						  --localstatedir=/var \
						  --libexecdir=/usr/lib/accountsservice \
						  --disable-static")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
		
	pisitools.dodoc ("README", "COPYING", "AUTHORS")
