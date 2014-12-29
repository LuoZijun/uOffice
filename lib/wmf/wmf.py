#!/usr/bin/env python
#-*- coding:utf-8 -*-

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
    data = None
    def __init__(self, data=''):
        pass
    def decode(self, data):
        # Decode Windows Metafile 
        #header = data[0:18]
        print "Raw: %s" % repr(data[0:18])
        header = unpack("HHHHHHIH", data[0:18])
        print "Type: %d\tHeaderSize: %d\tVersion: %d\tSizeLow: %d\tSizeHigh: %d\tNumberOfObjects: %d\tMaxRecord: %d\tNumberOfMembers: %d"\
        %( header[0],header[1],header[2],header[3],header[4],header[5],header[6], header[7])
        #self.decode_body(data)
    def PLACEABLE_Record(self,data):
        # Placeable record before WMF Header Record.
        # 22 bytes
        # Key: 4bytes HWmf: 2bytes  BoundingBox: 8bytes Inch: 2bytes Reserved: 4bytes Checksum: 2bytes
        print "Raw: %s" % repr(data[0:18])
        header = unpack("IHQHIH", data[0:22])
        print header

if __name__ == '__main__':
    if len(sys.argv) > 1:
        del sys.argv[0]
        for metafile in sys.argv:
            print colored("\t@@ Windows Metafile: ", 'red') + colored(metafile, 'green')
            Wmf().decode(open(metafile, 'r').read())
    else:
        print ":: 没有指定任何 WMF 文件."

