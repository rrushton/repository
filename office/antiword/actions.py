
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools
from os import listdir

def build():
    autotools.make()

def install():
    pisitools.dobin("antiword")

    docnames = ("COPYING", "ChangeLog", "ReadMe")
    for docs in docnames:
        pisitools.dodoc("%s/%s/Docs/%s" % (get.workDIR(), get.srcDIR(), docs))

    shelltools.makedirs("%s/usr/share/antiword" % get.installDIR())
    resourcefiles = listdir("%s/%s/Resources" % (get.workDIR(), get.srcDIR()))
    for resource in resourcefiles:
        pisitools.insinto("/usr/share/antiword",
                                          "%s/%s/Resources/%s" % (get.workDIR(), \
                                          get.srcDIR(), resource))

    pisitools.doman("%s/%s/Docs/antiword.1" % (get.workDIR(), get.srcDIR()))
