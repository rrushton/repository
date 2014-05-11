#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

# Circular deps  - woo
IgnoreAutodep = True

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-login \
                         --disable-su")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # Conflicts with e2fsprogs
    pisitools.remove("/usr/share/man/man8/fsck.8")

    pisitools.dosym ("/bin/mount", "/usr/bin/mount")
    pisitools.dosym ("/bin/umount", "/usr/bin/umount")
