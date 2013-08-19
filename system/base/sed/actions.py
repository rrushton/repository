
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.rawConfigure("--prefix=/usr \
							--bindir=/bin")
					  
def build():
	autotools.make()
	
def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dosym("/bin/sed", "/usr/bin/sed")
	pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS",
					"README", "THANKS")
