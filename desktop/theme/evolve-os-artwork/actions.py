#!/usr/bin/python

from pisi.actionsapi import autotools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
