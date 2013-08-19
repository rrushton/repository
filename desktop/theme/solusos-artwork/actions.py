#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import pisitools

	
def install():
    pisitools.insinto ("/usr/share", "gnome-background-properties")
    pisitools.insinto ("/usr/share", "backgrounds")
    
	
	

