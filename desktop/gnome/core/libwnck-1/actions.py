
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export ("HOME", get.workDIR())

def setup():
    autotools.configure ("--disable-static \
                          --program-suffix=-1")

def build():
    autotools.make ("GETTEXT_PACKAGE=libwnck-1")

def install():
    autotools.rawInstall ("GETTEXT_PACKAGE=libwnck-1 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc ("AUTHORS", "ChangeLog", "COPYING")
