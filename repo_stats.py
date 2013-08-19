#!/usr/bin/env python

import os
import sys
import os.path

try:
	import piksemel
except:
	print "Piksemel not available on this system. Aborting"
	sys.exit (1)
	
class Indexer:
	
	def __init__(self, workDir):
		self.workDir = workDir
		self.source_files = list()
		
	def index (self):
		for root, dirs, files in os.walk (self.workDir):
			if ".git" in dirs:
				dirs.remove (".git") # Don't visit .git
			
			for possible in files:
				if possible == "pspec.xml":
					fPath = os.path.join (root, possible)
					self.source_files.append (fPath)

class PspecParser:
	''' Parse pspec's '''
	def __init__(self, fPath):
		self.fPath = fPath
		doc = piksemel.parse(fPath)
		pkg = doc.getTag("Package")
		self.package_count = 0
		while (pkg):
			self.package_count += 1
			pkg = pkg.nextTag ("Package")
					
if __name__ == "__main__":
	i = Indexer (".")
	i.index ()

	# How many source files ?
	count = len(i.source_files)
	print "Encountered %d source files" % count

	pkg_count = 0
	for pspec in i.source_files:
		parsed = PspecParser (pspec)
		pkg_count += parsed.package_count
	print "%d possible binary packages from current repository" % pkg_count
	
