
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure ("--disable-libunwind")
						
def build():
	autotools.make ()
	
def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    for item in ["flower", "smoke", "image", "resizor", "eventdemo"]:
        pisitools.dobin ("clients/%s" % item)

    pisitools.dodoc ("COPYING")

	

