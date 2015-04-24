#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
The Brush Object defines the style, color, and pattern of a brush. Brush Objects are created by the
META_CREATEBRUSHINDIRECT, META_CREATEPATTERNBRUSH and
META_DIBCREATEPATTERNBRUSH records.

BrushStyle (2 bytes): A 16-bit unsigned integer that defines the brush style. The value MUST
be an enumeration from the BrushStyle Enumeration table. For the meanings of the
different values, see the following table.
ColorRef (4 bytes): A 32-bit field that specifies how to interpret color values in the object
defined in the BrushHatch field. Its interpretation depends on the value of BrushStyle, as
explained in the following table.
BrushHatch (variable): A variable-size field that contains the brush hatch or pattern data. The
content depends on the value of BrushStyle, as explained below.
The BrushStyle field determines how the ColorRef and BrushHatch fields SHOULD be
interpreted, as specified in the following table.
The following table shows the relationship between the BrushStyle, ColorRef, and BrushHatch
fields in a Brush Object.

================ =========================================== ===================================
   BrushStyle                  ColorRef                                  BrushHatch
================ =========================================== ===================================
BS_SOLID          SHOULD be a ColorRef Object,                Not used, and SHOULD be ignored.
                  specified in section 2.2.2.8.               
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BS_NULL           SHOULD be ignored.                          Not used, and SHOULD be ignored.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BS_PATTERN        SHOULD be ignored.                          SHOULD be a Bitmap16 Object,
                                                              specified in section 2.2.2.1, which
                                                              defines the brush pattern.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BS_DIBPATTERNPT   SHOULD be a 32-bit ColorUsage               SHOULD be a DIB Object, specified in
                  Enumeration value, specified in section     section 2.2.2.9, which defines the
                  2.1.1.6; the low-order word specifies the   brush pattern.
                  meaning of color values in the DIB.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BS_HATCHED        SHOULD be a ColorRef Object, specified in   SHOULD be a 16-bit value from the
                  section 2.2.2.8.                            specified in section 2.1.1.12, which
                                                              defines the brush pattern.
================ =========================================== ===================================

"""
class Brush:
    def __init__(self, data):
        pass

"""
The Font object specifies the attributes of a logical font.

Height (2 bytes): A 16-bit signed integer that specifies the height, in logical units, of the font's
character cell. The character height is computed as the character cell height minus the
internal leading. The font mapper SHOULD interpret the height as follows.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|     Value      |        Meaning                                                                     |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| value < 0x0000 | The font mapper SHOULD transform this value into device units and match its        |
|                | absolute value against the character height of available fonts.                    |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|    0x0000      | A default height value MUST be used when creating a physical font.                 |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| 0x0000 < value | The font mapper SHOULD transform this value into device units and match it against |
|                | the cell height of available fonts.                                                |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
For all height comparisons, the font mapper SHOULD find the largest physical font that does
not exceed the requested size. <42>

Width (2 bytes): A 16-bit signed integer that defines the average width, in logical units, of
characters in the font. If Width is 0x0000, the aspect ratio of the device SHOULD be matched
against the digitization aspect ratio of the available fonts to find the closest match,
determined by the absolute value of the difference.
Escapement (2 bytes): A 16-bit signed integer that defines the angle, in tenths of degrees,
between the escapement vector and the x-axis of the device. The escapement vector is
parallel to the base line of a row of text.
Orientation (2 bytes): A 16-bit signed integer that defines the angle, in tenths of degrees,
between each character's base line and the x-axis of the device.
Weight (2 bytes): A 16-bit signed integer that defines the weight of the font in the range 0
through 1000. For example, 400 is normal and 700 is bold. If this value is 0x0000, a default
weight SHOULD be used.

Italic (1 byte): A 8-bit Boolean value that specifies the italic attribute of the font.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|     Value      |        Meaning                                                                     |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  False   0x00  | This is not an italic font.                                                        |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  True    0x01  | This is an italic font.                                                            |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Underline (1 byte): An 8-bit Boolean value that specifies the underline attribute of the font.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|     Value      |        Meaning                                                                     |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  False   0x00  | This is not an underline font.                                                     |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  True    0x01  | This is an underline font.                                                         |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

StrikeOut (1 byte): An 8-bit Boolean value that specifies the strikeout attribute of the font.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|     Value      |        Meaning                                                                     |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  False   0x00  | This is not a strikeout font.                                                      |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  True    0x01  | This is a strikeout font.                                                          |
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

CharSet (1 byte): An 8-bit unsigned integer that defines the character set. It SHOULD be set
to a value in the CharacterSet Enumeration (section 2.1.1.5).
The DEFAULT_CHARSET value MAY be used to allow the name and size of a font to fully
describe the logical font. If the specified font name does not exist, a font in another character
set MAY be substituted. The DEFAULT_CHARSET value is set to a value based on the current
system locale. For example, when the system locale is United States, it is set to
ANSI_CHARSET.
If a typeface name in the FaceName field is specified, the CharSet value MUST match the
character set of that typeface.
OutPrecision (1 byte): An 8-bit unsigned integer that defines the output precision. The output
precision defines how closely the output must match the requested font's height, width,
character orientation, escapement, pitch, and font type. It MUST be one of the values from
the OutPrecision Enumeration (section 2.1.1.21).
Applications can use the OUT_DEVICE_PRECIS, OUT_RASTER_PRECIS, OUT_TT_PRECIS, and
OUT_PS_ONLY_PRECIS values to control how the font mapper selects a font when the
operating system contains more than one font with a specified name. For example, if an
operating system contains a font named "Symbol" in raster and TrueType forms, specifying
OUT_TT_PRECIS forces the font mapper to select the TrueType version. Specifying
OUT_TT_ONLY_PRECIS forces the font mapper to select a TrueType font, even if it substitutes
a TrueType font of another name.
ClipPrecision (1 byte): An 8-bit unsigned integer that defines the clipping precision. The
clipping precision defines how to clip characters that are partially outside the clipping region.
It MUST be a combination of one or more of the bit settings in the ClipPrecision Flags
(section 2.1.2.1).
Quality (1 byte): An 8-bit unsigned integer that defines the output quality. The output quality
defines how carefully to attempt to match the logical font attributes to those of an actual
physical font. It MUST be one of the values in the FontQuality Enumeration (section
2.1.1.10).
PitchAndFamily (1 byte): A PitchAndFamily object (section 2.2.2.14) that defines the pitch
and the family of the font. Font families specify the look of fonts in a general way and are
intended for specifying fonts when the exact typeface wanted is not available.
Facename (variable): A null-terminated string of 8-bit Latin-1 [ISO/IEC-8859-1] ANSI
characters that specifies the typeface name of the font. The length of this string MUST NOT
exceed 32 8-bit characters, including the terminating null.

"""
class Font:
    def __init__(self, data):
        pass


"""
The Palette Object specifies the colors in a logical palette.

Start (2 bytes): A 16-bit unsigned integer that defines the offset into the Palette Object when
used with the META_SETPALENTRIES and META_ANIMATEPALETTE record types. When used
with META_CREATEPALETTE, it MUST be 0x0300.
NumberOfEntries (2 bytes): A 16-bit unsigned integer that defines the number of objects in
aPaletteEntries.
aPaletteEntries (variable): An array of NumberOfEntries 32-bit PaletteEntry Objects.


"""
class Palette:
    def __init__(self, data):
        pass

"""
The Pen Object specifies the style, width, and color of a pen.

PenStyle (2 bytes): A 16-bit unsigned integer that specifies the pen style. The value MUST be
defined from the PenStyle Enumeration table.
Width (4 bytes): A 32-bit PointS Object that specifies a point for the object dimensions. The x-
coordinate is the pen width. The y-coordinate is ignored.
ColorRef (4 bytes): A 32-bit ColorRef Object that specifies the pen color value.


"""
class Pen:
    def __init__(self, data):
        pass


"""
The Region Object defines a potentially non-rectilinear shape defined by an array of scanlines.

nextInChain (2 bytes): A value that MUST be ignored.<43>
ObjectType (2 bytes): A 16-bit signed integer that specifies the region identifier. It MUST be
0x0006.
ObjectCount (4 bytes): A value that MUST be ignored.<44>
RegionSize (2 bytes): A 16-bit signed integer that defines the size of the region in bytes plus
the size of aScans in bytes.
ScanCount (2 bytes): A 16-bit signed integer that defines the number of scanlines composing
the region.
maxScan (2 bytes): A 16-bit signed integer that defines the maximum number of points in any
one scan in this region.
BoundingRectangle (8 bytes): A Rect object (section 2.2.2.18) that defines the bounding
rectangle.
aScans (variable): An array of Scan objects (section 2.2.2.21) that define the scanlines in the
region.

"""
class Region:
    def __init__(self, data):
        pass

