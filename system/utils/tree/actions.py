#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools,get

def build():
    autotools.make()

def install():
    autotools.install()
