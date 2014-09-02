#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, cmaketools


def setup():
    cmaketools.configure()


def build():
    cmaketools.make()


def install():
    cmaketools.install()

    
