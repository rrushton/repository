#!/usr/bin/python

import os
import os.path

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
	os.system("/usr/sbin/groupadd cron")
	os.system("/bin/chgrp cron /usr/bin/crontab")
	os.system("/bin/chmod 4750 /usr/bin/crontab")

	crontabs = "/var/spool/cron/crontabs"
	for user in os.listdir(crontabs):
		os.system("/bin/chown %s:cron %s" % (user, os.path.join(crontabs, user)))
		os.system("/bin/chmod 0600 %s" % os.path.join(crontabs, user))
