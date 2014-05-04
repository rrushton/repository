#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s MANDIR=%s" %(get.installDIR(), get.manDIR()))

    pisitools.dodir("/etc/logrotate.d")

    pisitools.dobin("examples/logrotate.cron", "/etc/cron.daily")
    pisitools.insinto("/etc", "examples/logrotate-default", "logrotate.conf")

    pisitools.dodoc("CHANGES", "COPYING")
