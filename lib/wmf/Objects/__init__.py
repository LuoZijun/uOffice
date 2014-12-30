#!/usr/bin/env python
#-*- coding:utf-8 -*-

# The WMF Structure Objects specify data structures that are embedded in WMF objects and records.
# Structure objects, unlike graphics objects, are not explicitly created or deleted; they are
# components of more complex structures.

"""
    @@ Windows Metafile Objects 
"""
class ObjectBase:
    def __init__(self, data):
        pass
    def list(self):
        # return object list of window metafile.
        pass
    def count(self):
        # count window metafile object num.
        pass

class Object(ObjectBase):
    def __init__(self, data):
        pass