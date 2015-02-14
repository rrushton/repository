#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

BuildDir = "%s/%s" % ( get.workDIR(), "gcc-build")
GccDir = "../gcc-%s" % get.srcVERSION()

IgnoreAutodep = True

def setup():
    shelltools.makedirs (BuildDir)

    shelltools.cd (BuildDir)

    # Configure GCC
    shelltools.system ("%s/configure \
                        --prefix=/usr \
                        --with-pkgversion='Evolve OS' \
                        --libdir=/usr/lib \
                        --libexecdir=/usr/lib \
                        --with-system-zlib \
                        --enable-shared \
                        --enable-threads=posix \
                        --enable-__cxa_atexit \
                        --enable-plugin \
                        --enable-gold \
                        --enable-ld=default \
                        --with-plugin-ld=ld.gold \
                        --enable-clocale=gnu \
                        --disable-multilib \
                        --enable-lto \
                        --with-bugurl='http://bugs.evolve-os.com' \
                        --with-arch_32=i686 \
                        --enable-linker-build-id  \
                        --build=%s \
                        --target=%s \
                        --enable-languages=c,c++,fortran" % (GccDir, get.HOST(), get.HOST()) )

    # Print the summary
    shelltools.system ("%s/contrib/test_summary" % GccDir)

def build():
    shelltools.cd (BuildDir)
    autotools.make ()

def install():
    shelltools.cd (BuildDir)

    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
    # Linky linky
    pisitools.dosym ("/usr/bin/cpp", "/lib/cpp")
    pisitools.dosym ("/usr/bin/gcc", "/usr/bin/cc")
