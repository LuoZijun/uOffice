#!/usr/bin/env python
#-*- coding:utf-8 -*-

class CustomXml(Docx):
    pass
class Relationship(Docx):
    pass

class ContentType(Docx):
    def __init__(self):
        pass
    def parse_contenttype(self):
        pass

class DocProps(Docx):
    def __init__(self):
        pass
    def parse_app(self):
        pass
    def parse_core(self):
        pass
    def parse_custom(self):
        "is exists ??"
        pass


class Word(Docx):
    def __init__(self):
        pass
    def parse_relationship(self):
        pass
    def parse_style(self):
        pass
    def parse_fonttable(self):
        pass
    def parse_theme(self):
        pass
    def parse_embeddings(self):
        pass
    def parse_media(self):
        "parse media files."
        pass
    def parse_document(self):
        pass


    