
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def install():
    pisitools.dodir ("/usr/share/themes/Bluebird")

    for subtheme in ["gtk-2.0", "gtk-3.0", "metacity-1", "xfwm4"]:
        pisitools.insinto ("/usr/share/themes/Bluebird", subtheme)

    pisitools.dodoc ("LICENSE.CC", "LICENSE.GPL")
