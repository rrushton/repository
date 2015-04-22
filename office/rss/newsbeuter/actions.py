
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools

def build():
    autotools.make ()

def install():
    autotools.install ()
    pisitools.dodoc ("AUTHORS", "LICENSE")
