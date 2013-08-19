
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
	shelltools.export ("HOME", get.workDIR())
	autotools.configure ("--disable-static")
						  
def build():
	shelltools.export ("HOME", get.workDIR())
	autotools.make ()
	
def install():
	shelltools.export ("HOME", get.workDIR())
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
