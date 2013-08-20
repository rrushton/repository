
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
	shelltools.export ("CFLAGS", "-g -O2 -DSQLITE_ENABLE_FTS3=1 \
            -DSQLITE_ENABLE_COLUMN_METADATA=1     \
            -DSQLITE_ENABLE_UNLOCK_NOTIFY=1       \
            -DSQLITE_SECURE_DELETE=1")

	autotools.rawConfigure ("--prefix=/usr --disable-static")
						
def build():
	autotools.make ()
	
def install():
	autotools.install ()
	pisitools.dodir ("/usr/share/doc/sqlite3")
	pisitools.insinto ("/usr/share/doc/sqlite3", "docs/sqlite-doc-3071601/*")
