#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys,os,time

#from utils import unzip

from lxml import etree
import StringIO
import zipfile
import xmllib
# XMLParser

#     @staticmethod
def unzip(data):
    "uncompress zip file "
    f = StringIO.StringIO()
    f.write(data)
    del data
    z = zipfile.ZipFile(f, mode='r')
    #z.printdir()
    #[u'docProps/app.xml', u'docProps/core.xml', u'word/numbering.xml', u'word/settings.xml', u'word/fontTable.xml', u'word/styles.xml', u'word/document.xml', u'word/_rels/document.xml.rels', u'_rels/.rels', u'word/media/image03.png', u'word/media/image01.png', u'[
    uncompress_data = {}
    for fname in z.namelist():
        uncompress_data[fname] = z.read(fname)
    return uncompress_data

class FileObject:
    def __init__(self, fname='', fdata=''):
        self.fname = fname
        if fdata != '' and fdata != None: self.workspace = unzip(fdata)
        else:
            if fname != '' and fname != None: self.workspace = unzip(open(fname, 'r').read())
            else: self.workspace = {}
            
class Rels:
    "资源引用读取"
    workspace = ''
    document = ''
    def __init__(self, workspace):
        self.workspace = workspace
        self.document = self.workspace[u'word/_rels/document.xml.rels']
    def read(self):
        pass
    def get(self):
        return self.document
    
class Style:
    "styles"
    pass

class Font:
    "font table"
    pass

class Document:
    workspace = ''
    document = ''
    def __init__(self, workspace):
        self.workspace = workspace
        self.document = self.workspace[u'word/document.xml']
    def get(self):
        assert u'word/document.xml' in self.workspace.keys()
        return self.document

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

if __name__ == '__main__':
    if len(sys.argv) > 1:
        del sys.argv[0]
        for fname in sys.argv:
            oxml_object = Work(fname).testxml()
            print oxml_object.doms()
            #OpenXML(fname)
    else:
        print ":: 没有指定任何 输入 文件."