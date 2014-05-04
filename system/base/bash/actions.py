
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ("--prefix=/usr\
                                              --mandir=/usr/share/man\
                                              --infodir=/usr/share/info\
                                              --with-curses\
                                              --enable-history\
                                              --with-installed-readline")

def build():
    autotools.make ()

def install():
    autotools.install ()

    # Bash defaults to /usr/bin/bash, move it to /bin
    pisitools.domove ("/usr/bin/bash", "/bin/")
