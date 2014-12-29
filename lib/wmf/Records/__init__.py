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

class RecordBase:
    data = None
    def __init__(self, data):
        self.data = data
    def list(self):
        # return records of this windows metafile
        pass
    def count(self):
        # return records of this windows metafile
        pass

class Record(RecordBase):
    # function type.  Key: Hex Number
    Record_Function = {
        0x0000: "META_EOF",
        0x0035: "META_REALIZEPALETTE",
        0x0037: "META_SETPALENTRIES",
        0x0102: "META_SETBKMODE",
        0x0103: "META_SETMAPMODE",
        0x0104: "META_SETROP2",
        0x0105: "META_SETRELABS",
        0x0106: "META_SETPOLYFILLMODE",
        0x0107: "META_SETSTRETCHBLTMODE",
        0x0108: "META_SETTEXTCHAREXTRA",
        0x0127: "META_RESTOREDC",
        0x0139: "META_RESIZEPALETTE",
        0x0142: "META_DIBCREATEPATTERNBRUSH",
        0x0149: "META_SETLAYOUT",
        0x0201: "META_SETBKCOLOR",
        0x0209: "META_SETTEXTCOLOR",
        0x0211: "META_OFFSETVIEWPORTORG",
        0x0213: "META_LINETO",
        0x0214: "META_MOVETO",
        0x0220: "META_OFFSETCLIPRGN",
        0x0228: "META_FILLREGION",
        0x0231: "META_SETMAPPERFLAGS",
        0x0234: "META_SELECTPALETTE",
        0x0324: "META_POLYGON",
        0x0325: "META_POLYLINE",
        0x020A: "META_SETTEXTJUSTIFICATION",
        0x020B: "META_SETWINDOWORG",
        0x020C: "META_SETWINDOWEXT",
        0x020D: "META_SETVIEWPORTORG",
        0x020E: "META_SETVIEWPORTEXT",
        0x020F: "META_OFFSETWINDOWORG",
        0x0410: "META_SCALEWINDOWEXT",
        0x0412: "META_SCALEVIEWPORTEXT",
        # Part 2
        0x0415: "META_EXCLUDECLIPRECT",
        0x0416: "META_INTERSECTCLIPRECT",
        0x0418: "META_ELLIPSE",
        0x0419: "META_FLOODFILL",
        0x0429: "META_FRAMEREGION",
        0x0436: "META_ANIMATEPALETTE",
        0x0521: "META_TEXTOUT",
        0x0538: "META_POLYPOLYGON",
        0x0548: "META_EXTFLOODFILL",
        0x041B: "META_RECTANGLE",
        0x041F: "META_SETPIXEL",
        0x061C: "META_ROUNDRECT",
        0x061D: "META_PATBLT",
        0x001E: "META_SAVEDC",
        0x081A: "META_PIE",
        0x0B23: "META_STRETCHBLT",
        0x0626: "META_ESCAPE",
        0x012A: "META_INVERTREGION",
        0x012B: "META_PAINTREGION",
        0x012C: "META_SELECTCLIPREGION",
        0x012D: "META_SELECTOBJECT",
        0x012E: "META_SETTEXTALIGN",
        0x0817: "META_ARC",
        0x0830: "META_CHORD",
        0x0922: "META_BITBLT",
        0x0a32: "META_EXTTEXTOUT",
        0x0d33: "META_SETDIBTODEV",
        0x0940: "META_DIBBITBLT",
        0x0b41: "META_DIBSTRETCHBLT",
        0x0f43: "META_STRETCHDIB",
        0x01f0: "META_DELETEOBJECT",
        0x00f7: "META_CREATEPALETTE",
        0x01F9: "META_CREATEPATTERNBRUSH",
        0x02FA: "META_CREATEPENINDIRECT",
        0x02FB: "META_CREATEFONTINDIRECT",
        0x02FC: "META_CREATEBRUSHINDIRECT",
        0x06FF: "META_CREATEREGION"
    }
    def __init__(self):
        pass
    def type(self, record):
        # return record type ( RecordFunction )
        record_type = self.header(record)['type']
        return {'type': record_type, 'function': Record_Function[record_type]}
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