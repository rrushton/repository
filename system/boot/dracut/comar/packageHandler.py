#!/usr/bin/python

import piksemel
import os
import os.path


def updateInitrd(filepath):
    parse = piksemel.parse(filepath)
    for xmlfile in parse.tags("File"):
        path = xmlfile.getTagData("Path")
        if "/boot/kernel-" in path or "/boot/vmlinuz-" in path:
            version = path.split("-")[1]
            cmd = "dracut -f --kver %s" % version
            os.system(cmd)

            # Determine whether to actually update grub or not.
            if os.path.exists("/proc/cmdline"):
                os.system("/usr/sbin/update-grub")
            break


def setupPackage(metapath, filepath):
    updateInitrd(filepath)


def postCleanupPackage(metapath, filepath):
    updateInitrd(filepath)
