#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""

The MetafileVersion Enumeration defines values that specify support for device-independent
bitmaps (DIBs) in metafiles.

typedef enum
{
    METAVERSION100 = 0x0100,
    METAVERSION300 = 0x0300
} MetafileVersion;

METAVERSION100: DIBs are not supported.
METAVERSION300: DIBs are supported.


"""

MetafileVersion = {
    0x0100:{"hex": "0x0100", "dec": int("0x0100", 16), "desc": "DIBs are not supported."},
    0x0300:{"hex": "0x0300", "dec": int("0x0300", 16), "desc": "DIBs are supported."},
}