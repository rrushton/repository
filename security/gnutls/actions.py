
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure ("--disable-static\
						  --with-default-trust-store-file=/etc/ssl/ca-certificates.crt")
						  
def build():
	autotools.make ()
	
def install():
	autotools.install ()
	
	# Install docs
	autotools.make ("-C doc/reference install-data-local DESTDIR=%s" % get.installDIR())
	pisitools.dodoc ("COPYING", "COPYING.LESSER", "ChangeLog")
