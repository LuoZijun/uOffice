#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    ECMA-376, Fourth Edition, Part 1 - Fundamentals And Markup Language Reference
    
    22.1

Elements:

22.1.2 Elements .................................................................................................................................... 3592
22.1.2.1 acc (Accent) ................................................................................................................................. 3592
22.1.2.2 accPr (Accent Properties) ............................................................................................................ 3593
22.1.2.3 aln (Alignment) ............................................................................................................................ 3593
22.1.2.4 alnScr (Align Scripts) .................................................................................................................... 3595
22.1.2.5 argPr (Argument Properties) ....................................................................................................... 3596
22.1.2.6 argSz (Argument Size) .................................................................................................................. 3597
22.1.2.7 bar (Bar) ....................................................................................................................................... 3599
22.1.2.8 barPr (Bar Properties) .................................................................................................................. 3599
22.1.2.9 baseJc (Matrix Base Justification) ................................................................................................ 3600
22.1.2.10 begChr (Delimiter Beginning Character) ..................................................................................... 3603
22.1.2.11 borderBox (Border-Box Object) ................................................................................................... 3604
22.1.2.12 borderBoxPr (Border-Box Properties) ......................................................................................... 3604
22.1.2.13 box (Box Object) .......................................................................................................................... 3605
22.1.2.14 boxPr (Box Properties) ................................................................................................................. 3605
22.1.2.15 brk (Break) ................................................................................................................................... 3606
22.1.2.16 brkBin (Break on Binary Operators) ............................................................................................ 3608
22.1.2.17 brkBinSub (Break on Binary Subtraction) .................................................................................... 3609
22.1.2.18 cGp (Matrix Column Gap) ............................................................................................................ 3610
22.1.2.19 cGpRule (Matrix Column Gap Rule) ............................................................................................. 3611
22.1.2.20 chr (Character) ............................................................................................................................. 3613
22.1.2.21 count (Matrix Column Count) ...................................................................................................... 3614
22.1.2.22 cSp (Minimum Matrix Column Width) ........................................................................................ 3615
22.1.2.23 ctrlPr (Control Properties) ........................................................................................................... 3616
22.1.2.24 d (Delimiter Object) ..................................................................................................................... 3617
22.1.2.25 defJc (Default Justification) ......................................................................................................... 3618

22.1.2.26   deg (Degree) ................................................................................................................................ 3619
22.1.2.27   degHide (Hide Degree) ................................................................................................................ 3620
22.1.2.28   den (Denominator) ...................................................................................................................... 3621
22.1.2.29   diff (Differential) .......................................................................................................................... 3621
22.1.2.30   dispDef (Use Display Math Defaults) ........................................................................................... 3623
22.1.2.31   dPr (Delimiter Properties) ........................................................................................................... 3624
22.1.2.32   e (Element (Argument)) ............................................................................................................... 3624
22.1.2.33   endChr (Delimiter Ending Character) .......................................................................................... 3626
22.1.2.34   eqArr (Array Object) .................................................................................................................... 3626
22.1.2.35   eqArrPr (Array Properties) ........................................................................................................... 3628
22.1.2.36   f (Fraction Object) ........................................................................................................................ 3629
22.1.2.37   fName (Function Name) .............................................................................................................. 3630
22.1.2.38   fPr (Fraction Properties) .............................................................................................................. 3630
22.1.2.39   func (Function Apply Object) ....................................................................................................... 3631
22.1.2.40   funcPr (Function Properties) ....................................................................................................... 3631
22.1.2.41   groupChr (Group-Character Object) ............................................................................................ 3632
22.1.2.42   groupChrPr (Group-Character Properties) .................................................................................. 3633
22.1.2.43   grow (n-ary Grow) ....................................................................................................................... 3633
22.1.2.44   hideBot (Hide Bottom Edge) ........................................................................................................ 3634
22.1.2.45   hideLeft (Hide Left Edge) ............................................................................................................. 3635
22.1.2.46   hideRight (Hide Right Edge) ......................................................................................................... 3636
22.1.2.47   hideTop (Hide Top Edge) ............................................................................................................. 3637
22.1.2.48   interSp (Inter-Equation Spacing) ................................................................................................. 3637
22.1.2.49   intLim (Integral Limit Locations) .................................................................................................. 3638
22.1.2.50   intraSp (Intra-Equation Spacing) ................................................................................................. 3639
22.1.2.51   jc (Justification) ............................................................................................................................ 3639
22.1.2.52   lim (Limit) ..................................................................................................................................... 3640
22.1.2.53   limLoc (n-ary Limit Location) ....................................................................................................... 3640
22.1.2.54   limLow (Lower-Limit Object) ....................................................................................................... 3641
22.1.2.55   limLowPr (Lower-Limit Properties) .............................................................................................. 3642
22.1.2.56   limUpp (Upper-Limit Object) ....................................................................................................... 3642
22.1.2.57   limUppPr (Upper-Limit Properties) ............................................................................................. 3643
22.1.2.58   lit (Literal) .................................................................................................................................... 3644
22.1.2.59   lMargin (Left Margin)................................................................................................................... 3645
22.1.2.60   m (Matrix Object) ........................................................................................................................ 3646
22.1.2.61   mathFont (Math Font) ................................................................................................................. 3648
22.1.2.62   mathPr (Math Properties) ........................................................................................................... 3649
22.1.2.63   maxDist (Maximum Distribution) ................................................................................................ 3650
22.1.2.64   mc (Matrix Column) ..................................................................................................................... 3652
22.1.2.65   mcJc (Matrix Column Justification) .............................................................................................. 3653
22.1.2.66   mcPr (Matrix Column Properties) ................................................................................................ 3655
22.1.2.67   mcs (Matrix Columns) .................................................................................................................. 3657
22.1.2.68   mPr (Matrix Properties) ............................................................................................................... 3658
22.1.2.69   mr (Matrix Row) .......................................................................................................................... 3659
22.1.2.70   nary (n-ary Operator Object) ....................................................................................................... 3661
22.1.2.71   naryLim (n-ary Limit Location) ..................................................................................................... 3662
22.1.2.72   naryPr (n-ary Properties) ............................................................................................................. 3663
22.1.2.73   noBreak (No Break) ..................................................................................................................... 3664

22.1.2.74   nor (Normal Text) ........................................................................................................................ 3665
22.1.2.75   num (Numerator) ........................................................................................................................ 3666
22.1.2.76   objDist (Object Distribution)........................................................................................................ 3667
22.1.2.77   oMath (Office Math) .................................................................................................................... 3668
22.1.2.78   oMathPara (Office Math Paragraph) ........................................................................................... 3669
22.1.2.79   oMathParaPr (Office Math Paragraph Properties) ...................................................................... 3669
22.1.2.80   opEmu (Operator Emulator) ........................................................................................................ 3670
22.1.2.81   phant (Phantom Object) .............................................................................................................. 3671
22.1.2.82   phantPr (Phantom Properties) .................................................................................................... 3672
22.1.2.83   plcHide (Hide Placeholders (Matrix)) .......................................................................................... 3672
22.1.2.84   pos (Position) ............................................................................................................................... 3673
22.1.2.85   postSp (Post-Paragraph Spacing) ................................................................................................ 3674
22.1.2.86   preSp (Pre-Paragraph Spacing) .................................................................................................... 3674
22.1.2.87   r (Run) .......................................................................................................................................... 3675
22.1.2.88   rad (Radical Object) ..................................................................................................................... 3675
22.1.2.89   radPr (Radical Properties) ............................................................................................................ 3676
22.1.2.90   rMargin (Right Margin) ................................................................................................................ 3676
22.1.2.91   rPr (Run Properties) ..................................................................................................................... 3677
22.1.2.92   rSp (Row Spacing (Array)) ............................................................................................................ 3678
22.1.2.93   rSpRule (Row Spacing Rule) ......................................................................................................... 3679
22.1.2.94   scr (Script) .................................................................................................................................... 3681
22.1.2.95   sepChr (Delimiter Separator Character) ...................................................................................... 3682
22.1.2.96   show (Phantom Show) ................................................................................................................. 3683
22.1.2.97   shp (Shape (Delimiters)) .............................................................................................................. 3683
22.1.2.98   smallFrac (Small Fraction)............................................................................................................ 3684
22.1.2.99   sPre (Pre-Sub-Superscript Object) ............................................................................................... 3685
22.1.2.100  sPrePr (Pre-Sub-Superscript Properties) ................................................................................. 3685
22.1.2.101  sSub (Subscript Object) ............................................................................................................ 3686
22.1.2.102  sSubPr (Subscript Properties) .................................................................................................. 3687
22.1.2.103  sSubSup (Sub-Superscript Object) ........................................................................................... 3687
22.1.2.104  sSubSupPr (Sub-Superscript Properties) ................................................................................. 3688
22.1.2.105  sSup (Superscript Object) ........................................................................................................ 3689
22.1.2.106  sSupPr (Superscript Properties) ............................................................................................... 3689
22.1.2.107  strikeBLTR (Border Box Strikethrough Bottom-Left to Top-Right) .......................................... 3690
22.1.2.108  strikeH (Border Box Strikethrough Horizontal) ....................................................................... 3691
22.1.2.109  strikeTLBR (Border Box Strikethrough Top-Left to Bottom-Right) .......................................... 3691
22.1.2.110  strikeV (Border Box Strikethrough Vertical) ............................................................................ 3692
22.1.2.111  sty (style) ................................................................................................................................. 3693
22.1.2.112  sub (Subscript (Pre-Sub-Superscript)) ..................................................................................... 3694
22.1.2.113  subHide (Hide Subscript (n-ary)) ............................................................................................. 3694
22.1.2.114  sup (Superscript (Superscript object)) ..................................................................................... 3695
22.1.2.115  supHide (Hide Superscript (n-ary)) .......................................................................................... 3696
22.1.2.116  t (Text) ..................................................................................................................................... 3697
22.1.2.117  transp (Transparent (Phantom)) .............................................................................................. 3697
22.1.2.118  type (Fraction type) ................................................................................................................. 3698
22.1.2.119  vertJc (Vertical Justification) .................................................................................................... 3699
22.1.2.120  wrapIndent (Wrap Indent) ...................................................................................................... 3701
22.1.2.121  wrapRight (Wrap Right) ........................................................................................................... 3701
22.1.2.122  zeroAsc (Phantom Zero Ascent) .............................................................................................. 3702
22.1.2.123  zeroDesc (Phantom Zero Descent) .......................................................................................... 3703
22.1.2.124  zeroWid (Phantom Zero Width) .............................................................................................. 3704

22.1.3 Simple Types .............................................................................................................................. 3705
22.1.3.1    ST_BreakBin (Break Binary Operators) ........................................................................................ 3705
22.1.3.2    ST_BreakBinSub (Break on Binary Subtraction) .......................................................................... 3705
22.1.3.3    ST_Char (Character) ..................................................................................................................... 3706
22.1.3.4    ST_FType (Fraction Type) ............................................................................................................ 3706
22.1.3.5    ST_Integer2 (Integer value (-2 to 2)) ........................................................................................... 3707
22.1.3.6    ST_Integer255 (Integer value (1 to 255)) .................................................................................... 3707
22.1.3.7    ST_Jc (Justification) ...................................................................................................................... 3707
22.1.3.8    ST_LimLoc (Limit Location) .......................................................................................................... 3708
22.1.3.9    ST_Script (Script) ......................................................................................................................... 3708
22.1.3.10   ST_Shp (Shape (Delimiters)) ........................................................................................................ 3709
22.1.3.11   ST_SpacingRule (Spacing Rule) .................................................................................................... 3709
22.1.3.12   ST_Style (Style) ............................................................................................................................ 3709
22.1.3.13   ST_TopBot (Top-Bottom) ............................................................................................................. 3710
22.1.3.14   ST_UnSignedInteger (Unsigned integer.) .................................................................................... 3710


"""

import dwml
import dwml.omml
DOCXML_ROOT = ''.join(('<w:document '
            ,'xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" '
            ,'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
            ,'xmlns:o="urn:schemas-microsoft-com:office:office" '
            ,'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            ,'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
            ,'xmlns:v="urn:schemas-microsoft-com:vml" '
            ,'xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" '
            ,'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
            ,'xmlns:w10="urn:schemas-microsoft-com:office:word" '
            ,'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            ,'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
            ,'xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" '
            ,'xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" '
            ,'xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" '
            ,'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 wp14">'
            ,'{0}</w:document>'
        ))

"""

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\thispagestyle{empty}
\begin{document}
\[
x=\frac{-b±\sqrt{b^{2}-4ac}}{2a}
\]
\end{document}

"""



"""
header = '''
\\nonstopmode
\\documentclass[12pt]{article}
\\pagestyle{empty}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage[latin1]{inputenc}
\\begin{document}
\\[
'''

footer = '''
\\]
\\end{document}
'''

"""
LATEX_TEMPLATE = """
\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\thispagestyle{empty}
\begin{document}
\[
%s
\]
\end{document}
"""

def decode(omml):
    xml_str = DOCXML_ROOT.format(omml)
    a = dwml.omml.load_string(xml_str)[0].latex
    return LATEX_TEMPLATE % (a)



