
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools
from pisi.actionsapi.shelltools import system

import os.path

WorkDir = "docbook-xsl-1.77.1"
	
def install():
	docBookRoot = "/usr/share/xml/docbook/xsl-stylesheets-1.77.1"
	pisitools.dodir (docBookRoot)
	
	file_list = "VERSION common eclipse epub extensions fo highlighting html \
htmlhelp images javahelp lib manpages params profiling \
roundtrip slides template tests tools webhelp website \
xhtml xhtml-1_1"

	for copy in file_list.split (" "):
		copy_full = os.path.join (get.workDIR(), "%s/%s" % (WorkDir,copy))
		pisitools.insinto (docBookRoot, copy_full)
	
	# Create the .xsl symlink
	pisitools.dosym ("/usr/share/xml/docbook/xsl-stylesheets-1.77.1/VERSION", "/usr/share/xml/docbook/xsl-stylesheets-1.77.1/VERSION.xsl")

	# Whack the docs in
	pisitools.insinto ("/usr/share/doc", "doc/", "docbook-xsl-1.77.1")
