#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Luo Zijun
# Email: luozijun.assistant@gmail.com

import StringIO
import zipfile

def uncompress(data):
    # decode zip binary data.
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
