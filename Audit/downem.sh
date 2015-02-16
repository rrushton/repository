#!/bin/bash

wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2002.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2003.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2004.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2005.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2006.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2007.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2008.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2009.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2010.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2011.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2012.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2013.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2014.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2015.xml.gz
wget http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Modified.xml.gz

for i in *.xml.gz ; do gunzip $i ; done
