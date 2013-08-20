
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export ("HOME", get.workDIR())

def setup():
	autotools.configure ("--prefix=/usr \
						  --sysconfdir=/etc \
						  --libexecdir=/usr/lib/GConf \
						  --disable-orbit \
						  --disable-static")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
	pisitools.dosym ("/etc/gconf/gconf.xml.defaults", "/etc/gconf/gconf.xml.system")
	
	pisitools.dodoc ("ChangeLog", "COPYING")
