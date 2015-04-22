
#!/usr/bin/python


from pisi.actionsapi import get, pisitools
import glob

def install():
    #Insert our executables and global config
    pisitools.dobin("grc")
    pisitools.dobin("grcat")
    pisitools.insinto("/etc", "grc.conf")

    #Insert our syntax files
    conffiles = glob.glob('%s/%s/conf.*' % (get.workDIR(), get.srcDIR()))
    for conf in conffiles:
        pisitools.insinto("/usr/share/grc", "%s" % conf)

    pisitools.doman("grc.1", "grcat.1")
    pisitools.dodoc("COPYING", "CREDITS", "README")
