
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ()

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    for target in ["/usr/lib/libhogweed.so.2.3", "/usr/lib/libnettle.so.4.5"]:
        shelltools.chmod ("%s/%s" % (get.installDIR(), target), mode=0755)

    pisitools.dodoc ("nettle.html")
