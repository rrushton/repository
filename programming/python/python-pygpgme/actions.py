#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, pythonmodules, pisitools



def build():
    pythonmodules.compile()


def install():
    pythonmodules.install()

    
