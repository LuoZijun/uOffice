微软DOCX格式分析
=================

:Date: 2014/12/25
:Author: Luo Zijun


.. contents::


实现优先级
-----------------

*   Windows Metafile Format(WMF)  难度: 3
*   Enhanced Metafile Format(EMF)  难度: 8
*   Math Mark Luanage(MathML)  难度: 1



Windows Metafile Format(WMF)
----------------------------------------------

在 Windows Office 早期版本 以及 金山公司开发的WPS( Office个人版本: 9.1.0.4879 )中，对于 数学公式的编辑、渲染及呈现是采用微软一种早期(Microsoft Windows 3.0开始引入, 16位元的标准)的向量图格式 ( `WMF(维基百科) <https://zh.wikipedia.org/wiki/WMF>`_ ) 。WMF格式类似与印刷业广泛使用的PostScript格式(由 Adobe 开发)。

WMF协议: `[MS-WMF]: Windows Metafile Format <http://msdn.microsoft.com/en-us/library/cc250370.aspx>`_

`WMF(维基百科) <https://zh.wikipedia.org/wiki/WMF>`_ 

Windows Metafile 规范 第三方通俗介绍: 

*   http://wvware.sourceforge.net/caolan/ora-wmf.html
*   http://wvware.sourceforge.net/caolan/

WMF 解析及转换库:

*   `libwmf <http://wvware.sourceforge.net/libwmf.html>`_ 支持渲染及转换 WMF 格式文件至 SVG/EPS/FIG/F2X
*   `python-uniconvertor <http://sk1project.org/modules.php?name=Products&product=uniconvertor&op=download>`_ 试用失败 ...
*   `python-hachoir-metadata <https://pypi.python.org/pypi/hachoir-metadata/1.2.1>`_

**安全:**

WMF文件格式漏洞: https://zh.wikipedia.org/wiki/WMF%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F%E6%BC%8F%E6%B4%9E

Structure(结构)
^^^^^^^^^^^^^^^^

The WMF specifies structures for defining a graphical image. A WMF metafile contains drawing commands, property definitions, and graphics objects in a series of WMF records. In effect, a WMF metafile is a digital recording of an image, and the recording can be played back to reproduce that image. Because WMF metafiles are application-independent, they can be shared among applications and used for image storage.

Original WMF metafiles were device-specific; that is, the graphical images they contained would only be rendered correctly if played back on the output device for which they were recorded. To overcome this limitation, "placeable" WMF metafiles were developed, which contain an extension to the standard header with information about the placement and scaling of the image.

The following figure illustrates the high-level structures of the original and placeable forms of WMF metafile.

==================================== = ==============================================
WMF Header Record(头部信息)            WMF Placeable Header Record
WMF Record(常规纪录)                   WMF Header Record
...                                    WMF Record
WMF Record                             ...
WMF End-of-File Record(结束标识信息)   WMF Record
\                                      WMF End-of-File Record
==================================== = ==============================================


Control Record Types (控制性纪录的类型)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This section defines the Windows Metafile Format (WMF) Control Record Types, which specify records that begin and end a WMF metafile.
The following are the Control Record Types:

=============   ========    ==========================================
Name            Section     Description
=============   ========    ==========================================
Meta_header     2.3.2.1     Specifies The Start Of A Wmf Metafile.
Meta_eof        2.3.2.2     Specifies The End Of A Wmf Metafile.
=============   ========    ==========================================

Header Record (头部纪录格式)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The WMF header record, including:

*   The type of metafile
*   The version of metafile
*   The size of the metafile
*   The number of objects defined in the metafile
*   The size of the largest single record in the metafile

META_HEADER Record:

The Windows Metafile Format META_HEADER record is the first record in a standard WMF metafile.


+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| | | | | | | | | | |1| | | | | | | | | |2| | | | | | | | | |3| |
|0|1|2|3|4|5|6|7|8|9|0|1|2|3|4|5|6|7|8|9|0|1|2|3|4|5|6|7|8|9|0|1|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                 Type          |          HeaderSize           |
+-------------------------------+-------------------------------+
|                 Version       |          SizeLow              |
+-------------------------------+-------------------------------+
|                 SizeHight     |          NumberOfObjects      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            MaxRecord                          |
+-------------------------------+-------------------------------+
|         NumberOfMembers       |                               |
+-------------------------------+-------------------------------+



*Type (2 bytes):* A 16-bit unsigned integer that defines the type of metafile. It MUST be a value in the MetafileType Enumeration table.

        MEMORYMETAFILE = 0x0001
        DISKMETAFILE = 0x0002
        MEMORYMETAFILE: Metafile is stored in memory.
        DISKMETAFILE: Metafile is stored on disk.


*HeaderSize (2 bytes):* A 16-bit unsigned integer that defines the number of 16-bit words in the header.

*Version (2 bytes):* A 16-bit unsigned integer that defines the metafile version. It MUST be a value in the MetafileVersion Enumeration table.

        METAVERSION100 = 0x0100
        METAVERSION300 = 0x0300
        
        METAVERSION100: DIBs are not supported.
        METAVERSION300: DIBs are supported.


*SizeLow (2 bytes):* A 16-bit unsigned integer that defines the low-order word of the number of 16-bit words in the entire metafile.

*SizeHigh (2 bytes):* A 16-bit unsigned integer that defines the high-order word of the number of 16-bit words in the entire metafile.
一个16位无符号(unsigned integer)的整数  定义 high-order(高序位?)字符 在 16 位词的整个图元文件。

*NumberOfObjects (2 bytes):* A 16-bit unsigned integer that specifies the number of graphics objects that are defined in the entire metafile. These objects include brushes, pens and all the other fixed-length and variable-length objects specified in sections 2.2.1 and 2.2.2 .

*MaxRecord (4 bytes):* A 32-bit unsigned integer that specifies the size of the largest record used in the metafile (in 16-bit elements).

*NumberOfMembers (2 bytes):* A 16-bit unsigned integer that is not used. It SHOULD be 0x0000.


Generic Record (常规纪录格式)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WMF records have a generic format, the following information:

*   The record size
*   The record function
*   Parameters, if any, for the record function

All WMF metafiles are terminated by a WMF end-of-file record.

所有的 WMF 元文件 必须在 一个 WMF 结束纪录处终结。


End-of-File Record ( 结束标识纪录 )
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

META_EOF Record:

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| | | | | | | | | | |1| | | | | | | | | |2| | | | | | | | | |3| |
|0|1|2|3|4|5|6|7|8|9|0|1|2|3|4|5|6|7|8|9|0|1|2|3|4|5|6|7|8|9|0|1|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            RecordSize                         |
+-------------------------------+-------------------------------+
|       RecordFunction          |                               |
+-------------------------------+-------------------------------+


*RecordSize (4 bytes):* A 32-bit unsigned integer that defines the number of 16-bit WORDs in the record.

*RecordFunction (2 bytes):* A 16-bit unsigned integer that defines the type of this record. For META_EOF, this value MUST be 0x0000, as specified in the RecordType Enumeration table.

META_PLACEABLE Record
~~~~~~~~~~~~~~~~~~~~~~~
The META_PLACEABLE record is the first record in a placeable WMF metafile, which is an extension
to the WMF metafile format.<58> The information in this extension allows the specification of the
placement and size of the target image, which makes it adaptable to different output devices.
The META_PLACEABLE record MUST be the first record of the metafile, located immediately before
the META_HEADER record (section 2.3.2.2).



Enhanced Metafile Format(EMF)
----------------------------------------------

在 Windows NT推出时，微软又推出一个32位元的加强版标准，称之为Enhanced Metafile（简称 `EMF(维基百科) <https://zh.wikipedia.org/wiki/WMF#.E6.AD.B7.E5.8F.B2>`_ ）。

EMF维基百科介绍: `EMF维基百科 <https://zh.wikipedia.org/wiki/WMF#.E6.AD.B7.E5.8F.B2>`_

EMF协议: `[MS-EMF]: Enhanced Metafile Format <http://msdn.microsoft.com/en-us/library/cc230514.aspx>`_ 

EMF插件扩展协议: `[MS-EMFPLUS]: Enhanced Metafile Format Plus Extensions <http://msdn.microsoft.com/en-us/library/cc230724.aspx>`_

EMSF协议: `[MS-EMFSPOOL]: Enhanced Metafile Spool Format <http://msdn.microsoft.com/en-us/library/cc231034.aspx>`_


EMF 解析及转换库:

*   `libemf <http://libemf.sourceforge.net/>`_ libEMF is a C/C++ library which provides a drawing toolkit based on ECMA-234.
*   `pyemf <http://sourceforge.net/projects/pyemf/>`_ Pure Python library for Enhanced Metafile (.emf) ECMA-234 compliant scalable graphics files. (支持编辑 EMF 但是不支持渲染它)
*   `python-hachoir-metadata <https://pypi.python.org/pypi/hachoir-metadata/1.2.1>`_ ( 支持 WMF/EMF/TIFF/XCF/CUR/ICO/BMP/PCX )


Math Mark Luanage(MathML)
-------------------------------------------

在 Windows Office 2010 当中，经过测试，微软Office中的数学公式在 Word XML 树中的描述已经由 向量图 资源链接 更换成了 `MathML <https://developer.mozilla.org/zh-CN/docs/Web/MathML>`_ 标记语言，与 XML结合在一起。这意味着该数学公式的再次编辑将变得更加方便和简单。

*   `维基百科 <https://en.wikipedia.org/wiki/MathML>`_ 
*   `描述数学表达式 <http://www.ibm.com/developerworks/cn/xml/x-mathml/index.html>`_ 


Object Linking and Embedding(OLE)
----------------------------------------------------

Object Linking and Embedding:  `OLE维基百科介绍 <http://en.wikipedia.org/wiki/Object_Linking_and_Embedding>`_ (英文)

对象连接与嵌入: `对象连接与嵌入维基百科介绍 <http://zh.wikipedia.org/wiki/%E5%AF%B9%E8%B1%A1%E8%BF%9E%E6%8E%A5%E4%B8%8E%E5%B5%8C%E5%85%A5>`_ (中文简体)


笔记
--------

.. Note::

    Python 对于 WMF 格式的解析库 `python-uniconvertor <http://sk1project.org/modules.php?name=Products&product=uniconvertor&op=download>`_ 并不能解析 经过 WPS 或者 Windows Office 生产的 WMF 向量图。
    
    经查过 uniconvertor 代码，发现是因为 uniconvertor 在检查 WMF 格式文件的 Magic Number ( Header )时，发现并不与 `\xd7\xcd\xc6\x9a` 相符。
    
    初步在查看 `Windows Metafile Format(wmf) Specification` ，发现 规范里面并没有规定 WMF 格式的 Header 为 `\xd7\xcd\xc6\x9a` 。
    
    可以在 GIMP 软件里面打开并被正常查看的 WMF 格式图片 的 Header 经查看 也并非为 `\xd7\xcd\xc6\x9a` ，而是 `\x01\x00\t\x00` 。在 GIMP 里面无法进行查看的 WMF 向量图 Header 为 `\x01\x00\x00\x00`  。


libwmf 项目始于 2000 年之前，最近一次对 反馈的 处理是在 2008年11月。该项目的成员 有来自 Abiword 以及 PrefectWord 的成员, 似乎没有新鲜血液。

libwmf 对于 极个别的 WMF 格式向量图 无法渲染及转换(Magic Number 无法被识别)。经过测试，确实发现可以被识别的 WMF 向量图 与 不可以被识别的 WMF 向量图 头部确实不一致，但考虑到在 Libreoffice/MS Office 上面可以被正常解析，所以猜测 应该是版本 不兼容问题导致的。待验证 .... 


WMF Header 读取代码
-------------------------

.. code:: python

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    import os,sys,time
    from struct import pack,unpack


    class Wmf:
        def __init__(self):
            pass
        def decode(self, data):
            # Decode Windows Metafile 
            #header = data[0:18]
            print "======================"
            print "Raw: %s" % repr(data[0:18])
            header = unpack("HHHHHHIH", data[0:18])
            print "Type: %d\tHeaderSize: %d\tVersion: %d\tSizeLow: %d\tSizeHigh: %d\tNumberOfObjects: %d\tMaxRecord: %d\t" %( header[0],header[1],header[2],header[3],header[4],header[5],header[6])

    if __name__ == '__main__':
        if len(sys.argv) > 1:
            Wmf().decode(open(sys.argv[1], 'r').read())
        else:
            print ":: 没有指定任何 WMF 文件."

::

    luozijun@luozijun-LIFEBOOK-LH532 MS-Office研究 % python wmf.py Office文档样本/bad.wmf                                         [1]
    ======================
    Raw: '\x01\x00\x00\x00l\x00\x00\x00\xfe\xff\xff\xff\xff\xff\xff\xff>\x01'
    Type: 1 HeaderSize: 0   Version: 108    SizeLow: 0  SizeHigh: 65534 NumberOfObjects: 65535  MaxRecord: 4294967295   
    luozijun@luozijun-LIFEBOOK-LH532 MS-Office研究 % python wmf.py Office文档样本/good.wmf                                        [0]
    ======================
    Raw: '\x01\x00\t\x00\x00\x03\x9c\x01\x00\x00\x02\x00\x94\x00\x00\x00\x00\x00'
    Type: 1 HeaderSize: 9   Version: 768    SizeLow: 412    SizeHigh: 0 NumberOfObjects: 2  MaxRecord: 148  
    luozijun@luozijun-LIFEBOOK-LH532 MS-Office研究 % python wmf.py Office文档样本/image3.wmf                                      [0]
    ======================
    Raw: '\x01\x00\t\x00\x00\x03\t\x02\x00\x00\x04\x00\xa3\x00\x00\x00\x00\x00'
    Type: 1 HeaderSize: 9   Version: 768    SizeLow: 521    SizeHigh: 0 NumberOfObjects: 4  MaxRecord: 163  



