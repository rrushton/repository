#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure ("--prefix=/usr --libexecdir=/usr/lib")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    # Bash completion
    pisitools.insinto("/usr/share/bash-completion/completions",
                      "contrib/completion/git-completion.bash",
                      "git")

    pisitools.dodoc ("README", "COPYING")
