#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    RecordSize (4 bytes): A 32-bit unsigned integer that defines the number
                          of 16-bit WORDs in the record.
RecordFunction (2 bytes): A 16-bit unsigned integer that defines the type
                          of this record. The low-order byte MUST match the
                          low-order byte of one of the values in the RecordType
                          Enumeration.
       rdParam(variable): An optional place holder that is provided for
                          record-specific fields.
"""

import wmf.Constants.RecordType

class RecordBase:
    # data = windows metafile - windows metafile HEADER_RECORD( + Placeable_RECORD )
    data = None
    def __init__(self, data=None):
        self.data = data
    #@staticmethod
    def open(self, filename):
        # open windows metafile on disk filesystem.
        #return Record(open(filename, 'rb').read())
        pass
    def list(self):
        # return records of this windows metafile
        
    def count(self):
        # return records of this windows metafile
        pass

class Record(RecordBase):
    def __init__(self, data=None):
        RecordBase.__init__(self, data=data)
    def type(self, record):
        # return record type ( RecordFunction )
        record_type = self.header(record)['type']
        return {'type': record_type, 'function': RecordType.Record_Function[record_type]}
    def size(self, record):
        # return record size
        return self.header(record)['size']
    def body(self, record):
        # return record body ( variable )
        header = self.header(record)
        return record[6:header['size']]
    def header(self, record):
        # return record header ( size + type ) .
        record_type, record_size = unpack("IH", record)
        return {'type': record_type, 'size': record_size}
