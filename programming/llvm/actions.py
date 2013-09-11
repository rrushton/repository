#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	# Move the clang stuff to be usable
	shelltools.move ("tools/cfe-3.3.src", "tools/clang")
	shelltools.move ("projects/compiler-rt-3.3.src", "projects/compiler-rt")
	
		
	shelltools.export ("CC", "gcc")
	shelltools.export ("CXX", "g++")
	autotools.rawConfigure ("--prefix=/usr              \
						  --sysconfdir=/etc          \
						  --libdir=/usr/lib/llvm     \
						  --enable-libffi            \
						  --enable-optimized         \
						  --enable-shared            \
						  --disable-assertions       \
						  --disable-debug-runtime    \
						  --disable-expensive-checks \
						  --enable-experimental-targets=R600")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
