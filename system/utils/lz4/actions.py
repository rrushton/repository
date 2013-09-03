
#!/usr/bin/python

#Created For SolusOS

from pisi.actionsapi import shelltools, get, cmaketools, pisitools

def setup():
    shelltools.cd("cmake")
    cmaketools.configure("-DBUILD_SHARED_LIBS=true")


def build():
    shelltools.cd("cmake")
    cmaketools.make()


def install():
    shelltools.cd("cmake")
    cmaketools.install()

    pisitools.dodir("/usr/bin")
    # In future check arch
    shelltools.move("%s/usr/lz4c32" % get.installDIR(), "%s/usr/bin/lz4c32" % get.installDIR())

    pisitools.dosym ("/usr/bin/lz4c32", "/usr/bin/lz4c")
    
