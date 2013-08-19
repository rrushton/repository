
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

BuildDir = "%s/%s" % ( get.workDIR(), "gcc-build")
GccDir = "../gcc-4.7.2"

def get_multiarch_host ():
	if get.ARCH() == "x86_64":
		return "x86_64-linux-gnu"
	else:
		return "i386-linux-gnu"
		
def exportMultiVars ():
	# Export multiarch required variables
	shelltools.export ("CPATH", "/usr/include/%s" % get_multiarch_host())
	shelltools.export ("LIBRARY_PATH", "/usr/lib/%s" % get_multiarch_host())
	
def setup():
	exportMultiVars ()
	
	# .info's are broke to shit, don't bother building them
	shelltools.system ("sed -i 's/BUILD_INFO=info/BUILD_INFO=/' gcc/configure")
	shelltools.makedirs (BuildDir)
	
	shelltools.cd (BuildDir)
	
	# Configure GCC
	shelltools.system ("%s/configure \
						--prefix=/usr \
						--with-pkgversion='SolusOS 2'\
						--libdir=/usr/lib\
						--libexecdir=/usr/lib\
						--with-system-zlib\
						--enable-shared\
						--enable-threads=posix\
						--enable-__cxa_atexit\
						--enable-plugin\
						--enable-gold\
						--enable-ld=default\
						--with-plugin-ld=ld.gold\
						--enable-clocale=gnu\
						--enable-multiarch\
						--enable-lto\
						--with-multiarch-defaults=i386-linux-gnu\
						--with-arch-32=i686\
						--with-bugurl='http://bugs.solusos.com'\
						--build=%s\
						--host=%s\
						--target=%s\
						--enable-languages=c,c++,fortran" % (GccDir, get.HOST(), get.HOST(), get.HOST()) )
						
	# Print the summary
	shelltools.system ("%s/contrib/test_summary" % GccDir)
						  
def build():
	exportMultiVars ()
	shelltools.cd (BuildDir)
	autotools.make ()
		
def install():
	exportMultiVars ()
	shelltools.cd (BuildDir)
	
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	# Linky linky
	pisitools.dosym ("/usr/bin/cpp", "/lib/cpp")
	pisitools.dosym ("/usr/bin/gcc", "/usr/bin/cc")
