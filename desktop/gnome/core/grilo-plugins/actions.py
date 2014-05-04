#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    # TODO: Totem for --enable-optical-media, --enable-youtube,
    #                 --enable-vimeo
    #       gssdp for --enable-upnp
    #       gmime for --enable-podcasts
    autotools.configure("--enable-goa \
                         --enable-filesystem \
                         --enable-jamendo \
                         --enable-lastm-albumart \
                         --enable-flickr \
                         --enable-bookmarks \
                         --enable-shoutcast \
                         --enable-apple-trailers \
                         --enable-magnatune \
                         --enable-gravatar \
                         --enable-tracker")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
