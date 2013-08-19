
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

#def build():
#   autotools.make('-j1')
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc ("COPYING", "BUGS", "README")
