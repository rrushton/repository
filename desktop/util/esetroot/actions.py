
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools

def build():
    autotools.make()

def install():
    pisitools.dobin ("Esetroot")
    pisitools.dodoc ("LICENSE")
