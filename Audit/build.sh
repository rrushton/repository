gcc -o security-audit -O2 -ggdb3 -std=c99  -Wall `pkg-config --cflags --libs libxml-2.0` `pkg-config --cflags --libs glib-2.0` `pkg-config --cflags --libs gio-2.0` main.c 
