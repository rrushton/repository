
#!/usr/bin/python


from pisi.actionsapi import shelltools, pisitools

WorkDir = "."


Icons = ["Faenza",
         "Faenza-Ambiance",
         "Faenza-Dark",
         "Faenza-Darker",
         "Faenza-Darkest",
         "Faenza-Radiance"]

def build():
    for icon_theme in Icons:
        shelltools.system("tar xvf %s.tar.gz" % icon_theme)


def install():
    for icon_theme in Icons:
        pisitools.insinto ("/usr/share/icons", icon_theme)

    pisitools.dodoc("COPYING")
