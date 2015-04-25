#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys,os,time
from lxml import etree
import xmllib

import convert
import parse


class Docx(object):
    def __init__(self, workspace):
        # zipfile object
        self.workspace = workspace
    def parse(self):
        print self
        print dir(self)
        print self.workspace
    def convert(self):
        pass







"""
class Work:
    def __init__(self, fname):
        fo = FileObject(fname=fname)
        self.fname = fname
        self.workspace = fo.workspace
    def test(self):
        print self.workspace.keys()
    def testxml(self):
        return OpenXML(self.fname)

class OpenXML:
    document = None
    Gtag = []
    def __init__(self, fname, Gtag=[]):
        #f = StringIO.StringIO()
        #f.write(xml)
        self.document = etree.parse(fname)
        self.Gtag = Gtag
    def doms(self):
        # Show XML DOM Nodes ( Object )
        print repr(self.document)
        root = self.document.getroot()
        for dom in self.document.getiterator():
            DOMS.append(dom)
        return DOMS
    def fetch(self):
        pass
"""