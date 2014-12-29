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
Contents:

2.3 WMF Records ..................................................................................................... 107



2.3.1 Bitmap Record Types ..................................................................................... 108
2.3.1.1 META_BITBLT Record ............................................................................... 109
2.3.1.1.1 With Bitmap ...................................................................................... 110
2.3.1.1.2 Without Bitmap .................................................................................. 110
2.3.1.2 META_DIBBITBLT Record .......................................................................... 111
2.3.1.2.1 With Bitmap ...................................................................................... 112
2.3.1.2.2 Without Bitmap .................................................................................. 113
2.3.1.3 META_DIBSTRETCHBLT Record ................................................................. 113
2.3.1.3.1 With Bitmap ...................................................................................... 114
2.3.1.3.2 Without Bitmap .................................................................................. 115
2.3.1.4 META_SETDIBTODEV Record ..................................................................... 116
2.3.1.5 META_STRETCHBLT Record ....................................................................... 117
2.3.1.5.1 With Bitmap ...................................................................................... 118
2.3.1.5.2 Without Bitmap .................................................................................. 119
2.3.1.6 META_STRETCHDIB Record ....................................................................... 120

2.3.2 Control Record Types ..................................................................................... 122
2.3.2.1 META_EOF Record ................................................................................... 122
2.3.2.2 META_HEADER Record ............................................................................. 122
2.3.2.3 META_PLACEABLE Record ......................................................................... 123

2.3.3 Drawing Record Types ................................................................................... 124
2.3.3.1 META_ARC Record ................................................................................... 125
2.3.3.2 META_CHORD Record ............................................................................... 126
2.3.3.3 META_ELLIPSE Record.............................................................................. 127
2.3.3.4 META_EXTFLOODFILL Record .................................................................... 128
2.3.3.5 META_EXTTEXTOUT Record ...................................................................... 128
2.3.3.6 META_FILLREGION Record ........................................................................ 129
2.3.3.7 META_FLOODFILL Record ......................................................................... 130
2.3.3.8 META_FRAMEREGION Record .................................................................... 131
2.3.3.9 META_INVERTREGION Record ................................................................... 131
2.3.3.10 META_LINETO Record ............................................................................. 132
2.3.3.11 META_PAINTREGION Record ................................................................... 133
2.3.3.12 META_PATBLT Record ............................................................................. 133
2.3.3.13 META_PIE Record .................................................................................. 134
2.3.3.14 META_POLYLINE Record ......................................................................... 135
2.3.3.15 META_POLYGON Record.......................................................................... 135
2.3.3.16 META_POLYPOLYGON Record .................................................................. 136
2.3.3.17 META_RECTANGLE Record ...................................................................... 137
2.3.3.18 META_ROUNDRECT Record ..................................................................... 137
2.3.3.19 META_SETPIXEL Record .......................................................................... 138
2.3.3.20 META_TEXTOUT Record .......................................................................... 139

2.3.4 Object Record Types ...................................................................................... 139
2.3.4.1 META_CREATEBRUSHINDIRECT Record ...................................................... 140
2.3.4.2 META_CREATEFONTINDIRECT Record ........................................................ 141
2.3.4.3 META_CREATEPALETTE Record .................................................................. 142
2.3.4.4 META_CREATEPATTERNBRUSH Record ....................................................... 142
2.3.4.5 META_CREATEPENINDIRECT Record .......................................................... 144
2.3.4.6 META_CREATEREGION Record................................................................... 144
2.3.4.7 META_DELETEOBJECT Record ................................................................... 145
2.3.4.8 META_DIBCREATEPATTERNBRUSH Record .................................................. 145
2.3.4.9 META_SELECTCLIPREGION Record ............................................................. 146
2.3.4.10 META_SELECTOBJECT Record .................................................................. 147
2.3.4.11 META_SELECTPALETTE Record ................................................................ 147

2.3.5 State Record Types ....................................................................................... 148
2.3.5.1 META_ANIMATEPALETTE Record ................................................................ 150
2.3.5.2 META_EXCLUDECLIPRECT Record .............................................................. 150
2.3.5.3 META_INTERSECTCLIPRECT Record ........................................................... 151
2.3.5.4 META_MOVETO Record ............................................................................. 152
2.3.5.5 META_OFFSETCLIPRGN Record .................................................................. 152
2.3.5.6 META_OFFSETVIEWPORTORG Record ......................................................... 153
2.3.5.7 META_OFFSETWINDOWORG Record ........................................................... 153
2.3.5.8 META_REALIZEPALETTE Record ................................................................. 154
2.3.5.9 META_RESIZEPALETTE Record .................................................................. 154
2.3.5.10 META_RESTOREDC Record ...................................................................... 154
2.3.5.11 META_SAVEDC Record ............................................................................ 155
2.3.5.12 META_SCALEVIEWPORTEXT Record.......................................................... 155
2.3.5.13 META_SCALEWINDOWEXT Record ............................................................ 156
2.3.5.14 META_SETBKCOLOR Record .................................................................... 157
2.3.5.15 META_SETBKMODE Record ..................................................................... 157
2.3.5.16 META_SETLAYOUT Record ....................................................................... 158
2.3.5.17 META_SETMAPMODE Record ................................................................... 158
2.3.5.18 META_SETMAPPERFLAGS Record ............................................................. 159
2.3.5.19 META_SETPALENTRIES Record ................................................................ 159
2.3.5.20 META_SETPOLYFILLMODE Record ............................................................ 160
2.3.5.21 META_SETRELABS Record ....................................................................... 161
2.3.5.22 META_SETROP2 Record .......................................................................... 161
2.3.5.23 META_SETSTRETCHBLTMODE Record ....................................................... 162
2.3.5.24 META_SETTEXTALIGN Record .................................................................. 162
2.3.5.25 META_SETTEXTCHAREXTRA Record.......................................................... 163
2.3.5.26 META_SETTEXTCOLOR Record ................................................................. 163
2.3.5.27 META_SETTEXTJUSTIFICATION Record ..................................................... 164
2.3.5.28 META_SETVIEWPORTEXT Record ............................................................. 164
2.3.5.29 META_SETVIEWPORTORG Record ............................................................ 165
2.3.5.30 META_SETWINDOWEXT Record ............................................................... 165
2.3.5.31 META_SETWINDOWORG Record .............................................................. 166

2.3.6 Escape Record Types ..................................................................................... 166
2.3.6.1 META_ESCAPE Record .............................................................................. 169
2.3.6.2 ABORTDOC Record .................................................................................. 169
2.3.6.3 BEGIN_PATH Record ................................................................................ 170
2.3.6.4 CHECK_JPEGFORMAT Record .................................................................... 170
2.3.6.5 CHECK_PNGFORMAT Record ..................................................................... 171
2.3.6.6 CLIP_TO_PATH Record ............................................................................. 172
2.3.6.7 CLOSE_CHANNEL Record .......................................................................... 172
2.3.6.8 DOWNLOAD_FACE Record ........................................................................ 173
2.3.6.9 DOWNLOAD_HEADER Record .................................................................... 174
2.3.6.10 DRAW_PATTERNRECT Record .................................................................. 174
2.3.6.11 ENCAPSULATED_POSTSCRIPT Record ....................................................... 175
2.3.6.12 END_PATH Record ................................................................................. 176
2.3.6.13 ENDDOC Record .................................................................................... 177
2.3.6.14 EPS_PRINTING Record............................................................................ 177
2.3.6.15 EXTTEXTOUT Record .............................................................................. 178
2.3.6.16 GET_COLORTABLE Record ....................................................................... 178
2.3.6.17 GET_DEVICEUNITS Record...................................................................... 180
2.3.6.18 GET_EXTENDED_TEXTMETRICS Record .................................................... 180
2.3.6.19 GET_FACENAME Record .......................................................................... 181
2.3.6.20 GET_PAIRKERNTABLE Record .................................................................. 181
2.3.6.21 GET_PHYSPAGESIZE Record .................................................................... 182
2.3.6.22 GET_PRINTINGOFFSET Record ................................................................ 182
2.3.6.23 GET_PS_FEATURESETTING Record........................................................... 183
2.3.6.24 GET_SCALINGFACTOR Record ................................................................. 183
2.3.6.25 META_ESCAPE_ENHANCED_METAFILE Record ........................................... 184
2.3.6.26 METAFILE_DRIVER Record ...................................................................... 186
2.3.6.27 NEWFRAME Record ................................................................................ 186
2.3.6.28 NEXTBAND Record ................................................................................. 187
2.3.6.29 PASSTHROUGH Record ........................................................................... 187
2.3.6.30 POSTSCRIPT_DATA Record ..................................................................... 188
2.3.6.31 POSTSCRIPT_IDENTIFY Record ................................................................ 188
2.3.6.32 POSTSCRIPT_IGNORE Record .................................................................. 189
2.3.6.33 POSTSCRIPT_INJECTION Record .............................................................. 190
2.3.6.34 POSTSCRIPT_PASSTHROUGH Record ....................................................... 190
2.3.6.35 OPEN_CHANNEL Record .......................................................................... 191
2.3.6.36 QUERY_DIBSUPPORT Record ................................................................... 191
2.3.6.37 QUERY_ESCSUPPORT Record .................................................................. 192
2.3.6.38 SET_COLORTABLE Record ....................................................................... 193
2.3.6.39 SET_COPYCOUNT Record ........................................................................ 193
2.3.6.40 SET_LINECAP Record ............................................................................. 194
2.3.6.41 SET_LINEJOIN Record ............................................................................ 195
2.3.6.42 SET_MITERLIMIT Record......................................................................... 195
2.3.6.43 SPCLPASSTHROUGH2 Record .................................................................. 196
2.3.6.44 STARTDOC Record ................................................................................. 197


Bitmap Record Types
Control Record Types
Drawing Record Types
Object Record Types
State Record Types
Escape Record Types

"""

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

