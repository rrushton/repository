#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    with open("/etc/group") as groupfile:
        if not "mlocate" in groupfile:
            os.system("/usr/sbin/groupadd -g 17 mlocate")

    os.system("/usr/bin/updatedb -v")
