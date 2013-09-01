#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto ("/opt/thunderbird", "*")
