#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys,time
from struct import pack,unpack


class Wmf:
    def __init__(self):
        pass
    def decode(self, data):
        # Decode Windows Metafile 
        #header = data[0:18]
        print "======================"
        print "Raw: %s" % repr(data[0:18])
        header = unpack("HHHHHHIH", data[0:18])
        print "Type: %d\tHeaderSize: %d\tVersion: %d\tSizeLow: %d\tSizeHigh: %d\tNumberOfObjects: %d\tMaxRecord: %d\t" %( header[0],header[1],header[2],header[3],header[4],header[5],header[6])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        Wmf().decode(open(sys.argv[1], 'r').read())
    else:
        print ":: 没有指定任何 WMF 文件."

