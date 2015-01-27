

import sys
import logging

from lxml import etree

import ooxml
from ooxml import parse, serialize, importer

logging.basicConfig(filename='ooxml.log', level=logging.INFO)


file_name = 'test.docx'

dfile = ooxml.read_from_file(file_name)

print serialize.serialize(dfile.document)
#print serialize.serialize_styles(dfile.document)
#print serialize.serialize_(dfile.document)    
