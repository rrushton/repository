#!/usr/bin/python

import os, re

OUR_ID = 1002
OUR_NAME = "sudo"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
    except:
        pass

def postRemove():
    try:
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass
