
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    autotools.rawConfigure()
                          
def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc ("COPYING", "Copyright", "README")
    
    #Provided by Aspell and conflicts
    pisitools.remove("/usr/lib/aspell-0.60/iso-8859*")
