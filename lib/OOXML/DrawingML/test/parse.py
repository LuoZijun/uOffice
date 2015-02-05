#!/usr/bin/env python
#-*- coding:utf-8 -*-



import sys,os,time
import logging

sys.path.append( "/var/www/uOffice/format/ooxml" )
from lxml import etree

import ooxml
from ooxml import parse, serialize, importer

logging.basicConfig(filename='ooxml.log', level=logging.INFO)


#file_name = 'tests/files/MS-2007.docx'
#file_name = 'tests/files/MS-2010.docx'
#file_name = 'tests/files/kingsoft.docx'
file_name = 'tests/files/paper.docx'

dfile = ooxml.read_from_file(file_name)

html = """<!DOCTYPE html>
<html lang='zh_CN'>
    <head>
        <title>呵呵</title>
        <meta charset="UTF-8">
    </head>
    <body>\n
"""
html += serialize.serialize(dfile.document)
html += "\n</body>\n</html>"
print html
#print serialize.serialize_styles(dfile.document)
#print serialize.serialize_(dfile.document)

