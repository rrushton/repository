
#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure("--sysconfdir=/etc/mutt \
                                             --enable-pop \
                                             --enable-imap \
                                             --enable-smtp \
                                             --enable-gpgme \
                                             --enable-locales-fix \
                                             --enable-hcache \
                                             --with-curses \
                                             --with-regex \
                                             --with-ssl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
