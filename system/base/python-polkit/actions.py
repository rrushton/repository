
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, pythonmodules, pisitools

WorkDir = "python-polkit-master"

def install():
    pythonmodules.install ()

    pisitools.dodoc ("COPYING", "AUTHORS", "README")
