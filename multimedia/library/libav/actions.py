
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    # Need to enable some other options when we can.
    options = "--prefix=/usr \
                       --disable-static \
                       --enable-shared \
                       --enable-libtheora \
                       --enable-libvorbis \
                       --enable-libspeex \
                       --enable-zlib"
    autotools.rawConfigure (options)

def build():
    autotools.make ()

def install():
    autotools.install ()

    pisitools.dodoc("README", "Changelog")
