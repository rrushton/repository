#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import autotools, pisitools


def setup():
    autotools.configure()


def build():
    autotools.make()


def install():
    autotools.install()
    compDir = "/usr/share/bash-completion/completions/"
    compFile = "examples/bash_completion_tmux.sh"
    pisitools.insinto(compDir, compFile, "tmux")
