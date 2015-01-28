OMML格式分析
===============

:Date: 2015/01/28 14:05

.. contents:: 

介绍: `Office MathML (OMML) <https://en.wikipedia.org/wiki/Office_Open_XML_file_formats#Office_MathML_.28OMML.29>`_

shared-math.xsd
-----------------------------------
Source: `shared-math.xsd <http://www.datypic.com/sc/ooxml/s-shared-math.xsd.html>`_




MathML and Ecma Math (OMML)
--------------------------------------------

Source: `MSDN Blog <http://blogs.msdn.com/b/murrays/archive/2006/10/07/mathml-and-ecma-math-_2800_omml_2900_-.aspx>`_

Before comparing these two math XMLs, I'm excited to point you at Jennifer Michelstein's nifty post on Equations in Word 2007. It comes complete with instructive videos demonstrating how to enter mathematical expressions using the Equation Ribbon as well as using the linear format discussed in my earlier postings. Jennifer plans to add other posts on this subject to the Microsoft Office Word blog. It's worth pointing out that Outlook 2007 also has Word's math facility since Outlook 2007 uses Word 2007 for editing all email body text.

I'm currently busily connecting RichEdit's math facility to external clients, using three file formats: RTF, MathML, OMML (Office MathML). These are all high-level formats compared to the linear format we use for equation input. Naturally RichEdit has to handle RTF math, since RTF has been RichEdit's main file format since RichEdit 1.0 shipped back in 1993 for the Windows 3.1 mail client. RTF math is essentially just OMML with RTF braces {} instead of XML tags. With it, it's easy to copy technical text to and from Word 2007. RichEdit is used by the Microsoft Math graphing calculator, which ships with the Encarta Student Edition, but the calculator communicates with RichEdit using RichEdit's text object model (TOM) instead of a file format. RichEdit also handles text in OneNote, but the math facility isn't turned on there yet.

Meanwhile it would be great to connect RichEdit with the incredible math engines out there like OpenMaple, Mathematica, etc., and clearly MathML is the lingua franca for that. So I've been developing MathML and OMML writers for RichEdit and Misha (Mikhail Baranovsky) is developing the readers (they're harder!) In the process, we've been comparing these two math XMLs.

Naturally there's been a lot of discussion as to why we even have `OMML <http://www.ecma-international.org/news/TC45_current_work/Office%20Open%20XML%20Part%204%20-%20Markup%20Language%20Reference.docx>`_ , since MathML is really good. Brian Jones has addressed that issue in some detail in his `Open XML Formats <http://blogs.msdn.com/brian_jones/>`_ blog. The main problem is that Word needs to allow users to embed arbitrary span-level material (basically anything you can put into a Word paragraph) in math zones and MathML is geared toward allowing only math in math zones. A subsidiary consideration is the desire to have an XML that corresponds closely to the internal format, aiding performance and offering readily achievable robustness. Since both MathML and OMML are XMLs, XSLTs can (and have) been created to convert one into the other. So it seems you can have your cake and eat it too. Thank you XML!

The spirits of MathML and OMML are somewhat different. By MathML, I'm referring to the `MathML <http://www.w3.org/TR/2003/REC-MathML2-20031021/chapter3.html>`_ presentation tag set, rather than the content tag set, since our main emphasis is on presentation. A quick summary of the difference in spirits is

1.   MathML built-up objects may be described by an infix notation, while OMML's are described by a prefix notation
2.   MathML built-up object arguments are defined positionally, while OMML's are tagged explicitly

With MathML when you find an <mrow>, you look at the next tag(s) to see what's inside. If you find an <mo> entry, you have an operator, which you look up in your operator table to figure what kind of a possibly built-up object is involved. It could be an open fence (parentheses, brackets, braces, etc.), an n-ary operator, a function-apply (for trigonometric and other math functions), or one of many operators that don't get built up. For fences MathML also has the <mfenced> tag, which is essentially the same as OMML's delimiter <d> tag.

Each way of representing fences has its advantages, the infix approach allowing embellished fences (such as underlined fences) and the <mfenced> approach allowing a sequence of separated arguments. OMML's <d> can't represent embellished fences, but fortunately for OMML, they aren't common. At least, we couldn't find any in my shelves of physics and math books, but you never know for sure about these mathematicians J. Built-up expressions like subscripts and superscripts are represented by prefix notations in both MathML and OMML.

The following table summarizes the built-up objects in the Office math model along with the OMML and target MathML tags::

    Built-up Office Math Object OMML tag    MathMl
    Accent          acc mover/munder
    Bar bar mover/munder
    Box         box menclose (approx)
    BoxedFormula        borderBox   menclose
    Delimiters  d   mfenced
    EquationArray   eqArr   mtable (with alignment groups)
    Fraction    f   mfrac
    FunctionApply   func    &FunctionApply; (binary operator)
    LeftSubSup  sPre    mmultiscripts (special case of)
    LowerLimit  limLow  munder
    Matrix  m   mtable
    Nary    nary    mrow followed by n-ary mo
    Phantom phant   mphantom and/or mpadded
    Radical rad msqrt/mroot
    GroupChar   groupChr    mover/munder
    Subscript   sSub    msub
    SubSup  sSubSup msubsup
    Superscript sSup    msup
    UpperLimit  limUpp  mover


OMML tags are always written with a math namespace prefix like "m:" and I recommend this convention for MathML as well. The reason is that these XMLs are useful in many contexts, not just in HTML(5) and using namespace prefixes allows the XML parser to delegate to the appropriate tag-set owner.

Comparing the two ways of representing the built-up fraction, we see how OMML has explicit argument tags, whereas MathML determines arguments by position. The built up version of the fraction a/b in OMML is represented by (aside from possible properties)

::

    <m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
    <m:f> 
        <m:num> 
        <m:r>
            <m:t>a</m:t>
        </m:r> 
        </m:num> 
        <m:den> 
        <m:r>
            <m:t>b</m:t>
        </m:r> 
        </m:den> 
    </m:f>
    </m:oMath>

where we see how the numerator and denominator are tagged explicitly. In MathML, these arguments are given by the next entity and the one after that, respectively:

::

    <m:mfrac> 
    <m:mi>a</m:mi> 
    <m:mi>b</m:mi> 
    </m:mfrac>

This comparison reveals that OMML can be more verbose than MathML. A less verbose comparison results for the fraction (a+b)/c, since in OMML it's

::

    <m:f> 
    <m:num> 
        <m:r><m:t>a+b</m:t></m:r> 
    </m:num> 
    <m:den> 
        <m:r><m:t>c</m:t></m:r> 
    </m:den> 
    </m:f>

whereas in MathML, it's

::

    <m:mfrac> 
    <m:mrow> 
        <m:mi>a</m:mi> 
        <m:mo>+</m:mo> 
        <m:mi>b</m:mi> 
    </m:mrow> 
    <m:mi>c</m:mi> 
    </m:mfrac>

Here the <m:mrow> is needed for the numerator to make it the first entity following the <m:mfrac>. For both a/b and (a+b)/c, the linear format sure has the shortest representation!

Another difference between MathML and OMML is in the positioning of the radical (root) degree and prescript arguments relative to their respective bases. In OMML these arguments are positioned so that the left and right arrow keys traverse the objects unidirectionally. Specifically for the radical, the degree argument precedes the radicand, while for MathML it follows the radicand. By having it precede, a right arrow key at the start of the radical moves into the degree and then into the radicand, exactly the way one would expect geometrically. Similarly OMML's prescripts precede the base, whereas in MathML's multiscripts object they follow the base.