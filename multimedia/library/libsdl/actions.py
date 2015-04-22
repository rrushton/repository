
#!/usr/bin/python


from pisi.actionsapi import get, autotools, pisitools, libtools


def setup():
    autotools.configure ("--enable-events \
                                              --enable-cpuinfo \
                                              --enable-timers \
                                              --enable-threads \
                                              --enable-alsa \
                                              --enable-cdrom \
                                              --enable-file \
                                              --enable-oss \
                                              --enable-nasm \
                                              --enable-video-aalib \
                                              --enable-video-opengl \
                                              --enable-video-dummy \
                                              --enable-video-x11 \
                                              --enable-video-x11-xv \
                                              --enable-video-x11-xinerama \
                                              --enable-video-x11-xrandr \
                                              --with-x \
                                              --disable-rpath \
                                              --disable-static")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
    libtools.preplib()

    pisitools.dodoc ("COPYING", "BUGS","README-SDL.txt")
