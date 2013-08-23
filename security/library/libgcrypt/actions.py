#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools, get, pisitools


def setup():
    pisitools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")
    pisitools.system("./autogen.sh")
    autotools.automake("--add-missing")
    autotools.configure("--with-gpg-error-prefix=/usr")


def build():
    autotools.automake()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README",
                    "THANKS", "TODO", "VERSION")
