#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os,sys,time

data = open("good.wmf", 'r').read()

os.chdir("/var/www")
print ":: Now Work DIR: %s " % (os.getcwd())
sys.path.append( os.path.join(os.getcwd(), '') )

import uOffice
import wmf
import wmf.Constants
import wmf.Records
import wmf.Objects

print dir(wmf.Records)

r = wmf.Records.Record(data)
print r
print dir(r)