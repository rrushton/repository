#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  release.py - Handle releases
#  
#  Copyright 2013 Ikey Doherty <ikey@solusos>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import subprocess
import time
from datetime import date
import sys

MAJOR = "2"

release_who = "Ikey Doherty"
release_mail = "ikey@solusos.com"
should_filter = False


class CommitInfo:

    def __init__(self, line):
        splits = line.split("\t")
        self.commit_id = splits[0]
        self.date = splits[1]
        self.author = splits[2]
        self.author_email = splits[3]
        self.commit_msg = "\t".join(splits[4:])

class ReleaseVersion:

    def __init__(self):
        today = date.fromtimestamp(time.time())
        iso = today.isocalendar()

        self.major = MAJOR
        self.iso_year = iso[0]
        self.iso_week = iso[1]
        self.iso_day = iso[2]
        self.patch_level = "0"

        self.build_id = 0
        
    def __str__(self):
        s = "%s.%s%s.%s.%s" % (self.major,
                               self.iso_year,
                               self.iso_week,
                               self.iso_day,
                               str(self.build_id))


        return s
        
def _get_last_tag():
    cmd = subprocess.Popen("git describe --abbrev=0 --tags".split(), stdout=subprocess.PIPE)
    pipe = cmd.communicate()
    tag = pipe[0].strip()
    return tag


def _changes_since_tag(tag):
    format = '--pretty=format:%h%x09%ad%x09%an%x09%ae%x09%s'
    cmd = ["git", "log", format, "--date=short", "%s..HEAD" % tag]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    lines = proc.communicate()[0].split("\n")

    if lines[0] == "":
        return None
    
    changes = list()
    for line in lines:
        commit = CommitInfo(line)
        cmsg = commit.commit_msg
        if should_filter:
            if "[UPDATE]" in cmsg or "[NEW]" in cmsg or "[FIX]" in cmsg or "[REMOVE]" in cmsg:
                changes.append(commit)
        else:
            changes.append(commit)

    return changes
    
def main():
    tag = _get_last_tag() if len(sys.argv) < 2 else sys.argv[1]
    changes = _changes_since_tag(tag)

    tag = tag.split("-")[0]
    if changes is None:
        print "No changes have been commited since %s" % tag
        return 0

    print "%d changes since %s" % (len(changes), tag)
    print "\n\n"
    version = ReleaseVersion()
    version_h = str(version)
    new_packages = 0
    updated_packages = 0
    fixed_packages = 0
    
    for commit in changes:
        if "[UPDATE]" in commit.commit_msg:
            updated_packages += 1
        elif "[NEW]" in commit.commit_msg:
            new_packages += 1
        elif "[FIX]" in commit.commit_msg:
            fixed_packages += 1

    # Find out if we already have a build vers
    if "-" in tag:
        version.build_id = int(tag.split(".")[-1])
    old = ".".join(tag.split(".")[:3])
    new = ".".join(version_h.split(".")[:3])

    if old == new:
        # Already had a release today, bump build id
        version.build_id += 1

    # Now format all commits
    print "Release %s - %s <%s>\n" % (version, release_who, release_mail)
    for c in changes:
        print " * %s\n  - %s (%s)\n" % (c.commit_msg, c.author, c.author_email)
    
if __name__ == '__main__':
    main()

