#!/bin/bash
#
# evobuild - Highly delicate build tool
# 
# Copyright 2014 Ikey Doherty <ikey.doherty@gmail.com>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#/

TARGET="/var/evobuild/base.tgz"
REPO="http://packages.evolve-os.com/eopkg-index.xml.xz"
BUILDDIR="/var/evobuild/build"
GTDIR="$BUILDDIR"

# We cache packages and archives
PKGDIR="/var/evobuild/packages"
ARCHIVEDIR="/var/evobuild/archives"
CCACHEDIR="/var/evobuild/ccache"

if [[ $UID -ne 0 ]]; then
    echo "You must be root to run evobuild"
    exit 1
fi

# Typical die function
function do_die() {
    echo "ERROR: $1"
    do_clean
    exit 1
}

# Can't be too careful
function do_clean()
{
    PID=`cat $GTDIR/var/run/dbus/pid 2>/dev/null`
    if [[ $? -ne 0 ]]; then
        exit 0
    fi
    kill $PID
    sleep 1
    kill -9 $PID 2>/dev/null
    rm $GTDIR/var/run/dbus/pid

    if [[ `grep $PKGDIR /etc/mtab` ]]; then
        umount $GTDIR/$PKGDIR 2>/dev/null
    fi
    if [[ `grep $ARCHIVEDIR /etc/mtab` ]]; then
        umount $GTDIR/$ARCHIVEDIR 2>/dev/null
    fi
}

# trap keyboard interrupt (control-c)
trap do_clean SIGINT

# Initialize an Evolve OS chroot
function do_chroot_init() {
    if [[ ! -d "/var/evobuild" ]]; then
        mkdir /var/evobuild
    fi

    TDIR="./BUILDROOT"
    # Set up normal links before we go ahead and throw pisi in
    mkdir -p $TDIR/run/lock
    mkdir -p $TDIR/var
    ln -s ../run/lock $TDIR/var/log
    ln -s ../run $TDIR/var/run
    GTDIR="$TDIR"
    PIT="pisi it --ignore-comar -D $TDIR/ -y"

    if [[ ! -d "$TDIR/var/cache/eopkg/packages" ]]; then
        mkdir -p "$TDIR/var/cache/eopkg/packages"
    fi
    if [[ ! -d "$TDIR/var/cache/eopkg/archives" ]]; then
        mkdir -p "$TDIR/var/cache/eopkg/archives"
    fi

    # Mount host package directory to save on bandwidth if it exists
    if [[ ! -d "$PKGDIR" ]]; then
        mkdir "$PKGDIR"
    fi
    mount --bind "$PKGDIR" $TDIR/var/cache/eopkg/packages || do_die "Unable to bind mount $PKGDIR"

    # Add repo first
    pisi add-repo "Evolve OS" "$REPO" -D $TDIR
    # Install pisi stuffs
    $PIT --ignore-safety baselayout

    # Some basic requirements to skip dependency borks
    $PIT --ignore-safety python libgcrypt libgpg-error python3

    # Shove in base and devel (safety catches)
    $PIT -c system.devel

    # Also need ccache present (note this is not yet currently implemented!)
    $PIT ccache

    umount $TDIR/var/cache/eopkg/packages

    # Copy base layout files in for accounts
    cp -v $TDIR/usr/share/baselayout/* $TDIR/etc/.

    # Now configure it..
    chroot $TDIR groupadd -g 18 messagebus || do_die "Unable to add dbus group"
    chroot $TDIR useradd -m -d /var/run/dbus -r -s /bin/false -u 18 -g 18 messagebus -c "D-Bus Message Daemon" || do_die "Unable to add dbus user"

    chroot $TDIR dbus-uuidgen --ensure
    chroot $TDIR dbus-daemon --system

    # Saves us from ugly ass bind-mounts
    chroot $TDIR mknod -m 444 /dev/random c 1 8
    chroot $TDIR mknod -m 444 /dev/urandom c 1 9
    chroot $TDIR chmod o+x /usr/lib/dbus-1.0/dbus-daemon-launch-helper
    chroot $TDIR pisi configure-pending
    # Cleanup cache
    chroot $TDIR pisi delete-cache

    # Kill dbus
    PID=`cat $TDIR/var/run/dbus/pid`
    kill $PID
    sleep 1
    kill -9 $PID 2>/dev/null
    rm $TDIR/var/run/dbus/pid

    # Convert into base.tgz :)
    time tar -pczf $TARGET  $TDIR/ || do_die "Unable to compress build root"
    rm -rf "$TDIR"
}

function do_build()
{
    OLDDIR=`pwd`
    PSPECFILE="$2"
    if [[ ! -f "$PSPECFILE" ]]; then
        do_die "Unable to find $PSPECFILE"
    fi
    DIR=`dirname $PSPECFILE`
    ABSDIR=`realpath $DIR`
    RELNAME=`basename $PSPECFILE`
    if [[ "$RELNAME" != "pspec.xml" ]]; then
        do_die "$PSPECFILE doesn't look like a valid pspec.xml"
    fi

    if [[ ! -e $TARGET ]]; then
        echo "$TARGET doesn't exist. Make sure to use $0 init first"
        exit 1
    fi

    # Search for actions
    ACTIONSPY="$ABSDIR/actions.py"
    PSPEC="$ABSDIR/pspec.xml"

    if [[ ! -f "$ACTIONSPY" ]]; then
        do_die "$ACTIONSPY not found"
    fi

    # Extract
    if [[ -d "$BUILDDIR" ]]; then
        echo "Removing old build directory"
        rm -rf "$BUILDDIR" || do_die "Unable to purge old build root"
    fi

    echo "Extracting build root"
    mkdir -p "$BUILDDIR" || do_die "Unable to create build dir"

    cd "$BUILDDIR" || do_die "Unable to cd to $BUILDDIR"
    time tar xpf "$TARGET" || do_die "Unable to extract build root"

    # Now the fun begins!
    mkdir "$BUILDDIR/BUILDROOT/WORK" || do_die "Unable to create work toplevel"
    WORKDIR="$BUILDDIR/BUILDROOT/WORK/packages"
    mkdir "$WORKDIR" || do_die "Unable to create working directory"

    cp -v "$PSPEC" "$WORKDIR/."
    cp -v "$ACTIONSPY" "$WORKDIR/."

    # Check if a files or comar directory exists, these are needed!
    if [[ -d "$ABSDIR/comar" ]]; then
        cp -Rv "$ABSDIR/comar" "$WORKDIR/." || do_die "Unable to copy COMAR files"
    fi
    if [[ -d "$ABSDIR/files" ]]; then
        cp -Rv "$ABSDIR/files" "$WORKDIR/." || do_die "Unable to copy additional files"
    fi

    # Copy in the component
    if [[ -e "$ABSDIR/../component.xml" ]] ; then
        cp -v "$ABSDIR/../component.xml" "$BUILDDIR/BUILDROOT/WORK/."
    fi

    # Copy in most recent resolv.conf (so you haz internets)
    cp -v /etc/resolv.conf "$BUILDDIR/BUILDROOT/etc/resolv.conf"
    # Use host eopkg.conf to enable changing of jobs, etc.
    cp -v /etc/eopkg/eopkg.conf "$BUILDDIR/BUILDROOT/etc/eopkg/eopkg.conf"

    GTDIR="$BUILDDIR/BUILDROOT"

    chroot "$BUILDDIR/BUILDROOT" dbus-uuidgen --ensure
    chroot "$BUILDDIR/BUILDROOT" dbus-daemon --system

    # Use host archive and package dirs always
    if [[ ! -d "$PKGDIR" ]]; then
        mkdir -p "$PKGDIR" || do_die "Unable to create host package pool"
    fi
    if [[ ! -d "$ARCHIVEDIR" ]]; then
        mkdir -p "$ARCHIVEDIR" || do_die "Unable to create host archive pool"
    fi
    if [[ ! -d "$CCACHEDIR" ]]; then
        mkdir -p "$CCACHEDIR" || do_die "Unable to create host ccache pool"
    fi

    if [[ ! -d "$BUILDDIR/BUILDROOT/var/cache/eopkg/packages" ]]; then
        mkdir -p "$BUILDDIR/BUILDROOT/var/cache/eopkg/packages"
    fi
    if [[ ! -d "$BUILDDIR/BUILDROOT/var/cache/eopkg/archives" ]]; then
        mkdir -p "$BUILDDIR/BUILDROOT/var/cache/eopkg/archives"
    fi
    # pisi/eopkg have CCACHE_DIR locked to /root/.ccache
    if [[ ! -d "$BUILDDIR/BUILDROOT/root/.ccache" ]]; then
        mkdir -p "$BUILDDIR/BUILDROOT/root/.ccache"
    fi

    # Bind mount them
    mount -o bind "$PKGDIR" "$BUILDDIR/BUILDROOT/var/cache/eopkg/packages" || do_die "Unable to mount host packages pool"
    mount -o bind "$ARCHIVEDIR" "$BUILDDIR/BUILDROOT/var/cache/eopkg/archives" || do_die "Unable to mount host archives pool"
    mount -o bind "$CCACHEDIR" "$BUILDDIR/BUILDROOT/root/.ccache" || do_die "Unable to mount host ccache pool"

    # Now attempt to build it
    chroot "$BUILDDIR/BUILDROOT" pisi build -y /WORK/packages/pspec.xml -O /WORK
    if [[ $? -eq 0 ]]; then
        echo "Packages built successfully"
        mv -v $BUILDDIR/BUILDROOT/WORK/*.eopkg $OLDDIR/.
    else
        echo "Package building failed"
    fi

    umount "$BUILDDIR/BUILDROOT/var/cache/eopkg/packages"
    umount "$BUILDDIR/BUILDROOT/var/cache/eopkg/archives"
    umount "$BUILDDIR/BUILDROOT/root/.ccache"

    # Kill dbus (sigint handler will make sure this happens too)
    PID=`cat $BUILDDIR/BUILDROOT/var/run/dbus/pid`
    kill $PID
    sleep 1
    kill -9 $PID 2>/dev/null
    rm $BUILDDIR/BUILDROOT/var/run/dbus/pid
}

function do_update()
{
    if [[ ! -e $TARGET ]]; then
        do_die "$TARGET does not exist - aborting"
        exit 1
    fi
    OLDDIR=`pwd`

    TDIR="./UPDATEROOT"
    if [[ -d "$TDIR" ]]; then
        echo "$TDIR exists - aborting"
        exit 1
    fi
    mkdir "$TDIR"
    cd "$TDIR"
    time tar xpf "$TARGET" || do_die "Unable to extract original"
    cd $OLDDIR

    GTDIR="$TDIR/BUILDROOT"

    chroot "$TDIR/BUILDROOT" dbus-uuidgen --ensure
    chroot "$TDIR/BUILDROOT" dbus-daemon --system
    # Copy in most recent resolv.conf (so you haz internets)
    cp -v /etc/resolv.conf "$TDIR/BUILDROOT/etc/resolv.conf"

    if [[ ! -d "$TDIR/BUILDROOT/var/cache/eopkg/packages" ]]; then
        mkdir -p "$TDIR/BUILDROOT/var/cache/eopkg/packages"
    fi

    mount --bind "$PKGDIR" "$TDIR/BUILDROOT/var/cache/eopkg/packages" || do_die "Unable to bind mount $PKGDIR"
    chroot "$TDIR/BUILDROOT" pisi up

    umount "$TDIR/BUILDROOT/var/cache/eopkg/packages"

    # Kill dbus
    PID=`cat $TDIR/BUILDROOT/var/run/dbus/pid`
    kill $PID
    sleep 1
    kill -9 $PID 2>/dev/null
    rm $TDIR/BUILDROOT/var/run/dbus/pid

    cd $TDIR
    time tar -pczf $TARGET BUILDROOT || do_die "Unable to compress build root"
    cd "$OLDDIR"
    rm -rf "$TDIR"
}

case $1 in
    "init")
        echo "Initing..."
        do_chroot_init
        ;;
    "build")
        echo "Building..."
        do_build $*
        ;;
    "update")
        echo "Updating..."
        do_update
        ;;
    *)
        echo "Valid commands: init    build  (pspec.xml)  update"
        ;;
esac
