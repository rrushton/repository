
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools
import glob

WorkDir = "."

FontDir = "/usr/share/fonts/truetype/droid/"

def install():

    for i in glob.glob ("*.ttf"):
        pisitools.insinto (FontDir, i)
        		
	pisitools.dodoc ("README")
