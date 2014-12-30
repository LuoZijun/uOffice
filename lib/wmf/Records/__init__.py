#!/usr/bin/env python
#-*- coding:utf-8 -*-

# During the playback of a WMF metafile, a playback device context exists that can be described as a
# processing state in which every graphics object and property is defined. In the descriptions of WMF
# records that follow in this section, an element of the playback device context can be referred to as a
# "currently selected" graphics object or property. If a graphics object or property that is used in the
# output operation specified by a record has not been explicitly selected, a default value MUST be
# used. See Playback Device Context (section 3.1.5) for more information.
# When a WMF metafile is processed, the order in which graphics output is performed MUST be the
# same as the order of drawing records in the metafile. Thus, a given drawing command is always
# rendered on top of the renderings of preceding commands.
# The following packet definition specifies the generic structure of all WMF records except Control records.

# RecordSize    (4 bytes): A 32-bit unsigned integer that defines the number of 16-bit WORDs in the record.
# RecordFunction(2 bytes): A 16-bit unsigned integer that defines the type of this record. The low-order 
#                          byte MUST match the low-order byte of one of the values in the RecordType Enumeration.
# rdParam      (variable): An optional place holder that is provided for record-specific fields.

# Python Data Format(pack/unpack):
#     b   8 bit signed integer
#     B   8 bit unsigned integer
#     h   16 bit signed integer
#     H   16 bit unsigned integer
#     l   32 bit signed integer
#     L   32 bit unsigned integer
#     q   64 bit signed integer
#     Q   64 bit unsigned integer
#     f   32 bit floating point number
#     d   64 bit floating point number

from struct import unpack
import wmf.Constants.RecordType

class RecordBase:
    body = None # windows metafile - windows metafile HEADER_RECORD( + Placeable_RECORD )
    def __init__(self, body=None):
        assert type(body) == type('')
        self.body = body
    #@staticmethod

    @classmethod
    def _read(self, ):
        # 处理单个 record
        pass
    def list(self):
        # return records of this windows metafile 
        records = []
        #data = self.body
        pos = 0
        run = True
        while run == True:
            
            try:
                record_size, record_type  = unpack("IH", self.body[pos:pos+6] )
                record_content = self.body[pos+6:pos+record_size]
                
                record = {'type': record_type, 'size': record_size, 'content': record_content}
                records.append( record )
                if wmf.Constants.RecordType.Record_Types[record_type] == "META_EOF":
                    print ":: META_EOF"
                    run = False
                else:
                    print ":: "
                pos += record_size
            except:
                #print e
                print "*************************************************************************"
                print ":: Record Type ( %s ) Unknow , Now POS at %d " % (hex(record_type), pos)
                break
            print record
        print "========================================================================="
        return records
    def count(self):
        # return records of this windows metafile
        pass

class Record(RecordBase):
    def __init__(self, body=None):
        RecordBase.__init__(self, body=body)
    def type(self, record):
        # return record type ( RecordFunction )
        record_type = self.header(record)['type']
        return {'type': record_type, 'function': wmf.Constants.RecordType.Record_Types[record_type]}
    def size(self, record):
        # return record size
        return self.header(record)['size']
    def body(self, record):
        # return record body ( variable )
        header = self.header(record)
        return record[6:header['size']]
    def header(self, record):
        # return record header ( size + type ) .  6 bytes
        record_size, record_type = unpack("IH", record)
        return {'type': record_type, 'size': record_size}
