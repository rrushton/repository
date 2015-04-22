
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ("--libexecdir=/usr/lib/icon-naming-utils")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc ("AUTHORS", "ChangeLog", "COPYING")
