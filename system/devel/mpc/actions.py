
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools



def setup():
	autotools.configure ("--prefix=/usr")
	
def build():
	autotools.make ()

def check():
	autotools.make ("check")
		
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
	# TODO: Add docs
