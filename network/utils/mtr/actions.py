
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ()
                          
def build():
    autotools.make ()
    
def install():
    autotools.install ()

    #Remove setuid and move mtr from /usr/sbin to /usr/bin
    pisitools.domove("/usr/sbin/mtr", "/usr/bin/", "mtr")
    shelltools.chmod(get.installDIR() + "/usr/bin/mtr", 0755)
    shelltools.unlinkDir(get.installDIR() + "/usr/sbin")

    pisitools.dodoc ("COPYING", "AUTHORS", "README", "SECURITY")
