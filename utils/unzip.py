#!/usr/bin/env python
#-*- coding:utf-8 -*-


import StringIO
import zipfile

ZIP_FILE_MAGIC_CODE = "PK\x03\x04\x14\x00\x08\x08\x08\x00"

def from_file(file_name):
    return zipfile.ZipFile(f, mode='r')

def from_string(bstring):
    f = StringIO.StringIO()
    f.write(bstring)
    return zipfile.ZipFile(f, mode='r')
