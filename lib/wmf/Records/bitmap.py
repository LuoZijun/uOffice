#!/usr/bin/env python
#-*- coding:utf-8 -*-


class META_BITBLT:
    def __init__(self, data):
        #assert 
        pass
class META_DIBBITBLT:
    def __init__(self, data):
        #assert 
        pass
class META_DIBSTRETCHBLT:
    def __init__(self, data):
        #assert 
        pass
class META_SETDIBTODEV:
    def __init__(self, data):
        #assert 
        pass

class META_STRETCHBLT:
    def __init__(self, data):
        #assert 
        pass

"""

RecordSize (4 bytes): A 32-bit unsigned integer that defines the number of WORDs in the
record.
RecordFunction (2 bytes): A 16-bit unsigned integer that defines this WMF record type. The
lower byte MUST match the lower byte of the RecordType Enumeration (section 2.1.1.1)
value META_STRETCHDIB.
RasterOperation (4 bytes): A 32-bit unsigned integer that defines how the source pixels, the
current brush in the playback device context, and the destination pixels are to be combined to
form the new image. This code MUST be one of the values in the Ternary Raster Operation
Enumeration (section 2.1.1.31).
ColorUsage (2 bytes): A 16-bit unsigned integer that defines whether the Colors field of the
DIB contains explicit RGB values or indexes into a palette. This value MUST be in the
ColorUsage Enumeration (section 2.1.1.6).
SrcHeight (2 bytes): : A 16-bit signed integer that defines the height, in logical units, of the
source rectangle.
SrcWidth (2 bytes): : A 16-bit signed integer that defines the width, in logical units, of the
source rectangle.
YSrc (2 bytes): A 16-bit signed integer that defines the y-coordinate, in logical units, of the
source rectangle.
XSrc (2 bytes): A 16-bit signed integer that defines the x-coordinate, in logical units, of the
source rectangle.
DestHeight (2 bytes): A 16-bit signed integer that defines the height, in logical units, of the
destination rectangle.
DestWidth (2 bytes): A 16-bit signed integer that defines the width, in logical units, of the
destination rectangle.
yDst (2 bytes): A 16-bit signed integer that defines the y-coordinate, in logical units, of the
upper-left corner of the destination rectangle.
xDst (2 bytes): A 16-bit signed integer that defines the x-coordinate, in logical units, of the
upper-left corner of the destination rectangle.
DIB (variable): A variable-sized DeviceIndependentBitmap Object (section 2.2.2.9) that is the
source of the color data.
The source image in the DIB is specified in one of the following formats:
An array of pixels with a structure specified by the ColorUsage field and information in the
DeviceIndependentBitmap header.
A JPEG image `[JFIF] <http://www.w3.org/Graphics/JPEG/jfif.txt>`_ . <55>
A PNG image `[W3C-PNG] <http://www.w3.org/TR/PNG/>`_ . <56>
If the image format is JPEG or PNG, the ColorUsage field in this record MUST be set to
DIB_RGB_COLORS, and the RasterOperation field MUST be set to SRCCOPY.


"""
class META_STRETCHDIB:
    def __init__(self, data):
        #assert 
        pass
