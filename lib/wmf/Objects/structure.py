#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
The Bitmap16 Object specifies information about the dimensions and color format of a bitmap.

Type (2 bytes): A 16-bit signed integer that defines the bitmap type.

Width (2 bytes): A 16-bit signed integer that defines the width of the bitmap in pixels.

Height (2 bytes): A 16-bit signed integer that defines the height of the bitmap in scan lines.
WidthBytes (2 bytes): A 16-bit signed integer that defines the number of bytes per scan line.

Planes (1 byte): An 8-bit unsigned integer that defines the number of color planes in the
bitmap. The value of this field MUST be 0x01.
BitsPixel (1 byte): An 8-bit unsigned integer that defines the number of adjacent color bits on
each plane.

Bits (variable): A variable length array of bytes that defines the bitmap pixel data. The length
of this field in bytes can be computed as follows.
(((Width * BitsPixel + 15) >> 4) << 1) * Height


"""
class Bitmap16:
    def __init__(self):
        pass
    def decode(self, data):
        obj = {}
        Type, Width, Height, WidthBytes, Planes, BitsPixel = unpack("hhhhBB", data[0:10])
        Bits_size = (((Width * BitsPixel + 15) >> 4) << 1) * Height
        Bits = unpack("s"*Bits_size, data[10:Bits_size])
        obj['Type'] = Type
        obj['Width'] = Width
        obj['Height'] = Height
        obj['WidthBytes'] = WidthBytes
        obj['Planes'] = Planes
        obj['BitsPixel'] = BitsPixel
        obj['Bits'] = Bits
        return obj

"""
The BitmapCoreHeader Object contains information about the dimensions and color format of a
device-independent bitmap (DIB).<45>

HeaderSize (4 bytes): A 32-bit unsigned integer that defines the size of this object, in bytes.
Width (2 bytes): A 16-bit unsigned integer that defines the width of the DIB, in pixels.
Height (2 bytes): A 16-bit unsigned integer that defines the height of the DIB, in pixels.
Planes (2 bytes): A 16-bit unsigned integer that defines the number of planes for the target
device. This value MUST be 0x0001.
BitCount (2 bytes): A 16-bit unsigned integer that defines the format of each pixel, and the
maximum number of colors in the DIB. This value MUST be in the BitCount Enumeration
(section 2.1.1.3).
A DIB is specified by a DeviceIndependentBitmap Object (section 2.2.2.9).


"""
class BitmapCoreHeader:
    def __init__(self):
        pass

"""
The BitmapInfoHeader Object contains information about the dimensions and color format of a
device-independent bitmap (DIB).

HeaderSize (4 bytes): A 32-bit unsigned integer that defines the size of this object, in bytes.
Width (4 bytes): A 32-bit signed integer that defines the width of the DIB, in pixels. This value
MUST be positive.
This field SHOULD<46> specify the width of the decompressed image file, if the
Compression value specifies JPEG or PNG format.
Height (4 bytes): A 32-bit signed integer that defines the height of the DIB, in pixels. This
value MUST NOT be zero.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|     Value          |        Meaning                                                                     |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| 0x00000000 < value | If this value is positive, the DIB is a bottom-up bitmap, and its origin is the    |
|                    | lower-left corner.                                                                 |
|                    | This field SHOULD<47> specify the height of the decompressed image file, if        |
|                    | the Compression value specifies JPEG or PNG format.                                |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| value < 0x00000000 | If this value is negative, the DIB is a top-down bitmap, and its origin is the     |
|                    | upper-left corner. Top-down bitmaps do not support compression.                    |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Planes (2 bytes): A 16-bit unsigned integer that defines the number of planes for the target
device. This value MUST be 0x0001.

BitCount (2 bytes): A 16-bit unsigned integer that defines the number of bits that define each
pixel and the maximum number of colors in the DIB. This value MUST be in the BitCount
Enumeration (section 2.1.1.3).
Compression (4 bytes): A 32-bit unsigned integer that defines the compression mode of the
DIB. This value MUST be in the Compression Enumeration (section 2.1.1.7).
This value MUST NOT specify a compressed format if the DIB is a top-down bitmap, as
indicated by the Height value.
ImageSize (4 bytes): A 32-bit unsigned integer that defines the size, in bytes, of the image.
If the Compression value is BI_RGB, this value SHOULD be zero and MUST be ignored.<48>
If the Compression value is BI_JPEG or BI_PNG, this value MUST specify the size of the JPEG
or PNG image buffer, respectively.
XPelsPerMeter (4 bytes): A 32-bit signed integer that defines the horizontal resolution, in
pixels-per-meter, of the target device for the DIB.
YPelsPerMeter (4 bytes): A 32-bit signed integer that defines the vertical resolution, in pixels-
per-meter, of the target device for the DIB.
ColorUsed (4 bytes): A 32-bit unsigned integer that specifies the number of indexes in the
color table used by the DIB, as follows:
If this value is zero, the DIB uses the maximum number of colors that correspond to the
BitCount value.
If this value is nonzero and the BitCount value is less than 16, this value specifies the
number of colors used by the DIB.
If this value is nonzero and the BitCount value is 16 or greater, this value specifies the
size of the color table used to optimize performance of the system palette.
Note If this value is nonzero and greater than the maximum possible size of the color table
based on the BitCount value, the maximum color table size SHOULD be assumed.
ColorImportant (4 bytes): A 32-bit unsigned integer that defines the number of color indexes
that are required for displaying the DIB. If this value is zero, all color indexes are required.
A DIB is specified by a DeviceIndependentBitmap Object (section 2.2.2.9).
When the array of pixels in the DIB immediately follows the BitmapInfoHeader, the DIB is a packed
bitmap. In a packed bitmap, the ColorUsed value MUST be either 0x00000000 or the actual size of
the color table.


"""
class BitmapInfoHeader:
    def __init__(self):
        pass


"""
The BitmapV4Header Object contains information about the dimensions and color format of a
device-independent bitmap (DIB). It is an extension of the BitmapInfoHeader object (section
2.2.2.3).<49>

BitmapInfoHeader (40 bytes): A BitmapInfoHeader object, which defines properties of the
DIB.
RedMask (4 bytes): A 32-bit unsigned integer that defines the color mask that specifies the
red component of each pixel. If the Compression value in the BitmapInfoHeader object is not
BI_BITFIELDS, this value MUST be ignored.
GreenMask (4 bytes): A 32-bit unsigned integer that defines the color mask that specifies the
green component of each pixel. If the Compression value in the BitmapInfoHeader object is
not BI_BITFIELDS, this value MUST be ignored.
BlueMask (4 bytes): A 32-bit unsigned integer that defines the color mask that specifies the
blue component of each pixel. If the Compression value in the BitmapInfoHeader object is
not BI_BITFIELDS, this value MUST be ignored.
AlphaMask (4 bytes): A 32-bit unsigned integer that defines the color mask that specifies the
alpha component of each pixel.
ColorSpaceType (4 bytes): A 32-bit unsigned integer that defines the color space of the
Device Independent Bitmap object (section 2.2.2.9). If this value is LCS_CALIBRATED_RGB
from the LogicalColorSpace enumeration (section 2.1.1.14), the color values in the DIB are
calibrated RGB values, and the endpoints and gamma values in this structure SHOULD be
used to translate the color values before they are passed to the device.
See the LogColorSpace objects (sections 2.2.2.11 and 2.2.2.12) for details concerning a
logical color space.
Endpoints (36 bytes): A CIEXYZTriple object (section 2.2.2.7) that defines the CIE
chromaticity x, y, and z coordinates of the three colors that correspond to the red, green, and
blue endpoints for the logical color space associated with the DIB. If the ColorSpaceType
field does not specify LCS_CALIBRATED_RGB, this field MUST be ignored.
GammaRed (4 bytes): A 32-bit fixed point value that defines the toned response curve for red.
If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST be
ignored.
GammaGreen (4 bytes): A 32-bit fixed point value that defines the toned response curve for
green. If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST
be ignored.
GammaBlue (4 bytes): A 32-bit fixed point value that defines the toned response curve for
blue. If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST be
ignored.
The gamma value format is an unsigned "8.8" fixed-point integer that is then left-shifted by 8 bits.
"8.8" means "8 integer bits followed by 8 fraction bits": nnnnnnnnffffffff. Taking the shift into
account, the required format of the 32-bit DWORD is: 00000000nnnnnnnnffffffff00000000.



"""
class BitmapV4Header:
    def __init__(self):
        pass

"""
The BitmapV5Header Object contains information about the dimensions and color format of a
device-independent bitmap (DIB). It is an extension of the BitmapV4Header object (section
2.2.2.4). <50>

BitmapV4Header (108 bytes): A BitmapV4Header object, which defines properties of the DIB.
When it is part of a BitmapV5Header, the ColorSpaceType field of a BitmapV4Header can be
a logical color space value in the LogicalColorSpaceV5 enumeration (section 2.1.1.15).
Intent (4 bytes): A 32-bit unsigned integer that defines the rendering intent for the DIB. This
MUST be defined in the LogicalColorSpace enumeration (section 2.1.1.14).
ProfileData (4 bytes): A 32-bit unsigned integer that defines the offset, in bytes, from the
beginning of this structure to the start of the color profile data.

If the color profile is embedded in the DIB, ProfileData is the offset to the actual color
profile; if the color profile is linked, ProfileData is the offset to the null-terminated file name
of the color profile. This MUST NOT be a Unicode string, but MUST be composed exclusively of
characters from the Windows character set (code page 1252).
If the ColorSpaceType field in the BitmapV4Header does not specify LCS_PROFILE_LINKED
or LCS_PROFILE_EMBEDDED, the color profile data SHOULD be ignored.
ProfileSize (4 bytes): A 32-bit unsigned integer that defines the size, in bytes, of embedded
color profile data.
Reserved (4 bytes): A 32-bit unsigned integer that is undefined and SHOULD be ignored.

"""
class BitmapV5Header:
    def __init__(self):
        pass

"""
The CIEXYZ Object defines information about the CIEXYZ chromaticity object.

ciexyzX (4 bytes): A 32-bit 2.30 fixed point type that defines the x chromaticity value.
ciexyzY (4 bytes): A 32-bit 2.30 fixed point type that defines the y chromaticity value.
ciexyzZ (4 bytes): A 32-bit 2.30 fixed point type that defines the z chromaticity value.

"""
class CIEXYZ:
    def __init__(self):
        pass

"""
The CIEXYZTriple Object defines information about the CIEXYZTriple color object.

ciexyzRed (12 bytes): A 96-bit CIEXYZ Object that defines the red chromaticity values.
ciexyzGreen (12 bytes): A 96-bit CIEXYZ Object that defines the green chromaticity values.
ciexyzBlue (12 bytes): A 96-bit CIEXYZ Object that defines the blue chromaticity values.

"""
class CIEXYZTriple:
    def __init__(self):
        pass

"""
The ColorRef Object defines the RGB color.

Red (1 byte): An 8-bit unsigned integer that defines the relative intensity of red.
Green (1 byte): An 8-bit unsigned integer that defines the relative intensity of green.
Blue (1 byte): An 8-bit unsigned integer that defines the relative intensity of blue.
Reserved (1 byte): An 8-bit unsigned integer that MUST be 0x00.

"""
class ColorRef:
    def __init__(self):
        pass

"""
The DeviceIndependentBitmap Object defines an image in device-independent bitmap (DIB) format.

DIBHeaderInfo (variable): Either a BitmapCoreHeader Object (section 2.2.2.2) or a
BitmapInfoHeader Object (section 2.2.2.3) that specifies information about the image.
The first 32 bits of this field is the HeaderSize value. If it is 0x0000000C, then this is a
BitmapCoreHeader; otherwise, this is a BitmapInfoHeader.

Colors (variable): An optional array of either RGBQuad Objects (section 2.2.2.20) or 16-bit
unsigned integers that define a color table.
The size and contents of this field SHOULD be determined from the metafile record or object
that contains this DeviceIndependentBitmap and from information in the DIBHeaderInfo
field. See ColorUsage Enumeration (section 2.1.1.6) and BitCount Enumeration
(section 2.1.1.3) for additional details.

BitmapBuffer (variable): A buffer containing the image, which is not required to be
contiguous with the DIB header, unless this is a packed bitmap.

    UndefinedSpace (variable): An optional field that MUST be ignored. If this DIB is a
    packed bitmap, this field MUST NOT be present.
    aData (variable): An array of bytes that define the image.
    The size and format of this data is determined by information in the DIBHeaderInfo
    field. If it is a BitmapCoreHeader, the size in bytes MUST be calculated as follows:
    (((Width * Planes * BitCount + 31) & ~31) / 8) * abs(Height)
    This formula SHOULD also be used to calculate the size of aData when DIBHeaderInfo
    is a BitmapInfoHeader Object, using values from that object, but only if its
    Compression value is BI_RGB, BI_BITFIELDS, or BI_CMYK.
    Otherwise, the size of aData MUST be the BitmapInfoHeader Object value ImageSize.


"""
class DeviceIndependentBitmap:
    def __init__(self):
        pass

"""
The LogBrush Object defines the style, color, and pattern of a brush. This object is used only in the
META_CREATEBRUSHINDIRECT Record (section 2.3.4.1) to create a Brush Object (section 2.2.1.1).

BrushStyle (2 bytes): A 16-bit unsigned integer that defines the brush style. This MUST be a
value from the BrushStyle Enumeration (section 2.1.1.4). For the meanings of different
values, see the following table. The BS_NULL style specifies a brush that has no effect.<51>
ColorRef (4 bytes): A 32-bit ColorRef Object (section 2.2.2.8) that specifies a color. Its
interpretation depends on the value of BrushStyle, as explained in the following.
BrushHatch (2 bytes): A 16-bit field that specifies the brush hatch type. Its interpretation
depends on the value of BrushStyle, as explained in the following.
The following table shows the relationship between values in the BrushStyle, ColorRef and
BrushHatch fields in a LogBrush Object. Only supported brush styles are listed.

## Table
BrushStyle ## h1
BS_SOLID
BS_NULL
BS_PATTERN
ColorRef   ## h2
SHOULD be a ColorRef Object,
which determines the color of the
brush.
Not used, and SHOULD be
ignored.
Not used, and SHOULD be
ignored.
BS_DIBPATTERN
BS_DIBPATTERNPT
BS_HATCHED
Not used, and SHOULD be
ignored.
Not used, and SHOULD be
ignored.
SHOULD be a ColorRef Object,
which determines the foreground
color of the hatch pattern.
BrushHatch  ## h3
Not used, and SHOULD be ignored.
Not used, and SHOULD be ignored.
Not used. A default object, such as a solid-
color black Brush Object, MAY be
created.<52>
Not used. A default object, such as a solid-
color black Brush Object, MAY be created.
Not used. A default object, such as a solid-
color black Brush Object, MAY be created.
A value from the HatchStyle Enumeration
(section 2.1.1.12) that specifies the
orientation of lines used to create the hatch.

"""
class LogBrush:
    def __init__(self):
        pass


"""
The LogColorSpace object specifies a logical color space for the playback device context, which can
be the name of a color profile in ASCII characters.

Signature (4 bytes): A 32-bit unsigned integer that specifies the signature of color space
objects; it MUST be set to the value 0x50534F43, which is the ASCII encoding of the string
"PSOC".
Version (4 bytes): A 32-bit unsigned integer that defines a version number; it MUST be
0x00000400.
Size (4 bytes): A 32-bit unsigned integer that defines the size of this object, in bytes.
ColorSpaceType (4 bytes): A 32-bit signed integer that specifies the color space type. It
MUST be defined in the LogicalColorSpace enumeration (section 2.1.1.14). If this value is
LCS_sRGB or LCS_WINDOWS_COLOR_SPACE, the sRGB color space MUST be used.
Intent (4 bytes): A 32-bit signed integer that defines the gamut mapping intent. It MUST be
defined in the GamutMappingIntent enumeration (section 2.1.1.11).
Endpoints (36 bytes): A CIEXYZTriple object (section 2.2.2.7) that defines the CIE
chromaticity x, y, and z coordinates of the three colors that correspond to the RGB endpoints
for the logical color space associated with the bitmap. If the ColorSpaceType field does not
specify LCS_CALIBRATED_RGB, this field MUST be ignored.
GammaRed (4 bytes): A 32-bit fixed point value that defines the toned response curve for red.
If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST be
ignored.
GammaGreen (4 bytes): A 32-bit fixed point value that defines the toned response curve for
green. If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST
be ignored.
GammaBlue (4 bytes): A 32-bit fixed point value that defines the toned response curve for
blue. If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST be
ignored.
Filename (variable): An optional, ASCII charactger string that specifies the name of a file that
contains a color profile. If a file name is specified, and the ColorSpaceType field is set to
LCS_CALIBRATED_RGB, the other fields of this structure SHOULD be ignored.

The Endpoints, GammaRed, GammaGreen, and GammaBlue fields are used to specify a logical
color space. The Endpoints field is a CIEXYZTriple object that contains the x, y, and z values of the
RGB endpoint of the color space.
The relation between tri-stimulus values X,Y,Z and chromaticity values x,y,z is expressed as
follows.

    x = X/(X+Y+Z)
    y = Y/(X+Y+Z)
    z = Z/(X+Y+Z)

The GammaRed, GammaGreen, and GammaBlue fields contain values in "8.8 fixed point"
format, which is a technique for representing non-integer numbers. Each value consists of a zero-
extended 8-bit magnitude followed by an 8-bit fraction, with the combined 16 bits left-shifted by 8
bits. Thus, in 32-bits, the real value N.F is 00000000nnnnnnnnffffffff00000000, where "nnnnnnnn"
and "ffffffff" are binary representations of N and F, respectively. For example, for the real number
10.5, nnnnnnnn would be 00001010 (binary 10) and ffffffff would be 00000101 (binary 5), and the
complete 32-bit binary value would be 00000000000010100000010100000000, which is the
hexadecimal value 0x0A50.



"""
class LogColorSpace:
    def __init__(self):
        pass

"""
The LogColorSpaceW object specifies a logical color space, which can be defined by a color profile
file with a name consisting of Unicode 16-bit characters.

Signature (4 bytes): A 32-bit unsigned integer that specifies the signature of color space
objects. This MUST be set to the value 0x50534F43, which is the ASCII encoding of the string
"PSOC".
Version (4 bytes): A 32-bit unsigned integer that defines a version number; it MUST be
0x00000400.
Size (4 bytes): A 32-bit unsigned integer that defines the size of this object, in bytes.
ColorSpaceType (4 bytes): A 32-bit signed integer that specifies the color space type. It
MUST be defined in the LogicalColorSpace enumeration (section 2.1.1.14). If this value is
LCS_sRGB or LCS_WINDOWS_COLOR_SPACE, the sRGB color space MUST be used.
Intent (4 bytes): A 32-bit signed integer that defines the gamut mapping intent. It MUST be
defined in the GamutMappingIntent enumeration (section 2.1.1.11).
Endpoints (36 bytes): A CIEXYZTriple object (section 2.2.2.7) that defines the CIE
chromaticity x, y, and z coordinates of the three colors that correspond to the RGB endpoints
for the logical color space associated with the bitmap. If the ColorSpaceType field does not
specify LCS_CALIBRATED_RGB, this field MUST be ignored.
GammaRed (4 bytes): A 32-bit fixed point value that defines the toned response curve for red.
If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST be
ignored.
GammaGreen (4 bytes): A 32-bit fixed point value that defines the toned response curve for
green. If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST
be ignored.
GammaBlue (4 bytes): A 32-bit fixed point value that defines the toned response curve for
blue. If the ColorSpaceType field does not specify LCS_CALIBRATED_RGB, this field MUST be
ignored.
Filename (variable): An optional, null-terminated Unicode UTF16-LE character string, which
specifies the name of a file that contains a color profile. If a file name is specified, and the
ColorSpaceType field is set to LCS_CALIBRATED_RGB, the other fields of this structure
SHOULD be ignored.
See the LogColorSpace object (section 2.2.2.11) for additional details concerning the interpretation
of field values of this object.


"""
class LogColorSpaceW:
    def __init__(self):
        pass

"""
The PaletteEntry Object defines the color and usage of an entry in a palette.

Values (1 byte): An 8-bit unsigned integer that defines how the palette entry is to be used.
The Values field MUST be 0x00 or one of the values in the PaletteEntryFlag Enumeration
table.
Blue (1 byte): An 8-bit unsigned integer that defines the blue intensity value for the palette
entry.
Green (1 byte): An 8-bit unsigned integer that defines the green intensity value for the palette
entry.
Red (1 byte): An 8-bit unsigned integer that defines the red intensity value for the palette
entry.


"""
class PaletteEntry:
    def __init__(self):
        pass

"""
PitchAndFamily

The PitchAndFamily object specifies the pitch and family properties of a Font object (section
2.2.1.2). Pitch refers to the width of the characters, and family refers to the general appearance of a
font.

Family (4 bits): A property of a font that describes its general appearance. This MUST be a
value in the FamilyFont enumeration (section 2.1.1.8).
Pitch (2 bits): A property of a font that describes the pitch, of the characters. This MUST be a
value in the PitchFont enumeration (section 2.1.1.24).


"""
class PitchAndFamily:
    def __init__(self):
        pass

"""
The PointL Object defines the coordinates of a point.

x (4 bytes): A 32-bit signed integer that defines the horizontal (x) coordinate of the point.
y (4 bytes): A 32-bit signed integer that defines the vertical (y) coordinate of the point.

"""
class PointL:
    def __init__(self):
        pass


"""
The PointS Object defines the x- and y-coordinates of a point.

x (2 bytes): A 16-bit signed integer that defines the horizontal (x) coordinate of the point.
y (2 bytes): A 16-bit signed integer that defines the vertical (y) coordinate of the point.

"""
class PointS:
    def __init__(self):
        pass

"""
The PolyPolygon Object defines a series of closed polygons.

NumberOfPolygons (2 bytes): A 16-bit unsigned integer that defines the number of polygons
in the object.
aPointsPerPolygon (variable): A NumberOfPolygons array of 16-bit unsigned integers that
define the number of points for each polygon in the object.
aPoints (variable): An array of 16-bit unsigned integers that define the coordinates of the
polygons.

"""
class PolyPolygon:
    def __init__(self):
        pass

"""
The Rect Object defines a rectangle.

Left (2 bytes): A 16-bit signed integer that defines the x-coordinate, in logical coordinates, of
the upper-left corner of the rectangle
Top (2 bytes): A 16-bit signed integer that defines the y-coordinate, in logical coordinates, of
the upper-left corner of the rectangle.
Right (2 bytes): A 16-bit signed integer that defines the x-coordinate, in logical coordinates, of
the lower-right corner of the rectangle.
Bottom (2 bytes): A 16-bit signed integer that defines the y-coordinate, in logical coordinates,
of the lower-right corner of the rectangle.


"""
class Rect:
    def __init__(self):
        pass

"""
The RectL Object defines a rectangle.

Left (4 bytes): A 32-bit signed integer that defines the x coordinate, in logical coordinates, of
the upper-left corner of the rectangle.
Top (4 bytes): A 32-bit signed integer that defines the y coordinate, in logical coordinates, of
the upper-left corner of the rectangle.
Right (4 bytes): A 32-bit signed integer that defines the x coordinate, in logical coordinates, of
the lower-right corner of the rectangle.
Bottom (4 bytes): A 32-bit signed integer that defines y coordinate, in logical coordinates, of
the lower-right corner of the rectangle.

A rectangle defined with a RectL Object is filled up to— but not including—the right column and
bottom row of pixels.


"""
class RectL:
    def __init__(self):
        pass

"""
The RGBQuad Object defines the pixel color values in an uncompressed DIB.

Blue (1 byte): An 8-bit unsigned integer that defines the relative intensity of blue.
Green (1 byte): An 8-bit unsigned integer that defines the relative intensity of green.
Red (1 byte): An 8-bit unsigned integer that defines the relative intensity of red.
Reserved (1 byte): An 8-bit unsigned integer that MUST be 0x00.

"""
class RGBQuad:
    def __init__(self):
        pass

"""
The Scan Object specifies a collection of scanlines.

Count (2 bytes): A 16-bit unsigned integer that specifies the number of horizontal (x-axis)
coordinates in the ScanLines array. This value MUST be a multiple of 2, since left and right
endpoints are required to specify each scanline.
Top (2 bytes): A 16-bit unsigned integer that defines the vertical (y-axis) coordinate, in logical
units, of the top scanline.
Bottom (2 bytes): A 16-bit unsigned integer that defines the vertical (y-axis) coordinate, in
logical units, of the bottom scanline.

ScanLines (variable): An array of scanlines, each specified by left and right horizontal (x-axis)
                      coordinates of its endpoints.
    Left (2 bytes): A 16-bit unsigned integer that defines the horizontal (x-axis) coordinate,
    in logical units, of the left endpoint of the scanline.
    Right (2 bytes): A 16-bit unsigned integer that defines the horizontal (x-axis) coordinate,
    in logical units, of the right endpoint of the scanline.

Count2 (2 bytes): A 16-bit unsigned integer that MUST be the same as the value of the Count
field; it is present to allow upward travel in the structure.

"""
class Scan:
    def __init__(self):
        pass

"""
The SizeL Object defines the x- and y-extents of a rectangle.

cx (4 bytes): A 32-bit unsigned integer that defines the x-coordinate of the point.
cy (4 bytes): A 32-bit unsigned integer that defines the y-coordinate of the point.

"""
class SizeL:
    def __init__(self):
        pass
