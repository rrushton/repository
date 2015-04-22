
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.insinto("/usr/share/aspell-0.60", "bokmål.alias")
    pisitools.dodoc ("COPYING", "Copyright", "README")
