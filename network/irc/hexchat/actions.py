
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    shelltools.system("sh autogen.sh")
    autotools.configure("--enable-socks \
                         --enable-openssl=/usr/include/openssl \
                         --enable-spell=gtkspell")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc(get.workDIR() + "/" + get.srcDIR() +"/share/doc/*")
