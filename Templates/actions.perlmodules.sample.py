#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import perlmodules, pisitools


def setup():
    perlmodules.configure()


def build():
    perlmodules.make()


def install():
    perlmodules.install()

    #EXTRADOCS#
