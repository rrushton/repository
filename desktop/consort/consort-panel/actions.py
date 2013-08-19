
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export ("HOME", get.workDIR())

def setup():
    autotools.configure ("--disable-static \
                          --disable-scrollkeeper \
                          --enable-introspection=yes \
                          --disable-documentation \
                          --enable-telepathy-glib \
                          --enable-network-manager \
                          --disable-gtk-doc \
                          --libexecdir=/usr/lib/consort-panel")
						  
def build():
	autotools.make ()
	
def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    pisitools.domove ("/usr/bin/panel-test-applets", "/usr/bin", "consort-panel-test-applets")
    pisitools.domove ("/usr/bin/gnome-desktop-item-edit", "/usr/bin", "consort-desktop-item-edit")
    pisitools.dodoc ("AUTHORS", "ChangeLog", "COPYING")



