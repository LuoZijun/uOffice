#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
The RecordType Enumeration defines the types of records that can be used in WMF metafiles.

typedef enum
{
    META_EOF = 0x0000,
    META_REALIZEPALETTE = 0x0035,
    META_SETPALENTRIES = 0x0037,
    META_SETBKMODE = 0x0102,
    META_SETMAPMODE = 0x0103,
    META_SETROP2 = 0x0104,
    META_SETRELABS = 0x0105,
    META_SETPOLYFILLMODE = 0x0106,
    META_SETSTRETCHBLTMODE = 0x0107,
    META_SETTEXTCHAREXTRA = 0x0108,
    META_RESTOREDC = 0x0127,
    META_RESIZEPALETTE = 0x0139,
    META_DIBCREATEPATTERNBRUSH = 0x0142,
    META_SETLAYOUT = 0x0149,
    META_SETBKCOLOR = 0x0201,
    META_SETTEXTCOLOR = 0x0209,
    META_OFFSETVIEWPORTORG = 0x0211,
    META_LINETO = 0x0213,
    META_MOVETO = 0x0214,
    META_OFFSETCLIPRGN = 0x0220,
    META_FILLREGION = 0x0228,
    META_SETMAPPERFLAGS = 0x0231,
    META_SELECTPALETTE = 0x0234,
    META_POLYGON = 0x0324,
    META_POLYLINE = 0x0325,
    META_SETTEXTJUSTIFICATION = 0x020A,
    META_SETWINDOWORG = 0x020B,
    META_SETWINDOWEXT = 0x020C,
    META_SETVIEWPORTORG = 0x020D,
    META_SETVIEWPORTEXT = 0x020E,
    META_OFFSETWINDOWORG = 0x020F,
    META_SCALEWINDOWEXT = 0x0410,
    META_SCALEVIEWPORTEXT = 0x0412,
    META_EXCLUDECLIPRECT = 0x0415,
    META_INTERSECTCLIPRECT = 0x0416,
    META_ELLIPSE = 0x0418,
    META_FLOODFILL = 0x0419,
    META_FRAMEREGION = 0x0429,
    META_ANIMATEPALETTE = 0x0436,
    META_TEXTOUT = 0x0521,
    META_POLYPOLYGON = 0x0538,
    META_EXTFLOODFILL = 0x0548,
    META_RECTANGLE = 0x041B,
    META_SETPIXEL = 0x041F,
    META_ROUNDRECT = 0x061C,
    META_PATBLT = 0x061D,
    META_SAVEDC = 0x001E,
    META_PIE = 0x081A,
    META_STRETCHBLT = 0x0B23,
    META_ESCAPE = 0x0626,
    META_INVERTREGION = 0x012A,
    META_PAINTREGION = 0x012B,
    META_SELECTCLIPREGION = 0x012C,
    META_SELECTOBJECT = 0x012D,
    META_SETTEXTALIGN = 0x012E,
    META_ARC = 0x0817,
    META_CHORD = 0x0830,
    META_BITBLT = 0x0922,
    META_EXTTEXTOUT = 0x0a32,
    META_SETDIBTODEV = 0x0d33,
    META_DIBBITBLT = 0x0940,
    META_DIBSTRETCHBLT = 0x0b41,
    META_STRETCHDIB = 0x0f43,
    META_DELETEOBJECT = 0x01f0,
    META_CREATEPALETTE = 0x00f7,
    META_CREATEPATTERNBRUSH = 0x01F9,
    META_CREATEPENINDIRECT = 0x02FA,
    META_CREATEFONTINDIRECT = 0x02FB,
    META_CREATEBRUSHINDIRECT = 0x02FC,
    META_CREATEREGION = 0x06FF
} RecordType;

META_EOF: This record specifies the end of the file, the last record in the metafile.
META_REALIZEPALETTE: This record maps entries from the logical palette that is defined in
the playback device context to the system palette.
META_SETPALENTRIES: This record defines red green blue (RGB) color values in a range of
entries in the logical palette that is defined in the playback device context.
META_SETBKMODE: This record defines the background raster operation mix mode in the
playback device context. The background mix mode is the mode for combining pens, text,
hatched brushes, and interiors of filled objects with background colors on the output surface.
META_SETMAPMODE: This record defines the mapping mode in the playback device context.
The mapping mode defines the unit of measure used to transform page-space coordinates
into coordinates of the output device, and also defines the orientation of the device's x and y
axes.

META_SETROP2: This record defines the foreground raster operation mix mode in the playback
device context. The foreground mix mode is the mode for combining pens and interiors of
filled objects with foreground colors on the output surface.
META_SETRELABS: This record is undefined and MUST be ignored.
META_SETPOLYFILLMODE: This record defines polygon fill mode in the playback device
context for graphics operations that fill polygons.
META_SETSTRETCHBLTMODE: This record defines the bitmap stretching mode in the
playback device context.
META_SETTEXTCHAREXTRA: This record defines inter-character spacing for text justification
in the playback device context. Spacing is added to the white space between each character,
including break characters, when a line of justified text is output.
META_RESTOREDC: This record restores the playback device context from a previously saved
device context.
META_RESIZEPALETTE: This record redefines the size of the logical palette that is defined in
the playback device context.
META_DIBCREATEPATTERNBRUSH: This record defines a brush with a pattern specified by a
device-independent bitmap (DIB).
META_SETLAYOUT: This record defines the layout orientation in the playback device context.
<4>
META_SETBKCOLOR: This record sets the background color in the playback device context to a
specified color, or to the nearest physical color if the device cannot represent the specified
color.
META_SETTEXTCOLOR: This record defines the text color in the playback device context.
META_OFFSETVIEWPORTORG: This record moves the viewport origin in the playback device
context by using specified horizontal and vertical offsets.
META_LINETO: This record draws a line from the output position that is defined in the playback
device context up to, but not including, a specified point.
META_MOVETO: This record sets the output position in the playback device context to a
specified point.
META_OFFSETCLIPRGN: This record moves the clipping region that is defined in the playback
device context by specified offsets.
META_FILLREGION: This record fills a region by using a specified brush.
META_SETMAPPERFLAGS: This record defines the algorithm that the font mapper uses when
it maps logical fonts to physical fonts.
META_SELECTPALETTE: This record specifies the logical palette in the playback device
context.
META_POLYGON: This record paints a polygon consisting of two or more vertices connected by
straight lines. The polygon is outlined by using the pen and filled by using the brush and
polygon fill mode; these are defined in the playback device context.

META_POLYLINE: This record draws a series of line segments by connecting the points in a
specified array.
META_SETTEXTJUSTIFICATION: This record defines the amount of space to add to break
characters in a string of justified text.
META_SETWINDOWORG: This record defines the output window origin in the playback device
context.
META_SETWINDOWEXT: This record defines the horizontal and vertical extents of the output
window in the playback device context.
META_SETVIEWPORTORG: This record defines the viewport origin in the playback device
context.
META_SETVIEWPORTEXT: This record defines the horizontal and vertical extents of the
viewport in the playback device context.
META_OFFSETWINDOWORG: This record moves the output window origin in the playback
device context by using specified horizontal and vertical offsets.
META_SCALEWINDOWEXT: This record scales the horizontal and vertical extents of the output
window that is defined in the playback device context by using the ratios formed by specified
multiplicands and divisors.
META_SCALEVIEWPORTEXT: This record scales the horizontal and vertical extents of the
viewport that is defined in the playback device context by using the ratios formed by specified
multiplicands and divisors.
META_EXCLUDECLIPRECT: This record sets the clipping region that is defined in the playback
device context to the existing clipping region minus a specified rectangle.
META_INTERSECTCLIPRECT: This record sets the clipping region that is defined in the
playback device context to the intersection of the existing clipping region and a specified
rectangle.
META_ELLIPSE: This record defines an ellipse. The center of the ellipse is the center of a
specified bounding rectangle. The ellipse is outlined by using the pen and is filled by using the
brush; these are defined in the playback device context.
META_FLOODFILL: This record fills an area of the display surface with the brush that is defined
in the playback device context.
META_FRAMEREGION: This record defines a border around a specified region by using a
specified brush.
META_ANIMATEPALETTE: This record redefines entries in the logical palette that is defined in
the playback device context.
META_TEXTOUT: This record outputs a character string at a specified location using the font,
background color, and text color; these are defined in the playback device context.
META_POLYPOLYGON: This record paints a series of closed polygons. Each polygon is outlined
by using the pen and filled by using the brush and polygon fill mode; these are defined in the
playback device context. The polygons drawn in this operation can overlap.
META_EXTFLOODFILL: This record fills an area with the brush that is defined in the playback
device context.

META_RECTANGLE: This record paints a rectangle. The rectangle is outlined by using the pen
and filled by using the brush; these are defined in the playback device context.
META_SETPIXEL: This record sets the pixel at specified coordinates to a specified color.
META_ROUNDRECT: This record draws a rectangle with rounded corners. The rectangle is
outlined by using the current pen and filled by using the current brush.
META_PATBLT: This record paints the specified rectangle by using the brush that is currently
selected into the playback device context. The brush color and the surface color or colors are
combined using the specified raster operation.
META_SAVEDC: This record saves the playback device context for later retrieval.
META_PIE: This record draws a pie-shaped wedge bounded by the intersection of an ellipse and
two radials. The pie is outlined by using the pen and filled by using the brush; these are
defined in the playback device context.
META_STRETCHBLT: This record specifies the transfer of a block of pixels according to a raster
operation, with possible expansion or contraction.
META_ESCAPE: This record makes it possible to access capabilities of a particular printing
device that are not directly available through other WMF records.
META_INVERTREGION: This record inverts the colors in a specified region.
META_PAINTREGION: This record paints a specified region by using the brush that is defined
in the playback device context.
META_SELECTCLIPREGION: This record specifies the clipping region in the playback device
context.
META_SELECTOBJECT: This record specifies a graphics object in the playback device context.
The new object replaces the previous object of the same type, if one is defined.
META_SETTEXTALIGN: This record defines the text-alignment values in the playback device
context.
META_ARC: This record draws an elliptical arc.
META_CHORD: This record draws a chord, which is a region bounded by the intersection of an
ellipse and a line segment. The chord is outlined by using the pen and filled by using the
brush; these are defined in the playback device context.
META_BITBLT: This record specifies the transfer of a block of pixels according to a raster
operation.
META_EXTTEXTOUT: This record outputs a character string by using the font, background
color, and text color; these are defined in the playback device context. Optionally, dimensions
can be provided for clipping, opaquing, or both.
META_SETDIBTODEV: This record sets a block of pixels using device-independent color data.
META_DIBBITBLT: This record specifies the transfer of a block of pixels in device-independent
format according to a raster operation.
META_DIBSTRETCHBLT: This record specifies the transfer of a block of pixels in device-
independent format according to a raster operation, with possible expansion or contraction.

META_STRETCHDIB: This record specifies the transfer of color data from a block of pixels in
device-independent format according to a raster operation, with possible expansion or
contraction.
META_DELETEOBJECT: This record deletes a graphics object, which can be a pen, brush, font,
region, or palette.
META_CREATEPALETTE: This record defines a logical palette.
META_CREATEPATTERNBRUSH: This record defines a brush with a pattern specified by a DIB.
META_CREATEPENINDIRECT: This record defines a pen with specified style, width, and color.
META_CREATEFONTINDIRECT: This record defines a font with specified characteristics.
META_CREATEBRUSHINDIRECT: This record defines a brush with specified style, color, and
pattern.
META_CREATEREGION: This record defines a region.
The high-order byte of the WMF record type values MAY <5> be ignored for all record types except
the following.
META_BITBLT
META_DIBBITBLT
META_DIBSTRETCHBLT
META_POLYGON
META_POLYLINE
META_SETPALENTRIES
META_STRETCHBLT
The meanings of the high-order bytes of these record type fields are specified in the respective
sections that define them.
A record type is not defined for the WMF Header record, because only one can be present as the
first record in the metafile.


"""

"""
# TODO: Need Update record function table.
Record Functions table:
    META_EOF = 0x0000,     # Control Record Types
    META_REALIZEPALETTE = 0x0035,
    META_SETPALENTRIES = 0x0037,
    META_SETBKMODE = 0x0102,
    META_SETMAPMODE = 0x0103,
    META_SETROP2 = 0x0104,
    META_SETRELABS = 0x0105,
    META_SETPOLYFILLMODE = 0x0106,
    META_SETSTRETCHBLTMODE = 0x0107,
    META_SETTEXTCHAREXTRA = 0x0108,
    META_RESTOREDC = 0x0127,
    META_RESIZEPALETTE = 0x0139,
    META_DIBCREATEPATTERNBRUSH = 0x0142,
    META_SETLAYOUT = 0x0149,
    META_SETBKCOLOR = 0x0201,
    META_SETTEXTCOLOR = 0x0209,
    META_OFFSETVIEWPORTORG = 0x0211,
    META_LINETO = 0x0213,
    META_MOVETO = 0x0214,
    META_OFFSETCLIPRGN = 0x0220,
    META_FILLREGION = 0x0228,
    META_SETMAPPERFLAGS = 0x0231,

    META_SELECTPALETTE = 0x0234,
    META_POLYGON = 0x0324,
    META_POLYLINE = 0x0325,
    META_SETTEXTJUSTIFICATION = 0x020A,
    META_SETWINDOWORG = 0x020B,
    META_SETWINDOWEXT = 0x020C,
    META_SETVIEWPORTORG = 0x020D,
    META_SETVIEWPORTEXT = 0x020E,
    META_OFFSETWINDOWORG = 0x020F,
    META_SCALEWINDOWEXT = 0x0410,
    META_SCALEVIEWPORTEXT = 0x0412,

    # Part 2
    META_EXCLUDECLIPRECT = 0x0415,
    META_INTERSECTCLIPRECT = 0x0416,
    META_ELLIPSE = 0x0418,
    META_FLOODFILL = 0x0419,
    META_FRAMEREGION = 0x0429,
    META_ANIMATEPALETTE = 0x0436,
    META_TEXTOUT = 0x0521,
    META_POLYPOLYGON = 0x0538,
    META_EXTFLOODFILL = 0x0548,
    META_RECTANGLE = 0x041B,
    META_SETPIXEL = 0x041F,
    META_ROUNDRECT = 0x061C,
    META_PATBLT = 0x061D,
    META_SAVEDC = 0x001E,
    META_PIE = 0x081A,
    META_STRETCHBLT = 0x0B23,
    META_ESCAPE = 0x0626,
    META_INVERTREGION = 0x012A,
    META_PAINTREGION = 0x012B,
    META_SELECTCLIPREGION = 0x012C,
    META_SELECTOBJECT = 0x012D,
    META_SETTEXTALIGN = 0x012E,
    META_ARC = 0x0817,
    META_CHORD = 0x0830,
    META_BITBLT = 0x0922,
    META_EXTTEXTOUT = 0x0a32,
    META_SETDIBTODEV = 0x0d33,
    META_DIBBITBLT = 0x0940,
    META_DIBSTRETCHBLT = 0x0b41,
    META_STRETCHDIB = 0x0f43,
    META_DELETEOBJECT = 0x01f0,
    META_CREATEPALETTE = 0x00f7,
    META_CREATEPATTERNBRUSH = 0x01F9,
    META_CREATEPENINDIRECT = 0x02FA,
    META_CREATEFONTINDIRECT = 0x02FB,
    META_CREATEBRUSHINDIRECT = 0x02FC,
    META_CREATEREGION = 0x06FF
    
"""


"""
Bitmap Record Types
Control Record Types
Drawing Record Types
Object Record Types
State Record Types
Escape Record Types

"""

import wmf.Records.bitmap
import wmf.Records.control
import wmf.Records.drawing
import wmf.Records.escape
import wmf.Records.state
import wmf.Records.object

Record_Types = {
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

