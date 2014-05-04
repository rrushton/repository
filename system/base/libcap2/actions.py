
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools



def build():
    autotools.make()

def install():
    autotools.rawInstall("RAISE_SETFCAP=no DESTDIR=%s" % get.installDIR())
