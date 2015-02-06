#!/usr/bin/env python
#-*- coding:utf-8 -*-


from lxml import etree

doc = etree.parse('a.xml')


def node(obj):
	doms = []
	for x in obj.iterchildren():
		doms.append(x)
	return doms



def fetch_text(dom):
	return dom.text

content = u''
for dom in doc.getiterator():
	for children in node(dom):
		text = fetch_text(children)
		if text == '' or text == None or text == 'None':
			pass
		else:
			if 'unicode' not in str(type(text)):
				text = unicode(text)
			content += text

print "\n:: Raw Content:\n\n", repr(content), "\n\n:: String For Human:\n", content

