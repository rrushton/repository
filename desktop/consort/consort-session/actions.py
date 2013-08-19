
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, pisitools
	
def install():
    pisitools.insinto ("/usr/share/glib-2.0/schemas", "org.consort.desktop.gschema.xml")
    pisitools.insinto ("/usr/share/gnome-session/sessions", "consort.session")
    pisitools.insinto ("/usr/share/xsessions", "consort.desktop")
    pisitools.dobin ("consort-session")


