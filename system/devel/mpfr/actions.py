
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools



def setup():
    autotools.configure ("--prefix=/usr\
                                              --enable-thread-safe\
                                              --docdir=/usr/share/doc/mpfr")

def build():
    autotools.make ()

def check():
    autotools.make ("check")

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    # Make docs
    autotools.make ("html")
    autotools.make ("DESTDIR=%s install-html" % get.installDIR())
