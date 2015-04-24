#!/usr/bin/env python
#-*- coding:utf-8 -*-

#__doc__       = "Document"
#__version__   = "0.0000001"

import os,sys,time
from struct import pack,unpack
from termcolor import colored

import wmf.Records.control


class Wmf:
    metafile = None
    header = None
    records = None
    objects = None
    def __init__(self, metafile=''):
        assert type(metafile) == type('')
        assert len(metafile) > 18
        self.metafile = metafile
    def decode(self):
        # Decode Windows Metafile
        self.header = wmf.Records.control.header(self.metafile[0:18])
        self.records = wmf.Records.Record(self.metafile[18:]).list()
        print self.header
        self.records


if __name__ == '__main__':
    # Test
    if len(sys.argv) > 100:
        del sys.argv[0]
        for metafile in sys.argv:
            print colored("\t@@ Windows Metafile: ", 'red') + colored(metafile, 'green')
            Wmf().decode(open(metafile, 'r').read())
    else:
        print ":: 没有指定任何 WMF 文件."