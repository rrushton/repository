#!/usr/bin/python

from pisi.actionsapi import autotools


def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
