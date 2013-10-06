
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())


def setup():
    # TODO: Add libevdev: --enable-evdev-input
    # Need to support GNOME on Wayland in SolusOS
    autotools.configure("--disable-static \
                         --enable-x11-backend \
                         --enable-gdk-backend \
                         --enable-wayland-backend \
                         --enable-egl-backend \
                         --enable-wayland-compositor \
                         --enable-xinput \
                         --enable-gdk-pixbuf \
                         --enable-introspection")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING")
