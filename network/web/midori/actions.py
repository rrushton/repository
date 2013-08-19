
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("JOBS",get.makeJOBS().replace('-j',''))

def setup():
	autotools.rawConfigure ("--prefix=/usr \
							 --enable-nls \
							 --disable-unique \
							 --enable-addons \
							 --enable-gtk3")
						  
def build():
	#autotools.make ()
	shelltools.system("make")
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	
	pisitools.dodoc ("COPYING", "ChangeLog", "AUTHORS")
	
	

