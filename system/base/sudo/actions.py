
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ("--libexecdir=/usr/lib/sudo \
                          --docdir=/usr/share/doc/sudo \
                          --with-all-insults \
                          --with-env-editor ")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
	pisitools.dodoc ("ChangeLog")
	
	

