OOXML解析
==========


python-ooxml 包在解析金山公司的WPS办公套件生成的docx格式的文档时，会漏解析一些XML元素。一下是发现的列表。

*   <w:p> <w:r><w:r><w:p> (Python OOXML会把 <w:r>元素内容当作纯文本处理，但是WPS软件会把影像元素附加在<w:p>元素下面。比较合乎逻辑的做法应该是放在 <w:drawing>元素下面)


