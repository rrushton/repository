Preparing the first revision of GCC 4.7.2
-----------------------------------------

SolusOS GCC/Toolchain Maintainer: Ikey Doherty <ikey@solusos.com>

## First run
Firstly I'll just get GCC built with the minimal options, with just C, C++
and fortran compilers

## Second run
Add UnZip to the repositories to support the building of the GCJ Java Compilers
Rebuild with ppl (0.11)

## Third run
Add the GNAT 2011 dist to the tree via extra <Archive>, and allow building of ada.

## Fourth run
Allow all languages (c,c++,fortran,ada,go,java,objc,obj-c++), define paths and split
various subpackages (language-specific compilers, libstdc++, libgcc, etc)

## Last run
Patch all parts of the toolchain to support multiarch (/usr/lib/<host_triplet>/)

