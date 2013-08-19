
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	pisitools.system("./autogen.sh")
	autotools.configure("--with-x")

def build():
	autotools.make()
	
def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("AUTHORS", "LICENSE", "NEWS", "README")
