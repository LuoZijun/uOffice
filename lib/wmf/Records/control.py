#!/usr/bin/env python
#-*- coding:utf-8 -*-

from struct import unpack

"""
Record Type Category: 
    Control Record Types:
        META_EOF
        META_HEADER
        META_PLACEABLE


Note:
    先暂时不考虑这种 placeable record 文件. 

META_HEADER Record
==========================
The META_HEADER record is the first record in a standard (nonplaceable) WMF metafile.


Type (2 bytes): A 16-bit unsigned integer that defines the type of metafile. It MUST be a value
in the MetafileType enumeration (section 2.1.1.18).
HeaderSize (2 bytes): A 16-bit unsigned integer that defines the number of 16-bit words in
the header.
Version (2 bytes): A 16-bit unsigned integer that defines the metafile version. It MUST be a
value in the MetafileVersion enumeration (section 2.1.1.19).<57>
SizeLow (2 bytes): A 16-bit unsigned integer that defines the low-order word of the number of
16-bit words in the entire metafile.
SizeHigh (2 bytes): A 16-bit unsigned integer that defines the high-order word of the number
of 16-bit words in the entire metafile.
NumberOfObjects (2 bytes): A 16-bit unsigned integer that specifies the number of graphics
objects that are defined in the entire metafile. These objects include brushes, pens, and the
other objects specified in section 2.2.1.
MaxRecord (4 bytes): A 32-bit unsigned integer that specifies the size of the largest record
used in the metafile (in 16-bit elements).
NumberOfMembers (2 bytes): A 16-bit unsigned integer that is not used. It SHOULD be
0x0000.

See section 2.3.2 for the specification of similar records.


META_PLACEABLE Record
==========================
The META_PLACEABLE record is the first record in a placeable WMF metafile, which is an extension
to the WMF metafile format.<58> The information in this extension allows the specification of the
placement and size of the target image, which makes it adaptable to different output devices.
The META_PLACEABLE record MUST be the first record of the metafile, located immediately before
the META_HEADER record (section 2.3.2.2).

Key (4 bytes): Identification value that indicates the presence of a placeable metafile header.
This value MUST be 0x9AC6CDD7.
HWmf (2 bytes): The resource handle to the metafile, when the metafile is in memory. When
the metafile is on disk, this field MUST contain 0x0000. This attribute of the metafile is
specified in the Type field of the META_HEADER record.
BoundingBox (8 bytes): The destination rectangle, measured in logical units, for displaying
the metafile. The size of a logical unit is specified by the Inch field.
Inch (2 bytes): The number of logical units per inch used to represent the image. This value
can be used to scale an image.
By convention, an image is considered to be recorded at 1440 logical units (twips) per inch.
Thus, a value of 720 specifies that the image SHOULD be rendered at twice its normal size,
and a value of 2880 specifies that the image SHOULD be rendered at half its normal size.
Reserved (4 bytes): A field that is not used and MUST be set to 0x00000000.
Checksum (2 bytes): A checksum for the previous 10 16-bit values in the header. This value
can be used to determine whether the metafile has become corrupted.

See section 2.3.2 for the specification of similar records.

META_EOF Record
======================
The META_EOF record indicates the end of the WMF metafile.

RecordSize (4 bytes): A 32-bit unsigned integer that defines the number of 16-bit WORDs in
the record.
RecordFunction (2 bytes): A 16-bit unsigned integer that defines the type of this record. For
META_EOF, this value MUST be 0x0000, as specified in the RecordType Enumeration table.

See section 2.3.2 for the specification of similar records.

"""

class Control:
    def __init__(self):
        pass
    @staticmethod
    def header(self, data):
        # META_HEADER Record ( 18 bytes )
        assert len(data) == 18
        # header_size: A 16-bit unsigned integer that defines the number of 16-bit words in the header.
        # size_low: A 16-bit unsigned integer that defines the low-order word of the number of 16-bit words in the entire metafile. (liite-ending) 低字节序 ? 
        # size_hight: A 16-bit unsigned integer that defines the high-order word of the number of 16-bit words in the entire metafile. (hight-ending) 高字节序 ?
        # objects: A 16-bit unsigned integer that specifies the number of graphics
        #                 objects that are defined in the entire metafile. These objects include brushes, pens, and the
        #                 other objects specified in section 2.2.1.
        #                 (NumberOfObjects : 2 bytes)
        # members: A 16-bit unsigned integer that is not used. It SHOULD be 0x0000. (  NumberOfMembers: 2 bytes)
        # max_record: 0x0000000C specifies the size in WORDs of the largest record in the metafile, which is equivalent to 24 (0x00000018) bytes. ( MaxRecord )

        ## NOTE: Based on the value of the NumberOfObjects field, a WMF Object Table (section 3.1.4.1) can be created that is large enough for 2 objects.
        metafile_type, header_size, metafile_version, size_low, size_hight,  objects, max_record, members = unpack("HHHHHHIH", data)
        return {'metafile_type': metafile_type, 'metafile_version': metafile_version, 'header_size': header_size, \
        'size_low': size_low, 'size_hight': size_hight, 'objects': objects, 'members': members, 'max_record': max_record}

    @staticmethod
    def eof(self data):
        # META_EOF Record ( 6 bytes )
        assert len(data) == 6
        # size ( 4 bytes ): A 32-bit unsigned integer that defines the number of 16-bit WORDs in the record.
        # function ( 2 bytes ): A 16-bit unsigned integer that defines the type of this record. For META_EOF, 
        #                                        this value MUST be 0x0000, as specified in the RecordType Enumeration table.
        size, function  = unpack("IH", data)
        return {'size': size, 'function': function}

    @staticmethod
    def placeable(self, data):
        # META_PLACEABLE Record ( 22 bytes )
        # Key: 4bytes HWmf: 2bytes  BoundingBox: 8bytes Inch: 2bytes Reserved: 4bytes Checksum: 2bytes
        assert len(data) == 22
        # key ( 4 bytes ): Identification value that indicates the presence of a placeable metafile header. This value MUST be 0x9AC6CDD7.
        # HWmf (2 bytes): The resource handle to the metafile, when the metafile is in memory. 
        #                                  When the metafile is on disk, this field MUST contain 0x0000. 
        #                                  This attribute of the metafile is specified in the Type field of the META_HEADER record.
        # BoundingBox (8 bytes): The destination rectangle, measured in logical units, 
        #                                                for displaying the metafile. The size of a logical unit is specified by the Inch field.
        # Inch (2 bytes): The number of logical units per inch used to represent the image. This value can be used to scale an image.
        # Reserved (4 bytes): A field that is not used and MUST be set to 0x00000000.
        # Checksum (2 bytes): A checksum for the previous 10 16-bit values in the header.
        #                                          This value can be used to determine whether the metafile has become corrupted.
        key, HWmf, BoundingBox, Inch, Reserved, Checksum = unpack("IHQHIH", data)
        return {"key": key, 'HWmf': HWmf, 'BoundingBox': BoundingBox, 'Inch': Inch, 'Reserved': Reserved, 'Checksum': Checksum}
