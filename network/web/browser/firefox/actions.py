
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import autotools, shelltools, pisitools

def build():
    autotools.make ("-f client.mk")
    #autotools.make ("-C firefox-build-dir/browser/installer")

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc ("LICENSE", "AUTHORS", "COPYING", "ChangeLog", "CHANGELOG")
