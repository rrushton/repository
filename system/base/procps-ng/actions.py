
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure ("--prefix=/usr\
						  --exec-prefix=\
						  --libdir=/usr/lib\
						  --docdir=/usr/share/doc/procps-ng-3.3.6\
						  --disable-static\
						  --disable-skill\
						  --disable-kill")
						  
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	
	# Move libraries into lib 
	pisitools.domove ("/usr/lib/libprocps.so*", "/lib")
	
	# Symlink back to /usr
	pisitools.dosym ("/lib/libprocps.so.1.1.0", "/usr/lib/libprocps.so")
