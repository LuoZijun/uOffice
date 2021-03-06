#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""

The MetafileType Enumeration specifies where the metafile is stored.

typedef enum
{
    MEMORYMETAFILE = 0x0001,
    DISKMETAFILE = 0x0002
} MetafileType;

MEMORYMETAFILE: Metafile is stored in memory.
DISKMETAFILE: Metafile is stored on disk.


"""

MetafileType = {
    0x0001: {"hex": "0x0001", "dec": int("0x0001", 16), "type": "MEMORYMETAFILE", "desc": "Metafile is stored in memory."},
    0x0002: {"hex": "0x0002", "dec": int("0x0002", 16), "type": "DISKMETAFILE", "desc": "Metafile is stored on disk."},
}
"""
2.1.1.21
MetafileDataType Enumeration
The MetafileDataType enumeration defines types of metafiles data that can be embedded in an
EMF+ metafile.
typedef enum
{
MetafileDataTypeWmf = 0x00000001,
MetafileDataTypeWmf                = 0x00000002,
MetafileDataTypeEmf = 0x00000003,
MetafileDataTypeEmfPlusOnly = 0x00000004,
MetafileDataTypeEmfPlusDual = 0x00000005
} MetafileDataType;
"""