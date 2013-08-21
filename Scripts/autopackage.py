#!/usr/bin/env python

import os
import sys
import os.path
import dloader
import datetime
import shutil

from configobj import ConfigObj

''' Example config file
~/.solusos/packager

[Packager]
Name=Your Name Goes Here
Email=Your Email Goes Here
'''

# What we term as needed doc files
KnownDocFiles = [ "COPYING", "COPYING.LESSER", "ChangeLog", "COPYING.GPL", "AUTHORS", "BUGS", "CHANGELOG", "LICENSE"]

# Compile type to build 'actions.py'
GNOMEY = 1
AUTOTOOLS = 2
CMAKE = 3
PYTHON_MODULES = 4
PERL_MODULES = 5

class AutoPackage:
	
	def __init__(self, uri):
		self.package_uri = uri
		homeDir = os.environ ["HOME"]
		config = ".solusos/packager"
		self.config_dir = os.path.join (homeDir, config)
		if not os.path.exists (self.config_dir):
			print "Config file not found at %s" % self.config_dir
			sys.exit (-1)
		
		# See the above commentary for details on the file format	
		self.config = ConfigObj (self.config_dir)
		self.email = self.config["Packager"]["Email"]
		self.packager_name = self.config["Packager"]["Name"]
		
		# Templates
		us = os.path.dirname(os.path.abspath(__file__))
		base_dir = "/".join (us.split ("/")[:-1])
		self.template_dir = os.path.join (base_dir, "Templates")
		
		self.doc_files = list()
		
	def verify (self):
		print "Verifying %s" % self.package_uri
		self.file_name = self.package_uri.split ("/")[-1]
		self.file_name_full = os.path.abspath (self.file_name)
		print self.file_name
		try:
			dloader.download_file (self.package_uri)
			self.sha1sum = dloader.get_sha1sum (self.file_name)
		except Exception, e:
			print e
			return False
		return True
	
	def examine_source (self):
		splits = self.file_name.split (".")
		suffix = "".join(splits [-2:]).replace ("bzip2", "bz2")
		# Find out pspec file type
		if suffix.endswith ("zip"):
			suffix = "zip"
		self.file_type = suffix
		
		# Work out the version number
		path,ext = os.path.splitext (self.file_name)
		version = path.split ("-")[-1].split(".")[:-1]
		version_string = ".".join(version)
		self.version_string = version_string
		
		# Package name, including hyphens
		self.package_name = "-".join(path.split("-")[:-1])
		self.compile_type = None

		print "Package: %s\nVersion: %s" % (self.package_name, self.version_string)
		print "SHA1 Sum: %s" % self.sha1sum
		
		# Set up temporary
		self.temp_dir = os.path.abspath ("./TEMP")
		os.mkdir (self.temp_dir)
		self.current_dir = os.getcwd ()
		
		# Extract this shit
		os.chdir (self.temp_dir)
		os.system ("tar xf \"%s\"" % self.file_name_full)
		
		# Check for certain files..
		for root,dirs,files in os.walk (os.getcwd ()):
			depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
			if depth == 3:
				# We're currently two directories in, so all subdirs have depth 3
				dirs[:] = [] # Don't recurse any deeper
			for file in files:
				if file in KnownDocFiles:
					# Append files for pisitools.dodoc ()
					if not file in self.doc_files:
						self.doc_files.append (file)
						print "Added %s" % file
				if "configure" in file:
					# Check if we need to employ certain hacks needed in gnome packages
					fPath = os.path.join (root, file)
					print "Checking %s for use of g-ir-scanner" % fPath
					
					if self.check_is_gnomey (fPath):
						self.compile_type = GNOMEY
					else:
						self.compile_type = AUTOTOOLS
				if "CMakeLists.txt" in file:
					# This will use the actions with cmake
					print "CMake files founded."
					self.compile_type = CMAKE
				if "setup.py" in file:
					# this is a python module.
					self.compile_type = PYTHON_MODULES
				if "Makefile.PL" in file:
					# This is a perl module
					self.compile_type = PERL_MODULES

		if self.compile_type == GNOMEY:
			print "This package utilises g-ir-scanner, a specific actions.py will be used"
						
		# Clean up on aisle 3
		os.chdir (self.current_dir)
		shutil.rmtree (self.temp_dir)

		# Always delete
		if os.path.exists (self.file_name):
			os.remove (self.file_name)
					
	def create_pspec (self):
		''' Now the interesting stuff happens. We'll create a pspec.xml automagically :) '''
		sample_pspec = os.path.join (self.template_dir, "pspec.sample.xml")
		
		date = datetime.datetime.now().strftime ("%m-%d-%Y")
		with open (sample_pspec, "r") as sample:
			mapping =  { 'PackagerName' : self.packager_name, \
						 'PackagerEmail' : self.email, \
						 'PackageName' : self.package_name, \
						 'Summary': 'Add summary', \
						 'Description': 'Add description', \
						 'License': 'GPLv2+', \
						 'HashSum': self.sha1sum, \
						 'ArchiveType': self.file_type, \
						 'ArchiveURI': self.package_uri, \
						 'Date': date, \
						 'Version': self.version_string }
			lines = sample.read () % mapping
			
			with open ("pspec.xml", "w") as pspec:
				pspec.write (lines)
				pspec.flush ()
	
	def create_actions (self):
		''' Create actions.py '''
		if self.compile_type == GNOMEY:
			sample_actions = os.path.join (self.template_dir, "actions.gnome.sample.py")
		elif self.compile_type == AUTOTOOLS:
			sample_actions = os.path.join (self.template_dir, "actions.sample.py")
		elif self.compile_type == CMAKE:
			sample_actions = os.path.join (self.template_dir, "actions.cmake.sample.py")
		elif self.compile_type == PYTHON_MODULES:
			sample_actions = os.path.join (self.template_dir, "actions.pythonmodules.sample.py")
		elif self.compile_type == PERL_MODULES:
			sample_actions = os.path.join (self.template_dir, "actions.perlmodules.sample.py")
		doc_str = ""
		if len(self.doc_files) > 0:
			doc_str = "pisitools.dodoc("
			for doc in self.doc_files:
				if doc == self.doc_files[-1]:
					doc_str += "\"%s\"" % doc
				else:
					doc_str += "\"%s\", " % doc
				
			doc_str += ")"
		print doc_str	
		with open (sample_actions, "r") as sample:
			lines = sample.read ().replace ("#EXTRADOCS#", doc_str)
			
			# Write out the actions.py
			with open ("actions.py", "w") as actions:
				actions.write (lines)
				actions.flush ()
				
	def check_is_gnomey (self, path):
		with open (path, "r") as makefile:
			lines = makefile.read ()
			if "g-ir-scanner" in lines or "g_ir_scanner" in lines:
				return True
		return False
				
if __name__ == "__main__":
	if len (sys.argv) < 2:
		print "%s: <URI>" % sys.argv[0]
		sys.exit (-1)
		
	p  = AutoPackage (sys.argv[1])
	if not p.verify ():
		print "Unable to locate given URI"
	else:
		print "Completed verification"
		p.examine_source ()
		p.create_pspec ()
		p.create_actions ()
