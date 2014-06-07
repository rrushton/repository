
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    pisitools.dosed("configure.ac", "pthread-stubs", "")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-xinput\
                         --docdir=/usr/share/doc/libxcb-1.9")

    # configure routine gets this wrong
    pisitools.dosed("doc/Makefile", "/root/install-sh", "%s/libxcb-1.9/install-sh" % get.workDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
