#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools

def install():
    files = ["basket.py", "groups.py", "updates.py", "style.css",
             "components.py", "interface.py", "package_view.py", "widgets.py"]

    for f in files:
        pisitools.insinto("/usr/lib/evolve-sc", f)
    pisitools.dobin("main.py")
    pisitools.domove("/usr/bin/main.py", "/usr/bin", destinationFile="evolve-sc")
    pisitools.insinto("/usr/share/applications", "data/evolve-sc.desktop")
