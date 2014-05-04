#!/usr/bin/python
# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    autotools.configure("--with-ncurses \
                            --datarootdir=/usr/share/cgames")
def build():
    autotools.make()

def install():
    autotools.install()

    #Classics.txt is for cblocks
    pisitools.domove("/usr/share/Classics.txt", "/usr/share/cgames/cblocks/")
    #Rest of the files are Sokoban puzzles
    pisitools.domove("/usr/share/*.txt", "/usr/share/cgames/csokoban")

    pisitools.dodoc("Changelog", "COPYING", "README")
