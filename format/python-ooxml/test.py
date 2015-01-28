

import sys
import logging

from lxml import etree

import ooxml
from ooxml import parse, serialize, importer

logging.basicConfig(filename='ooxml.log', level=logging.INFO)


file_name = 'b2.docx'

dfile = ooxml.read_from_file(file_name)

html = """<!DOCTYPE html>
<html lang='zh_CN'>
    <head>
        <title>hehe</title>
        <meta charset="UTF-8">
    </head>
    <body>\n
"""
html += serialize.serialize(dfile.document)
html += "\n</body>\n</html>"
print html
#print serialize.serialize_styles(dfile.document)
#print serialize.serialize_(dfile.document)    
