
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools
						
def build():
	autotools.make()
		
def install():
	pisitools.insinto("/usr/games", "greed")
	pisitools.doman("greed.6")
	pisitools.dodoc ("COPYING", "README")
	shelltools.makedirs("%s/var/games/greed" % get.installDIR())
