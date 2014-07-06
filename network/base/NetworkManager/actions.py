
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    shelltools.export("HOME", get.workDIR())
    autotools.configure("--libexecdir=/usr/lib/NetworkManager\
                         --sysconfdir=/etc\
                         --localstatedir=/var\
                         --with-systemdsystemunitdir=/usr/lib/systemd/system\
                         --with-session-tracking=systemd\
                         --enable-shared\
                         --disable-static\
                         --disable-ppp")
    ## Its erroring out with new glib
    shelltools.system("find . -name \"Makefile\" | xargs sed -i \"s@ -Werror@@g\"")

def build():
    shelltools.export("HOME", get.workDIR())
    autotools.make()

def install():
    shelltools.export("HOME", get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Enable systemd stuff
    pisitools.dosym("/usr/lib/systemd/system/NetworkManager.service", "/usr/lib/systemd/system/dbus-org.freedesktop.NetworkManager.service")
