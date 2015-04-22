
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ()

def build():
    autotools.make ()

def install():
    autotools.install ()
    autotools.make ("install-ti DESTDIR=%s" % get.installDIR())
