#!/usr/bin/env python
#-*- coding:utf-8 -*-

# This section defines the Bitmap Record Types, which specify records that manage and output
# bitmaps.
# The following are the Bitmap Record Types.


"""
The META_BITBLT record specifies the transfer of a block of pixels according to a raster
operation.The destination of the transfer is the current output region in the playback device context.
There are two forms of META_BITBLT, one which specifies a bitmap as the source, and the other
which uses the playback device context as the source. The fields that are the same in the two forms
of META_BITBLT are defined below. The subsections that follow specify the packet structures of the
two forms of META_BITBLT.

RecordSize: A 32-bit unsigned integer that defines the number of 16-bit WORDs in the record.
RecordFunction: A 16-bit unsigned integer that defines this WMF record type. The low-order byte
MUST match the low-order byte of the RecordType enumeration (section 2.1.1.1) value
META_BITBLT.
RasterOperation: A 32-bit unsigned integer that defines how the source pixels, the current brush
in the playback device context, and the destination pixels are to be combined to form the new
image. This code MUST be one of the values in the Ternary Raster Operation enumeration
(section 2.1.1.31).
YSrc: A 16-bit signed integer that defines the y-coordinate, in logical units, of the upper-left corner
of the source rectangle.
XSrc: A 16-bit signed integer that defines the x-coordinate, in logical units, of the upper-left corner
of the source rectangle.
Height: A 16-bit signed integer that defines the height, in logical units, of the source and
destination rectangles.
Width: A 16-bit signed integer that defines the width, in logical units, of the source and destination
rectangles.
YDest: A 16-bit signed integer that defines the y-coordinate, in logical units, of the upper-left
corner of the destination rectangle.
XDest: A 16-bit signed integer that defines the x-coordinate, in logical units, of the upper-left
corner of the destination rectangle.


The RecordSize and RecordFunction fields SHOULD be used to differentiate between the two
forms of META_BITBLT. If the following Boolean expression is TRUE, a source bitmap is not specified
in the record.

    RecordSize == ((RecordFunction >> 8) + 3)


"""
class META_BITBLT:
    def __init__(self, data):
        #assert 
        pass
    def decode(self, data):
        # With BMP
        # RecordSize / RecordFunction / RasterOperation / YSrc / XSrc / Height / Width / YDest / XDest / Target (variable)
        
        # RecordFunction (2 bytes): A 16-bit unsigned integer that defines this WMF record type. The
        #    low-order byte MUST match the low-order byte of the RecordType enumeration (section
        #    2.1.1.1) value META_BITBLT. The high-order byte MUST contain a value equal to the
        #    number of 16-bit WORDs in the record minus the number of WORDs in the RecordSize and
        #    Target fields. That is:
        #        RecordSize - (2 + (sizeof(Target)/2))
        # Target (variable): A variable-sized Bitmap16 Object (section 2.2.2.1) that defines source
        #    image content. This object MUST be specified, even if the raster operation does not require a
        #    source.
        unpack("LHLhhhhhh", data)
        # With out BMP
        # RecordSize / RecordFunction / RasterOperation / YSrc / XSrc (!Reserved!) / Height / Width / YDest / XDest
        
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
