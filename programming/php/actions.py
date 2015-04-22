#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure("--with-config-file-path=/etc \
                         --with-zlib                  \
                         --with-curl                  \
                         --enable-bcmath              \
                         --with-bz2                   \
                         --enable-calendar            \
                         --disable-dba                \
                         --with-gmp                   \
                         --enable-ftp                 \
                         --with-gettext               \
                         --enable-mbstring            \
                         --with-readline")


def build():
    autotools.make()


def install():
    shelltools.export("INSTALL_ROOT", get.installDIR())
    autotools.install()

    # Now move it all.. absurd build because only parts of php
    # respect INSTALL_ROOT ..
    pisitools.domove("%s/usr/*" % get.installDIR(), "/usr")
    pisitools.domove("/usr/lib/lib/*", "/usr/lib/.")
    pisitools.domove("/usr/lib/php/php/*", "/usr/lib/php/.")
    pisitools.removeDir("/usr/lib/php/php")
    pisitools.removeDir("/usr/lib/lib")
    pisitools.removeDir("/var")
    pisitools.remove("/.*")
    pisitools.removeDir("/.registry")
    pisitools.removeDir("/.channels")
    pisitools.remove("/usr/lib/php/.*")
    pisitools.removeDir("/usr/lib/php/.channels")
    pisitools.removeDir("/usr/lib/php/.registry")
    pisitools.dodoc("LICENSE", "CREDITS")
    pisitools.dosym("/usr/bin/php", "/usr/bin/php5")
