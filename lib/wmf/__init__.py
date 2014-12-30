#!/usr/bin/env python
#-*- coding:utf-8 -*-

#__doc__       = "Document"
#__version__   = "0.0000001"

import os,sys,time
from struct import pack,unpack
from termcolor import colored
"""
Python Data Format(pack/unpack):

    b   8 bit signed integer
    B   8 bit unsigned integer
    h   16 bit signed integer
    H   16 bit unsigned integer
    l   32 bit signed integer
    L   32 bit unsigned integer
    q   64 bit signed integer
    Q   64 bit unsigned integer
    f   32 bit floating point number
    d   64 bit floating point number
"""


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
        pass



if __name__ == '__main__':
    # Test
    pass
    if len(sys.argv) > 1:
        del sys.argv[0]
        for metafile in sys.argv:
            print colored("\t@@ Windows Metafile: ", 'red') + colored(metafile, 'green')
            Wmf().decode(open(metafile, 'r').read())
    else:
        print ":: 没有指定任何 WMF 文件."