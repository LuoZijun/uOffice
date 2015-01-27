OOXML解析
==========

:Date: 2015/01/27 23:06

.. contents::


python-ooxml 包在解析金山公司的WPS办公套件生成的docx格式的文档时，会漏解析一些XML元素。一下是发现的列表。

*   <w:p> <w:r><w:r><w:p> (Python OOXML会把 <w:r>元素内容当作纯文本处理，但是WPS软件会把影像元素附加在<w:p>元素下面。比较合乎逻辑的做法应该是放在 <w:drawing>元素下面)

影像元素标签声明


金山办公套件不规范列表：

*   <w:pict> (已知对应的多媒体类型为 PNG 格式图片)
*   <w:object> （已知对应的多媒体类型为 WMF 格式向量图）
*   


关于金山办公套件图片色彩失真问题
--------------------------------------

我们可以看看这个PNG 格式图片在 金山办公套件生成的 DOCX 格式文件中的 XML描述为:


下面是一个 PNG 图片的描述。

.. code:: xml

    <w:pict>
        <v:shape id="图片 2" o:spid="_x0000_s1026" type="#_x0000_t75"
            style="height:233.25pt;width:414.85pt;rotation:0f;" 
            o:ole="f" fillcolor="#FFFFFF" filled="f" o:preferrelative="t" 
            stroked="f" coordorigin="0,0" coordsize="21600,21600">
        <v:fill on="f" color2="#FFFFFF" focus="0%"/>
        <v:imagedata gain="65536f" blacklevel="0f" gamma="0" o:title="" r:id="rId5"/>
        <o:lock v:ext="edit" position="f" selection="f" grouping="f" rotation="f" cropping="f" text="f" aspectratio="t"/>
        <w10:wrap type="none"/>
        <w10:anchorlock/>
        </v:shape>
    </w:pict>
    
    下面是一个 WMF 向量图的嵌入（金山套件加入 OLEObject）。

    <w:object>
        <v:shape id="图片 1" type="#_x0000_t75" style="height:31pt;width:78.95pt;
            rotation:0f;" o:ole="t" fillcolor="#FFFFFF" filled="f" 
            o:preferrelative="t" stroked="f" coordorigin="0,0" 
            coordsize="21600,21600"><v:fill on="f" color2="#FFFFFF" 
            focus="0%"/>
            <v:imagedata gain="65536f" blacklevel="0f" gamma="0" o:title="" r:id="rId7"/>
            <o:lock v:ext="edit" position="f" selection="f" grouping="f" rotation="f" cropping="f" text="f" aspectratio="t"/>
            <w10:wrap type="none"/>
            <w10:anchorlock/>
        </v:shape>
        <o:OLEObject Type="Embed" ProgID="" ShapeID="图片 1" DrawAspect="Content" ObjectID="_2" r:id="rId6"/>
    </w:object>


我们可以发现在 XML 节点属性当中，加入了很多看起来像是 颜色指令的属性。

另外： 暂且不清楚， 元素 <w:pict>在OOXML 规范文档里面是否为合法标准。目前发现其它的软件生成并没用该项。


正常的 JPEG 格式图片嵌入的 XML 描述:

.. code:: xml

    <w:drawing>
        <wp:inline distT="0" distB="0" distL="0" distR="0">
        <wp:extent cx="2000250" cy="2152650"/>
        <wp:effectExtent l="19050" t="0" r="0" b="0"/>
        <wp:docPr id="12" name="图片 12" descr="1"/>
        <wp:cNvGraphicFramePr>
        <a:graphicFrameLocks noChangeAspect="1"/>
        </wp:cNvGraphicFramePr>
        <a:graphic>
            <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
            <pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="Picture 12" descr="1"/>
            <pic:cNvPicPr><a:picLocks noChangeAspect="1" noChangeArrowheads="1"/></pic:cNvPicPr>
            </pic:nvPicPr><pic:blipFill><a:blip r:embed="rId24"/><a:srcRect/>
            <a:stretch><a:fillRect/></a:stretch>
            </pic:blipFill>
            <pic:spPr bwMode="auto">
                <a:xfrm><a:off x="0" y="0"/>
                <a:ext cx="2000250" cy="2152650"/></a:xfrm><a:prstGeom prst="rect">
                <a:avLst/></a:prstGeom><a:noFill/>
                <a:ln w="9525"><a:noFill/>
                <a:miter lim="800000"/>
                    <a:headEnd/><a:tailEnd/></a:ln>
            </pic:spPr>
            </pic:pic>
            </a:graphicData>
            </a:graphic>
       </wp:inline>
    </w:drawing>



修正OOXML一览表
----------------------------

parse.py
^^^^^^^^^^

Add:

.. code:: python

    def parse_pict(document, container, elem):
        """Parse pict element
        Fix KingSoft.
        """
        #<v:imagedata gain="65536f" blacklevel="0f" gamma="0" o:title="" r:id="rId5"/>
        imagedata = elem.xpath('.//v:imagedata', namespaces=NAMESPACES)[0]        
        _rid =  imagedata.attrib[_name('{{{r}}}id')]

        img = doc.Image(_rid)
        container.elements.append(img)

    def parse_object(document, container, elem):
        """Parse object element
        Fix KingSoft.
        """
        #<v:imagedata gain="65536f" blacklevel="0f" gamma="0" o:title="" r:id="rId5"/>
        imagedata = elem.xpath('.//v:imagedata', namespaces=NAMESPACES)[0]        
        _rid =  imagedata.attrib[_name('{{{r}}}id')]

        img = doc.Image(_rid)
        container.elements.append(img)

Change:

.. code:: python

    def parse_text(document, container, element):
        "Parse text element."

        txt = None

        alternate = element.find(_name('{{{mc}}}AlternateContent'))

        if alternate is not None:
            parse_alternate(document, container, alternate)

        br = element.find(_name('{{{w}}}br'))

        if br is not None:
            if _name('{{{w}}}type') in br.attrib:
                _type = br.attrib[_name('{{{w}}}type')]        
                brk = doc.Break(_type)
            else:
                brk = doc.Break()

            container.elements.append(brk)

        t = element.find(_name('{{{w}}}t'))

        if t is not None:
            txt = doc.Text(t.text)
            txt.parent = container

            container.elements.append(txt)

        rpr = element.find(_name('{{{w}}}rPr'))

        if rpr is not None:
            # Notice it is using txt as container
            parse_previous_properties(document, txt, rpr)

        for r in element.findall(_name('{{{w}}}r')):
            parse_text(document, container, r)

        foot = element.find(_name('{{{w}}}footnoteReference'))

        if foot is not None:
            parse_footnote(document, container, foot)

        end = element.find(_name('{{{w}}}endnoteReference'))

        if end is not None:
            parse_endnote(document, container, end)

        sym = element.find(_name('{{{w}}}sym'))

        if sym is not None:
            _font = sym.attrib[_name('{{{w}}}font')]
            _char = sym.attrib[_name('{{{w}}}char')]

            container.elements.append(doc.Symbol(font=_font, character=_char))

        image = element.find(_name('{{{w}}}drawing'))

        if image is not None:
            parse_drawing(document, container, image)
        
        k_image = element.find(_name('{{{w}}}pict'))
        if k_image is not None:
            parse_pict(document, container, k_image)
        
        k_object = element.find(_name('{{{w}}}pict'))
        if k_object is not None:
            parse_object(document, container, k_object)
        

        return


serialize.py
^^^^^^^^^^^^^^

Change:

.. code:: python

    def serialize_image(ctx, document, elem, root):
        """Serialize image element.

        This is not abstract enough.
        """

        img_src = document.relationships[elem.rid]['target']
        #print img_src
        img_name, img_extension = os.path.splitext(img_src)
        #print img_name
        _img = etree.SubElement(root, 'img')
        #print dir(_img)
        # make path configurable
        #_img.set('src', 'static/{}{}'.format(elem.rid, img_extension))
        _img.set('src', 'static/{}{}'.format(img_name, img_extension))

        fire_hooks(ctx, document, elem, _img, ctx.get_hook('img'))

        return root

    
