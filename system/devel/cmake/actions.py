 #!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools,get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --datadir=/share/cmake \
                            --docdir=/share/doc \
                            --mandir=/share/man \
                            --system-libs \
                            --no-qt-gui")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
