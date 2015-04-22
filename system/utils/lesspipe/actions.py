
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.rawConfigure("--prefix=/usr \
                                                    --default")

def build():
    autotools.make()

def install():
    pisitools.dobin("code2color")
    pisitools.dobin("sxw2txt")
    pisitools.dobin("tarcolor")
    pisitools.dobin("lesspipe.sh")
    pisitools.doman("lesspipe.1")
