ECMA-376 WordprocessingML
============================


*ECMA-376 Part 1 Page 28*


This clause contains specifications for relationship items and parts that are specific to WordprocessingML. Parts
that can occur in a WordprocessingML document, but are not WordprocessingML-specific, are specified
in §15.2. Unless stated explicitly, all references to relationship items, content-type items, and parts in this clause
refer to WordprocessingML ZIP items.


11.1    Glossary of WordprocessingML-Specific Terms
-----------------------------------------------------------------------
The following terms are used in the context of a WordprocessingML document:

**document setting** — A document-level property that affects the handling of a given document, and influences
the appearance and behavior of the current document, as well as the stored document-level state.

**document building block** — A reusable element in a template. [Note: Such elements include boilerplate text,
cover pages, equations, footers, headers, tables, text boxes, and watermarks. end note]

**glossary document** — An additional WordprocessingML document story used to store reusable fragments of
rich WordprocessingML content. It is called the glossary document as this story contains one or more fragments
that can be indexed and extracted by name, like items in a glossary.

**master document** — A document that is the parent of one or more subdocuments. [Note: A master document
can be used to manage a multipart document, such as a book having several chapters. In such as case, the
master document might contain the cover page, front matter, table of contents, and cross-reference index,
while each chapter and appendix resides in its own subdocument. end note]

**section** — A portion of a document in which certain page formatting options can be set. [Note: A new section is
created to change such properties as line numbering, number of columns, or headers and footers. end note]

**subdocument** — A piece of a master document. [Note: A chapter or appendix might be a subdocument in a
book. end note]

**supplementary document storage location** — A part within a WordprocessingML document in which fragments
of WordprocessingML content can be stored separate from the printed page. See also glossary document

**template** — A document that is a pattern for creating other documents. A template can contain text,
formatting, and graphics, among other things, such that documents based on it automatically have access to
these elements.


11.2 Package Structure
-------------------------------------------
A WordprocessingML package shall contain a package-relationship item and a content-type item. The package-
relationship item shall have implicit relationships with targets of the following type:

*   One Main Document part (§11.3.10)

The package-relationship item is permitted to have implicit relationships with targets of the following type:

*   Digital Signature Origin (§15.2.7)
*   File Property parts (§15.2.12) (Application-Defined File Properties, Core File Properties, and Custom File
*   Properties), as appropriate.
*   Thumbnail (§15.2.16).

The required and optional relationships between parts are defined in §16.1 and its subordinate clauses.

::

    [Example: The following package represents the minimal conformant WordprocessingML package as defined by
    ECMA-376:
    First, the content type for relationship parts and the Main Document part (the only required part) must be
    defined (physically located at /[Content_Types].xml in the package):

        <Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
        <Default Extension="rels"
        ContentType="application/vnd.openxmlformats-
        package.relationships+xml"/>
        <Override PartName="/document.xml"
        ContentType="application/vnd.openxmlformats-
        officedocument.wordprocessingml.document.main+xml"/>
        </Types>
        
    Next, the single required relationship (the package-level relationship to the Main Document part) must be
    defined (physically located at /_rels/.rels in the package)

        <Relationships xmlns="...">
        <Relationship Id="rId1"
        Type="http://purl.oclc.org/ooxml/officeDocument/relationships/officeDocument"
        Target="document.xml"/>
        </Relationships>
        Finally, the minimum content for the Main Document part must be defined (physically located at /document.xml
        in the package):
        <w:document xmlns:w="...">
        <w:body>
        <w:p/>
        </w:body>
        </w:document>

    end example]

::

    [Example: Consider a WordprocessingML document that is an early draft of ECMA-376. Here’s an example of the
    hierarchical folder structure that might be used for the ZIP items in the package for that document. As shown,
    one part, Main Document (stored in the ZIP item /word/document.xml), has its own relationship item:
    /[Content_Types].xml
    Content-type item
    /_rels/.rels
    Package-relationship item
    /docProps/app.xml
    Application-Defined File Properties part
    /docProps/core.xml
    Core File Properties part
    /word/document.xml
    Main Document part
    /word/_rels/document.xml.rels
    Part-relationship item
    /word/comments.xml
    Comment part
    /word/endnotes.xml
    Endnotes part
    /word/fontTable.xml
    Font Table part
    /word/footer1.xml
    Footer parts
    /word/footer2.xml
    /word/footer3.xml
    /word/footer4.xml
    /word/footnotes.xml
    Footnotes part
    /word/header1.xml
    Header parts
    /word/header2.xml
    /word/header3.xml
    /word/header4.xml
    /word/header5.xml
    /word/header6.xml
    /word/numbering.xml
    Numbering Definitions part
    /word/settings.xml
    Document Settings part
    /word/styles.xml
    Style Definitions part
    /word/theme/theme1.xml
    Theme part
    The package-relationship item contains the following:
    <Relationships xmlns="...">
    <Relationship Id="rId3"
    Type="http://.../extended-properties" Target="docProps/app.xml"/>
    <Relationship Id="rId2"
    Type="http://.../core-properties" Target="docProps/core.xml"/>
    <Relationship Id="rId1"
    Type="http://.../officeDocument" Target="word/document.xml"/>
    </Relationships>
    end example]



11.3 Part Summary
-------------------------------
The subclauses subordinate to this one describe in detail each of the part types specific to WordprocessingML.

[Note: For convenience, information from those subclauses is summarized in the following table::

    Part                                                    Relationship Target of                                                                                            Root Element      Ref.
    Alternative Format Import         Comments, Endnotes, Footer, Footnotes, Header, or Main Document   Not applicable    §11.3.1
    Comments                                       Glossary Document or Main Document                                                            comments            §11.3.2
    Document Settings                       Glossary Document or Main Document                                                            settings                 §11.3.3
    Endnotes                                          Glossary Document or Main Document                                                            endnotes              §11.3.4
    Font Table                         Glossary Document or Main Document     fonts                             §11.3.5
    Footer                                 Glossary Document or Main Document     ftr                                  §11.3.6
    Footnotes                          Glossary Document or Main Document     footnotes                    §11.3.7
    Glossary Document        Main Document                                                 glossaryDocument  §11.3.8
    Header                                Glossary Document or Main Document     hdr                                §11.3.9
    Main Document               WordprocessingML package                         document                   §11.3.10
    Numbering Definitions  Glossary Document or Main Document     numbering                  §11.3.11
    Style Definitions              Glossary Document or Main Document    styles                            §11.3.12
    Web Settings                    Glossary Document or Main Document    webSettings                §11.3.13

end note]


11.3.1 Alternative Format Import Part
-----------------------------------------------------

