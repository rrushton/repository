
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure()

def build():
	autotools.make()
	
def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	#Remove empty /etc - does this on a source install, not PiSi issue
	pisitools.removeDir("/etc")
