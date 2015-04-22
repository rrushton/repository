#!/usr/bin/python


from pisi.actionsapi import get, pythonmodules, pisitools



def build():
    pythonmodules.compile()


def install():
    pythonmodules.install()

    
