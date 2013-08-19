#!/usr/bin/env python
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
	# Must run depmod to keep the modules up to date :)
	os.system ("/sbin/depmod")
	
