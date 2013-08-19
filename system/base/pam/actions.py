
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure ("--prefix=/usr \
						  --sysconfdir=/etc \
						  --docdir=/usr/share/doc/Linux-PAM-1.1.6 \
						  --disable-nis")
						  
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	shelltools.chmod ("%s/sbin/unix_chkpwd" % get.installDIR(), 4755)
