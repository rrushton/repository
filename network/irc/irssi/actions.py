
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools, perlmodules


def setup():
	# Patch manpage for conf file location
	pisitools.dosed("docs/irssi.1", "/etc/irssi.conf", "/etc/irssi/irssi.conf")
	autotools.configure("--sysconfdir=/etc/irssi \
						 --with-socks \
						 --with-bot \
						 --with-proxy \
						 --with-ncurses")

def build():
	autotools.make()
	
def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "TODO")
	pisitools.remove("/usr/lib/perl5/5.16.3/i686-linux/perllocal.pod")
