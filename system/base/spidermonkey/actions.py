
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools
import os

BuildDir = "js/src"

def setup():
    os.chdir (BuildDir)
    autotools.configure ("--prefix=/usr --enable-threadsafe --with-system-nspr")

def build():
    os.chdir (BuildDir)
    autotools.make ()

def install():
    os.chdir (BuildDir)
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    shelltools.system ("sed -i %s/usr/lib/pkgconfig/mozjs185.pc -e 's@/var/pisi/spidermonkey.*/install@@g'" % get.installDIR())
