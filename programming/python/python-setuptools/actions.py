
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import pythonmodules, pisitools

def build():
    pythonmodules.compile()

def check():
    pythonmodules.compile("test")

def install():
    pythonmodules.install()

    
