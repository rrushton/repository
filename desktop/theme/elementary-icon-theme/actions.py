
#!/usr/bin/python

# Created for solusos

from pisi.actionsapi import pisitools

def install():
	pisitools.insinto("/usr/share/icons","elementary")
	pisitools.insinto("/usr/share/icons",'elementary-mono-dark')
