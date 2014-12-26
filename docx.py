#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys,os,time
import StringIO

from tools import unzip
from lxml import etree


#     @staticmethod
"""
Open Office XML Format:
    
    # row
    w:p   #  ( w->prefix : p->dom name )  # Shuld add one, 
             # Values: w:rsidR="00D33BCF" w:rsidRDefault="00EF061D"
        w:pPr || w:r    
            w:rPr  || w:t # Text


        # prefix: m, oMathPara
        # prefix: m. oMath
        ## Document from [MS-ODRAWXML].pdf  PAGE: 34
        ## cGp, cGpRule, cSp, eqArrPr, mathFont, mathPr, mcJc, mcPr, mPr, oMath, r, rSp, rSpRule

"""


class Parse:
    def _init__(self):
        pass
    def test(self):
        pass

class OpenXML:
    document = None
    Gtag = []
    def __init__(self, xml, Gtag=[]):
        f = StringIO.StringIO()
        f.write(xml)
        self.document = etree.parse(f)
        self.Gtag = Gtag
    def doms(self):
        # Show XML DOM Nodes ( Object )
        root = document.getroot()
        for dom in self.document.getiterator():
            DOMS.append(dom)
        return DOMS
    def fetch(self):
        

class Docx:
    docx = None
    good_tag = []
    def __init__(self, docx):
        # docx data need unzip.
        self.docx = unzip.uncompress( docx )
    def parse(self):
        assert u'word/document.xml' in self.docx.keys()
        document = self.docx[u'word/document.xml']
        OpenXML(document)
        print document



if __name__ == '__main__':
    if len(sys.argv) > 1:
        del sys.argv[0]
        for f in sys.argv:
            docx = Docx(open(f, 'r').read())
            docx.parse()
    else:
        print ":: 没有指定任何 输入 文件."