#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys,time
# add import path.
#sys.path.append( os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib') )

from .utils import unzip

#def detect_format(file_header):
#    magic.from_buffer(file_header[0:1024], mime=True)

def read_from_file(file_name):
    return unzip.from_file(file_name)
    
def read_from_unzipstring(file_content):
    return unzip.from_string(file_content)

def parse():
    pass



