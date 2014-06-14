
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.autoreconf ("-fi")
    shelltools.export ("CFLAGS", "-O2")
    shelltools.export ("CXXFLAGS", "-O2")

    #disabled r300,r600,radeonsi
    autotools.configure ("--prefix=/usr                  \
                          --sysconfdir=/etc              \
                          --enable-texture-float         \
                          --enable-gles1                 \
                          --enable-gles2                 \
                          --enable-openvg                \
                          --enable-osmesa                \
                          --enable-xa                    \
                          --enable-gbm                   \
                          --enable-gallium-egl           \
                          --enable-gallium-gbm           \
                          --enable-glx-tls               \
                          --with-llvm-shared-libs        \
                          --enable-shared-glapi \
                          --with-egl-platforms=\"drm,x11,wayland\" \
                          --with-gallium-drivers=\"nouveau,svga,swrast\" ")

def build():
    autotools.make ()

    # Build the demos too
    autotools.make ("-C xdemos DEMOS_PREFIX=/usr")

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

    autotools.rawInstall ("-C xdemos DEMOS_PREFIX=/usr DESTDIR=%s" % get.installDIR())

    # Add docs at some stage
