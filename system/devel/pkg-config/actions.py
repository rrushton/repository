
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	# Multiarch tuples (be compatible with Ubuntu & Debian's multiarch implementation
	if "i686" in get.HOST():
		m_tuple = "i386-linux-gnu"
	else:
		m_tuple = " x86_64-linux-gnu"
		
	pcDirs = "/usr/local/lib/%(MULTIARCH)s/pkgconfig:/usr/local/lib/pkgconfig:/usr/local/share/pkgconfig:/usr/lib/%(MULTIARCH)s/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig" % { 'MULTIARCH' : m_tuple }
	autotools.configure("--prefix=/usr \
						 --docdir=/usr/share/doc/pkg-config \
						 --with-internal-glib \
						 --with-pc-path=%s\
						 --disable-host-tool" % pcDirs)
					
def build():
	autotools.make()
	
def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	
	pisitools.dodoc ("AUTHORS", "COPYING", "ChangeLog", "README")
	
