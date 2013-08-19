
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    '''
    Notes: Pidgin will require GStreamer 0.10 series,
    Also a GTK2 gtkspell
    '''
    autotools.configure("--disable-vv \
                         --disable-idn \
                         --disable-meanwhile \
                         --disable-gtkspell \
                         --disable-gstreamer \
                         --disable-schemas-install \
                         --disable-avahi")
						  
def build():
    autotools.make()
	
def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/lib/perl5")
