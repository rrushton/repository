
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
