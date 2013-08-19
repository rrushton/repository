
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, pythonmodules, pisitools

	
def install():
	pythonmodules.install ()

	pisitools.dodoc ("COPYING", "COPYING2", "ChangeLog", "README", "TODO")
	pisitools.domove ("/usr/share/doc/pycurl", "/usr/share/doc/python-pycurl")
