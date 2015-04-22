
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, pythonmodules, pisitools

WorkDir = "python-polkit-master"

def install():
    pythonmodules.install ()

    pisitools.dodoc ("COPYING", "AUTHORS", "README")
