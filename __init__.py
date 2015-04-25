#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys,time
# add import path.
#sys.path.append( os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib') )

from .utils import unzip
from .format.docx import Docx as docx

def read_from_file(file_name):
    return unzip.from_file(file_name)

def read_from_unzipstring(file_content):
    return unzip.from_string(file_content)






