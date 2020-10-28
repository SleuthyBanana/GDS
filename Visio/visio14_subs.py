#!/usr/bin/env python

#
# Generated Fri Oct 23 17:03:41 2020 by generateDS.py version 2.36.4.
# Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
#
# Command line options:
#   ('-o', 'visio14_main.py')
#   ('-s', 'visio14_subs.py')
#
# Command line arguments:
#   1 - XML Schemas\Visio2010XSDFiles\visio14.xsd
#
# Command line:
#   generateDS.py -o "visio14_main.py" -s "visio14_subs.py" 1 - XML Schemas\Visio2010XSDFiles\visio14.xsd
#
# Current working directory (os.getcwd()):
#   3 - generateDS
#

import os
import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class Row_TypeSub(supermod.Row_Type):
    def __init__(self, Del=None, extensiontype_=None, **kwargs_):
        super(Row_TypeSub, self).__init__(Del, extensiontype_,  **kwargs_)
supermod.Row_Type.subclass = Row_TypeSub
# end class Row_TypeSub


class IndexedRow_TypeSub(supermod.IndexedRow_Type):
    def __init__(self, IX=None, Del=None, extensiontype_=None, **kwargs_):
        super(IndexedRow_TypeSub, self).__init__(IX, Del, extensiontype_,  **kwargs_)
supermod.IndexedRow_Type.subclass = IndexedRow_TypeSub
# end class IndexedRow_TypeSub


class NamedRow_TypeSub(supermod.NamedRow_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, extensiontype_=None, **kwargs_):
        super(NamedRow_TypeSub, self).__init__(Name, NameU, Del, ID, extensiontype_,  **kwargs_)
supermod.NamedRow_Type.subclass = NamedRow_TypeSub
# end class NamedRow_TypeSub


class NamedIndexedRow_TypeSub(supermod.NamedIndexedRow_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, IX=None, extensiontype_=None, **kwargs_):
        super(NamedIndexedRow_TypeSub, self).__init__(Name, NameU, Del, ID, IX, extensiontype_,  **kwargs_)
supermod.NamedIndexedRow_Type.subclass = NamedIndexedRow_TypeSub
# end class NamedIndexedRow_TypeSub


class GeomSection_TypeSub(supermod.GeomSection_Type):
    def __init__(self, IX=None, Del=None, extensiontype_=None, **kwargs_):
        super(GeomSection_TypeSub, self).__init__(IX, Del, extensiontype_,  **kwargs_)
supermod.GeomSection_Type.subclass = GeomSection_TypeSub
# end class GeomSection_TypeSub


class Cell_TypeSub(supermod.Cell_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, extensiontype_=None, **kwargs_):
        super(Cell_TypeSub, self).__init__(Unit, F, Err, V, valueOf_, extensiontype_,  **kwargs_)
supermod.Cell_Type.subclass = Cell_TypeSub
# end class Cell_TypeSub


class ExtendableCell_TypeSub(supermod.ExtendableCell_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, SolutionXML=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None, **kwargs_):
        super(ExtendableCell_TypeSub, self).__init__(Unit, F, Err, V, SolutionXML, valueOf_, mixedclass_, content_, extensiontype_,  **kwargs_)
supermod.ExtendableCell_Type.subclass = ExtendableCell_TypeSub
# end class ExtendableCell_TypeSub


class SolutionXML_TypeSub(supermod.SolutionXML_Type):
    def __init__(self, Name=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(SolutionXML_TypeSub, self).__init__(Name, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.SolutionXML_Type.subclass = SolutionXML_TypeSub
# end class SolutionXML_TypeSub


class TextCell_TypeSub(supermod.TextCell_Type):
    def __init__(self, cp=None, pp=None, tp=None, fld=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None, **kwargs_):
        super(TextCell_TypeSub, self).__init__(cp, pp, tp, fld, valueOf_, mixedclass_, content_, extensiontype_,  **kwargs_)
supermod.TextCell_Type.subclass = TextCell_TypeSub
# end class TextCell_TypeSub


class cp_TypeSub(supermod.cp_Type):
    def __init__(self, IX=None, **kwargs_):
        super(cp_TypeSub, self).__init__(IX,  **kwargs_)
supermod.cp_Type.subclass = cp_TypeSub
# end class cp_TypeSub


class pp_TypeSub(supermod.pp_Type):
    def __init__(self, IX=None, **kwargs_):
        super(pp_TypeSub, self).__init__(IX,  **kwargs_)
supermod.pp_Type.subclass = pp_TypeSub
# end class pp_TypeSub


class tp_TypeSub(supermod.tp_Type):
    def __init__(self, IX=None, **kwargs_):
        super(tp_TypeSub, self).__init__(IX,  **kwargs_)
supermod.tp_Type.subclass = tp_TypeSub
# end class tp_TypeSub


class fld_TypeSub(supermod.fld_Type):
    def __init__(self, IX=None, valueOf_=None, **kwargs_):
        super(fld_TypeSub, self).__init__(IX, valueOf_,  **kwargs_)
supermod.fld_Type.subclass = fld_TypeSub
# end class fld_TypeSub


class XPropsCell_TypeSub(supermod.XPropsCell_Type):
    def __init__(self, XProp=None, extensiontype_=None, **kwargs_):
        super(XPropsCell_TypeSub, self).__init__(XProp, extensiontype_,  **kwargs_)
supermod.XPropsCell_Type.subclass = XPropsCell_TypeSub
# end class XPropsCell_TypeSub


class XProp_TypeSub(supermod.XProp_Type):
    def __init__(self, Name=None, Unit=None, ID=None, valueOf_=None, **kwargs_):
        super(XProp_TypeSub, self).__init__(Name, Unit, ID, valueOf_,  **kwargs_)
supermod.XProp_Type.subclass = XProp_TypeSub
# end class XProp_TypeSub


class Text_TypeSub(supermod.Text_Type):
    def __init__(self, cp=None, pp=None, tp=None, fld=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(Text_TypeSub, self).__init__(cp, pp, tp, fld, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Text_Type.subclass = Text_TypeSub
# end class Text_TypeSub


class XForm_TypeSub(supermod.XForm_Type):
    def __init__(self, Del=None, PinX=None, PinY=None, Width=None, Height=None, LocPinX=None, LocPinY=None, Angle=None, FlipX=None, FlipY=None, ResizeMode=None, **kwargs_):
        super(XForm_TypeSub, self).__init__(Del, PinX, PinY, Width, Height, LocPinX, LocPinY, Angle, FlipX, FlipY, ResizeMode,  **kwargs_)
supermod.XForm_Type.subclass = XForm_TypeSub
# end class XForm_TypeSub


class PinX_TypeSub(supermod.PinX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PinX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PinX_Type.subclass = PinX_TypeSub
# end class PinX_TypeSub


class PinY_TypeSub(supermod.PinY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PinY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PinY_Type.subclass = PinY_TypeSub
# end class PinY_TypeSub


class Width_TypeSub(supermod.Width_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Width_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Width_Type.subclass = Width_TypeSub
# end class Width_TypeSub


class Height_TypeSub(supermod.Height_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Height_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Height_Type.subclass = Height_TypeSub
# end class Height_TypeSub


class LocPinX_TypeSub(supermod.LocPinX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LocPinX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LocPinX_Type.subclass = LocPinX_TypeSub
# end class LocPinX_TypeSub


class LocPinY_TypeSub(supermod.LocPinY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LocPinY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LocPinY_Type.subclass = LocPinY_TypeSub
# end class LocPinY_TypeSub


class Angle_TypeSub(supermod.Angle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Angle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Angle_Type.subclass = Angle_TypeSub
# end class Angle_TypeSub


class FlipX_TypeSub(supermod.FlipX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FlipX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FlipX_Type.subclass = FlipX_TypeSub
# end class FlipX_TypeSub


class FlipY_TypeSub(supermod.FlipY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FlipY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FlipY_Type.subclass = FlipY_TypeSub
# end class FlipY_TypeSub


class ResizeMode_TypeSub(supermod.ResizeMode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ResizeMode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ResizeMode_Type.subclass = ResizeMode_TypeSub
# end class ResizeMode_TypeSub


class Line_TypeSub(supermod.Line_Type):
    def __init__(self, Del=None, LineWeight=None, LineColor=None, LinePattern=None, Rounding=None, EndArrowSize=None, BeginArrow=None, EndArrow=None, LineCap=None, BeginArrowSize=None, LineColorTrans=None, **kwargs_):
        super(Line_TypeSub, self).__init__(Del, LineWeight, LineColor, LinePattern, Rounding, EndArrowSize, BeginArrow, EndArrow, LineCap, BeginArrowSize, LineColorTrans,  **kwargs_)
supermod.Line_Type.subclass = Line_TypeSub
# end class Line_TypeSub


class LineWeight_TypeSub(supermod.LineWeight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineWeight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineWeight_Type.subclass = LineWeight_TypeSub
# end class LineWeight_TypeSub


class LineColor_TypeSub(supermod.LineColor_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineColor_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineColor_Type.subclass = LineColor_TypeSub
# end class LineColor_TypeSub


class LinePattern_TypeSub(supermod.LinePattern_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LinePattern_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LinePattern_Type.subclass = LinePattern_TypeSub
# end class LinePattern_TypeSub


class Rounding_TypeSub(supermod.Rounding_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Rounding_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Rounding_Type.subclass = Rounding_TypeSub
# end class Rounding_TypeSub


class EndArrowSize_TypeSub(supermod.EndArrowSize_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EndArrowSize_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EndArrowSize_Type.subclass = EndArrowSize_TypeSub
# end class EndArrowSize_TypeSub


class BeginArrow_TypeSub(supermod.BeginArrow_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BeginArrow_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BeginArrow_Type.subclass = BeginArrow_TypeSub
# end class BeginArrow_TypeSub


class EndArrow_TypeSub(supermod.EndArrow_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EndArrow_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EndArrow_Type.subclass = EndArrow_TypeSub
# end class EndArrow_TypeSub


class LineCap_TypeSub(supermod.LineCap_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineCap_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineCap_Type.subclass = LineCap_TypeSub
# end class LineCap_TypeSub


class BeginArrowSize_TypeSub(supermod.BeginArrowSize_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BeginArrowSize_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BeginArrowSize_Type.subclass = BeginArrowSize_TypeSub
# end class BeginArrowSize_TypeSub


class LineColorTrans_TypeSub(supermod.LineColorTrans_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineColorTrans_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineColorTrans_Type.subclass = LineColorTrans_TypeSub
# end class LineColorTrans_TypeSub


class Fill_TypeSub(supermod.Fill_Type):
    def __init__(self, Del=None, FillForegnd=None, FillBkgnd=None, FillPattern=None, ShdwForegnd=None, ShdwBkgnd=None, ShdwPattern=None, FillForegndTrans=None, FillBkgndTrans=None, ShdwForegndTrans=None, ShdwBkgndTrans=None, ShapeShdwType=None, ShapeShdwOffsetX=None, ShapeShdwOffsetY=None, ShapeShdwObliqueAngle=None, ShapeShdwScaleFactor=None, **kwargs_):
        super(Fill_TypeSub, self).__init__(Del, FillForegnd, FillBkgnd, FillPattern, ShdwForegnd, ShdwBkgnd, ShdwPattern, FillForegndTrans, FillBkgndTrans, ShdwForegndTrans, ShdwBkgndTrans, ShapeShdwType, ShapeShdwOffsetX, ShapeShdwOffsetY, ShapeShdwObliqueAngle, ShapeShdwScaleFactor,  **kwargs_)
supermod.Fill_Type.subclass = Fill_TypeSub
# end class Fill_TypeSub


class FillForegnd_TypeSub(supermod.FillForegnd_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FillForegnd_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FillForegnd_Type.subclass = FillForegnd_TypeSub
# end class FillForegnd_TypeSub


class FillBkgnd_TypeSub(supermod.FillBkgnd_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FillBkgnd_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FillBkgnd_Type.subclass = FillBkgnd_TypeSub
# end class FillBkgnd_TypeSub


class FillPattern_TypeSub(supermod.FillPattern_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FillPattern_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FillPattern_Type.subclass = FillPattern_TypeSub
# end class FillPattern_TypeSub


class ShdwForegnd_TypeSub(supermod.ShdwForegnd_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwForegnd_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwForegnd_Type.subclass = ShdwForegnd_TypeSub
# end class ShdwForegnd_TypeSub


class ShdwBkgnd_TypeSub(supermod.ShdwBkgnd_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwBkgnd_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwBkgnd_Type.subclass = ShdwBkgnd_TypeSub
# end class ShdwBkgnd_TypeSub


class ShdwPattern_TypeSub(supermod.ShdwPattern_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwPattern_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwPattern_Type.subclass = ShdwPattern_TypeSub
# end class ShdwPattern_TypeSub


class FillForegndTrans_TypeSub(supermod.FillForegndTrans_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FillForegndTrans_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FillForegndTrans_Type.subclass = FillForegndTrans_TypeSub
# end class FillForegndTrans_TypeSub


class FillBkgndTrans_TypeSub(supermod.FillBkgndTrans_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FillBkgndTrans_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FillBkgndTrans_Type.subclass = FillBkgndTrans_TypeSub
# end class FillBkgndTrans_TypeSub


class ShdwForegndTrans_TypeSub(supermod.ShdwForegndTrans_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwForegndTrans_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwForegndTrans_Type.subclass = ShdwForegndTrans_TypeSub
# end class ShdwForegndTrans_TypeSub


class ShdwBkgndTrans_TypeSub(supermod.ShdwBkgndTrans_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwBkgndTrans_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwBkgndTrans_Type.subclass = ShdwBkgndTrans_TypeSub
# end class ShdwBkgndTrans_TypeSub


class ShapeShdwType_TypeSub(supermod.ShapeShdwType_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeShdwType_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeShdwType_Type.subclass = ShapeShdwType_TypeSub
# end class ShapeShdwType_TypeSub


class ShapeShdwOffsetX_TypeSub(supermod.ShapeShdwOffsetX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeShdwOffsetX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeShdwOffsetX_Type.subclass = ShapeShdwOffsetX_TypeSub
# end class ShapeShdwOffsetX_TypeSub


class ShapeShdwOffsetY_TypeSub(supermod.ShapeShdwOffsetY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeShdwOffsetY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeShdwOffsetY_Type.subclass = ShapeShdwOffsetY_TypeSub
# end class ShapeShdwOffsetY_TypeSub


class ShapeShdwObliqueAngle_TypeSub(supermod.ShapeShdwObliqueAngle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeShdwObliqueAngle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeShdwObliqueAngle_Type.subclass = ShapeShdwObliqueAngle_TypeSub
# end class ShapeShdwObliqueAngle_TypeSub


class ShapeShdwScaleFactor_TypeSub(supermod.ShapeShdwScaleFactor_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeShdwScaleFactor_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeShdwScaleFactor_Type.subclass = ShapeShdwScaleFactor_TypeSub
# end class ShapeShdwScaleFactor_TypeSub


class XForm1D_TypeSub(supermod.XForm1D_Type):
    def __init__(self, Del=None, BeginX=None, BeginY=None, EndX=None, EndY=None, **kwargs_):
        super(XForm1D_TypeSub, self).__init__(Del, BeginX, BeginY, EndX, EndY,  **kwargs_)
supermod.XForm1D_Type.subclass = XForm1D_TypeSub
# end class XForm1D_TypeSub


class BeginX_TypeSub(supermod.BeginX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BeginX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BeginX_Type.subclass = BeginX_TypeSub
# end class BeginX_TypeSub


class BeginY_TypeSub(supermod.BeginY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BeginY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BeginY_Type.subclass = BeginY_TypeSub
# end class BeginY_TypeSub


class EndX_TypeSub(supermod.EndX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EndX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EndX_Type.subclass = EndX_TypeSub
# end class EndX_TypeSub


class EndY_TypeSub(supermod.EndY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EndY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EndY_Type.subclass = EndY_TypeSub
# end class EndY_TypeSub


class Event_TypeSub(supermod.Event_Type):
    def __init__(self, Del=None, TheData=None, TheText=None, EventDblClick=None, EventXFMod=None, EventDrop=None, EventMultiDrop=None, **kwargs_):
        super(Event_TypeSub, self).__init__(Del, TheData, TheText, EventDblClick, EventXFMod, EventDrop, EventMultiDrop,  **kwargs_)
supermod.Event_Type.subclass = Event_TypeSub
# end class Event_TypeSub


class TheData_TypeSub(supermod.TheData_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TheData_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TheData_Type.subclass = TheData_TypeSub
# end class TheData_TypeSub


class TheText_TypeSub(supermod.TheText_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TheText_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TheText_Type.subclass = TheText_TypeSub
# end class TheText_TypeSub


class EventDblClick_TypeSub(supermod.EventDblClick_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EventDblClick_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EventDblClick_Type.subclass = EventDblClick_TypeSub
# end class EventDblClick_TypeSub


class EventXFMod_TypeSub(supermod.EventXFMod_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EventXFMod_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EventXFMod_Type.subclass = EventXFMod_TypeSub
# end class EventXFMod_TypeSub


class EventDrop_TypeSub(supermod.EventDrop_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EventDrop_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EventDrop_Type.subclass = EventDrop_TypeSub
# end class EventDrop_TypeSub


class EventMultiDrop_TypeSub(supermod.EventMultiDrop_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EventMultiDrop_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EventMultiDrop_Type.subclass = EventMultiDrop_TypeSub
# end class EventMultiDrop_TypeSub


class D_TypeSub(supermod.D_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, SolutionXML=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(D_TypeSub, self).__init__(Unit, F, Err, V, SolutionXML, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.D_Type.subclass = D_TypeSub
# end class D_TypeSub


class E_TypeSub(supermod.E_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(E_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.E_Type.subclass = E_TypeSub
# end class E_TypeSub


class LayerMem_TypeSub(supermod.LayerMem_Type):
    def __init__(self, Del=None, LayerMember=None, **kwargs_):
        super(LayerMem_TypeSub, self).__init__(Del, LayerMember,  **kwargs_)
supermod.LayerMem_Type.subclass = LayerMem_TypeSub
# end class LayerMem_TypeSub


class LayerMember_TypeSub(supermod.LayerMember_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LayerMember_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LayerMember_Type.subclass = LayerMember_TypeSub
# end class LayerMember_TypeSub


class Guide_TypeSub(supermod.Guide_Type):
    def __init__(self, **kwargs_):
        super(Guide_TypeSub, self).__init__( **kwargs_)
supermod.Guide_Type.subclass = Guide_TypeSub
# end class Guide_TypeSub


class X_TypeSub(supermod.X_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(X_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.X_Type.subclass = X_TypeSub
# end class X_TypeSub


class Y_TypeSub(supermod.Y_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Y_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Y_Type.subclass = Y_TypeSub
# end class Y_TypeSub


class A_TypeSub(supermod.A_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, SolutionXML=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(A_TypeSub, self).__init__(Unit, F, Err, V, SolutionXML, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.A_Type.subclass = A_TypeSub
# end class A_TypeSub


class StyleProp_TypeSub(supermod.StyleProp_Type):
    def __init__(self, Del=None, EnableLineProps=None, EnableFillProps=None, EnableTextProps=None, HideForApply=None, **kwargs_):
        super(StyleProp_TypeSub, self).__init__(Del, EnableLineProps, EnableFillProps, EnableTextProps, HideForApply,  **kwargs_)
supermod.StyleProp_Type.subclass = StyleProp_TypeSub
# end class StyleProp_TypeSub


class EnableLineProps_TypeSub(supermod.EnableLineProps_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EnableLineProps_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EnableLineProps_Type.subclass = EnableLineProps_TypeSub
# end class EnableLineProps_TypeSub


class EnableFillProps_TypeSub(supermod.EnableFillProps_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EnableFillProps_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EnableFillProps_Type.subclass = EnableFillProps_TypeSub
# end class EnableFillProps_TypeSub


class EnableTextProps_TypeSub(supermod.EnableTextProps_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EnableTextProps_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EnableTextProps_Type.subclass = EnableTextProps_TypeSub
# end class EnableTextProps_TypeSub


class HideForApply_TypeSub(supermod.HideForApply_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(HideForApply_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.HideForApply_Type.subclass = HideForApply_TypeSub
# end class HideForApply_TypeSub


class C_TypeSub(supermod.C_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, SolutionXML=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(C_TypeSub, self).__init__(Unit, F, Err, V, SolutionXML, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.C_Type.subclass = C_TypeSub
# end class C_TypeSub


class Foreign_TypeSub(supermod.Foreign_Type):
    def __init__(self, Del=None, ImgOffsetX=None, ImgOffsetY=None, ImgWidth=None, ImgHeight=None, **kwargs_):
        super(Foreign_TypeSub, self).__init__(Del, ImgOffsetX, ImgOffsetY, ImgWidth, ImgHeight,  **kwargs_)
supermod.Foreign_Type.subclass = Foreign_TypeSub
# end class Foreign_TypeSub


class ImgOffsetX_TypeSub(supermod.ImgOffsetX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ImgOffsetX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ImgOffsetX_Type.subclass = ImgOffsetX_TypeSub
# end class ImgOffsetX_TypeSub


class ImgOffsetY_TypeSub(supermod.ImgOffsetY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ImgOffsetY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ImgOffsetY_Type.subclass = ImgOffsetY_TypeSub
# end class ImgOffsetY_TypeSub


class ImgWidth_TypeSub(supermod.ImgWidth_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ImgWidth_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ImgWidth_Type.subclass = ImgWidth_TypeSub
# end class ImgWidth_TypeSub


class ImgHeight_TypeSub(supermod.ImgHeight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ImgHeight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ImgHeight_Type.subclass = ImgHeight_TypeSub
# end class ImgHeight_TypeSub


class PageProps_TypeSub(supermod.PageProps_Type):
    def __init__(self, Del=None, PageWidth=None, PageHeight=None, ShdwOffsetX=None, ShdwOffsetY=None, PageScale=None, DrawingScale=None, DrawingSizeType=None, DrawingScaleType=None, InhibitSnap=None, UIVisibility=None, ShdwType=None, ShdwObliqueAngle=None, ShdwScaleFactor=None, PageColor=None, DrawingResizeType=None, **kwargs_):
        super(PageProps_TypeSub, self).__init__(Del, PageWidth, PageHeight, ShdwOffsetX, ShdwOffsetY, PageScale, DrawingScale, DrawingSizeType, DrawingScaleType, InhibitSnap, UIVisibility, ShdwType, ShdwObliqueAngle, ShdwScaleFactor, PageColor, DrawingResizeType,  **kwargs_)
supermod.PageProps_Type.subclass = PageProps_TypeSub
# end class PageProps_TypeSub


class PageWidth_TypeSub(supermod.PageWidth_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageWidth_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageWidth_Type.subclass = PageWidth_TypeSub
# end class PageWidth_TypeSub


class PageHeight_TypeSub(supermod.PageHeight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageHeight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageHeight_Type.subclass = PageHeight_TypeSub
# end class PageHeight_TypeSub


class ShdwOffsetX_TypeSub(supermod.ShdwOffsetX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwOffsetX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwOffsetX_Type.subclass = ShdwOffsetX_TypeSub
# end class ShdwOffsetX_TypeSub


class ShdwOffsetY_TypeSub(supermod.ShdwOffsetY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwOffsetY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwOffsetY_Type.subclass = ShdwOffsetY_TypeSub
# end class ShdwOffsetY_TypeSub


class PageScale_TypeSub(supermod.PageScale_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageScale_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageScale_Type.subclass = PageScale_TypeSub
# end class PageScale_TypeSub


class DrawingScale_TypeSub(supermod.DrawingScale_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DrawingScale_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DrawingScale_Type.subclass = DrawingScale_TypeSub
# end class DrawingScale_TypeSub


class DrawingSizeType_TypeSub(supermod.DrawingSizeType_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DrawingSizeType_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DrawingSizeType_Type.subclass = DrawingSizeType_TypeSub
# end class DrawingSizeType_TypeSub


class DrawingScaleType_TypeSub(supermod.DrawingScaleType_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DrawingScaleType_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DrawingScaleType_Type.subclass = DrawingScaleType_TypeSub
# end class DrawingScaleType_TypeSub


class DrawingResizeType_TypeSub(supermod.DrawingResizeType_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DrawingResizeType_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DrawingResizeType_Type.subclass = DrawingResizeType_TypeSub
# end class DrawingResizeType_TypeSub


class InhibitSnap_TypeSub(supermod.InhibitSnap_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(InhibitSnap_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.InhibitSnap_Type.subclass = InhibitSnap_TypeSub
# end class InhibitSnap_TypeSub


class UIVisibility_TypeSub(supermod.UIVisibility_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UIVisibility_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UIVisibility_Type.subclass = UIVisibility_TypeSub
# end class UIVisibility_TypeSub


class ShdwType_TypeSub(supermod.ShdwType_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwType_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwType_Type.subclass = ShdwType_TypeSub
# end class ShdwType_TypeSub


class ShdwObliqueAngle_TypeSub(supermod.ShdwObliqueAngle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwObliqueAngle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwObliqueAngle_Type.subclass = ShdwObliqueAngle_TypeSub
# end class ShdwObliqueAngle_TypeSub


class ShdwScaleFactor_TypeSub(supermod.ShdwScaleFactor_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShdwScaleFactor_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShdwScaleFactor_Type.subclass = ShdwScaleFactor_TypeSub
# end class ShdwScaleFactor_TypeSub


class PageColor_TypeSub(supermod.PageColor_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageColor_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageColor_Type.subclass = PageColor_TypeSub
# end class PageColor_TypeSub


class TextBlock_TypeSub(supermod.TextBlock_Type):
    def __init__(self, Del=None, LeftMargin=None, RightMargin=None, TopMargin=None, BottomMargin=None, VerticalAlign=None, TextBkgnd=None, DefaultTabStop=None, TextDirection=None, TextBkgndTrans=None, **kwargs_):
        super(TextBlock_TypeSub, self).__init__(Del, LeftMargin, RightMargin, TopMargin, BottomMargin, VerticalAlign, TextBkgnd, DefaultTabStop, TextDirection, TextBkgndTrans,  **kwargs_)
supermod.TextBlock_Type.subclass = TextBlock_TypeSub
# end class TextBlock_TypeSub


class LeftMargin_TypeSub(supermod.LeftMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LeftMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LeftMargin_Type.subclass = LeftMargin_TypeSub
# end class LeftMargin_TypeSub


class RightMargin_TypeSub(supermod.RightMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(RightMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.RightMargin_Type.subclass = RightMargin_TypeSub
# end class RightMargin_TypeSub


class TopMargin_TypeSub(supermod.TopMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TopMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TopMargin_Type.subclass = TopMargin_TypeSub
# end class TopMargin_TypeSub


class BottomMargin_TypeSub(supermod.BottomMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BottomMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BottomMargin_Type.subclass = BottomMargin_TypeSub
# end class BottomMargin_TypeSub


class VerticalAlign_TypeSub(supermod.VerticalAlign_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(VerticalAlign_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.VerticalAlign_Type.subclass = VerticalAlign_TypeSub
# end class VerticalAlign_TypeSub


class TextBkgnd_TypeSub(supermod.TextBkgnd_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TextBkgnd_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TextBkgnd_Type.subclass = TextBkgnd_TypeSub
# end class TextBkgnd_TypeSub


class DefaultTabStop_TypeSub(supermod.DefaultTabStop_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DefaultTabStop_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DefaultTabStop_Type.subclass = DefaultTabStop_TypeSub
# end class DefaultTabStop_TypeSub


class TextDirection_TypeSub(supermod.TextDirection_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TextDirection_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TextDirection_Type.subclass = TextDirection_TypeSub
# end class TextDirection_TypeSub


class TextBkgndTrans_TypeSub(supermod.TextBkgndTrans_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TextBkgndTrans_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TextBkgndTrans_Type.subclass = TextBkgndTrans_TypeSub
# end class TextBkgndTrans_TypeSub


class Flags_TypeSub(supermod.Flags_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Flags_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Flags_Type.subclass = Flags_TypeSub
# end class Flags_TypeSub


class DiacriticColor_TypeSub(supermod.DiacriticColor_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DiacriticColor_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DiacriticColor_Type.subclass = DiacriticColor_TypeSub
# end class DiacriticColor_TypeSub


class ExProps_TypeSub(supermod.ExProps_Type):
    def __init__(self, XProp=None, **kwargs_):
        super(ExProps_TypeSub, self).__init__(XProp,  **kwargs_)
supermod.ExProps_Type.subclass = ExProps_TypeSub
# end class ExProps_TypeSub


class TextXForm_TypeSub(supermod.TextXForm_Type):
    def __init__(self, Del=None, TxtPinX=None, TxtPinY=None, TxtWidth=None, TxtHeight=None, TxtLocPinX=None, TxtLocPinY=None, TxtAngle=None, **kwargs_):
        super(TextXForm_TypeSub, self).__init__(Del, TxtPinX, TxtPinY, TxtWidth, TxtHeight, TxtLocPinX, TxtLocPinY, TxtAngle,  **kwargs_)
supermod.TextXForm_Type.subclass = TextXForm_TypeSub
# end class TextXForm_TypeSub


class TxtPinX_TypeSub(supermod.TxtPinX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TxtPinX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TxtPinX_Type.subclass = TxtPinX_TypeSub
# end class TxtPinX_TypeSub


class TxtPinY_TypeSub(supermod.TxtPinY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TxtPinY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TxtPinY_Type.subclass = TxtPinY_TypeSub
# end class TxtPinY_TypeSub


class TxtWidth_TypeSub(supermod.TxtWidth_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TxtWidth_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TxtWidth_Type.subclass = TxtWidth_TypeSub
# end class TxtWidth_TypeSub


class TxtHeight_TypeSub(supermod.TxtHeight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TxtHeight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TxtHeight_Type.subclass = TxtHeight_TypeSub
# end class TxtHeight_TypeSub


class TxtLocPinX_TypeSub(supermod.TxtLocPinX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TxtLocPinX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TxtLocPinX_Type.subclass = TxtLocPinX_TypeSub
# end class TxtLocPinX_TypeSub


class TxtLocPinY_TypeSub(supermod.TxtLocPinY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TxtLocPinY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TxtLocPinY_Type.subclass = TxtLocPinY_TypeSub
# end class TxtLocPinY_TypeSub


class TxtAngle_TypeSub(supermod.TxtAngle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TxtAngle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TxtAngle_Type.subclass = TxtAngle_TypeSub
# end class TxtAngle_TypeSub


class Align_TypeSub(supermod.Align_Type):
    def __init__(self, Del=None, AlignLeft=None, AlignCenter=None, AlignRight=None, AlignTop=None, AlignMiddle=None, AlignBottom=None, **kwargs_):
        super(Align_TypeSub, self).__init__(Del, AlignLeft, AlignCenter, AlignRight, AlignTop, AlignMiddle, AlignBottom,  **kwargs_)
supermod.Align_Type.subclass = Align_TypeSub
# end class Align_TypeSub


class AlignLeft_TypeSub(supermod.AlignLeft_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AlignLeft_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AlignLeft_Type.subclass = AlignLeft_TypeSub
# end class AlignLeft_TypeSub


class AlignCenter_TypeSub(supermod.AlignCenter_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AlignCenter_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AlignCenter_Type.subclass = AlignCenter_TypeSub
# end class AlignCenter_TypeSub


class AlignRight_TypeSub(supermod.AlignRight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AlignRight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AlignRight_Type.subclass = AlignRight_TypeSub
# end class AlignRight_TypeSub


class AlignTop_TypeSub(supermod.AlignTop_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AlignTop_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AlignTop_Type.subclass = AlignTop_TypeSub
# end class AlignTop_TypeSub


class AlignMiddle_TypeSub(supermod.AlignMiddle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AlignMiddle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AlignMiddle_Type.subclass = AlignMiddle_TypeSub
# end class AlignMiddle_TypeSub


class AlignBottom_TypeSub(supermod.AlignBottom_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AlignBottom_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AlignBottom_Type.subclass = AlignBottom_TypeSub
# end class AlignBottom_TypeSub


class Protection_TypeSub(supermod.Protection_Type):
    def __init__(self, Del=None, LockWidth=None, LockHeight=None, LockMoveX=None, LockMoveY=None, LockAspect=None, LockDelete=None, LockBegin=None, LockEnd=None, LockRotate=None, LockCrop=None, LockVtxEdit=None, LockTextEdit=None, LockFormat=None, LockGroup=None, LockCalcWH=None, LockSelect=None, LockCustProp=None, LockFromGroupFormat=None, LockThemeColors=None, LockThemeEffects=None, **kwargs_):
        super(Protection_TypeSub, self).__init__(Del, LockWidth, LockHeight, LockMoveX, LockMoveY, LockAspect, LockDelete, LockBegin, LockEnd, LockRotate, LockCrop, LockVtxEdit, LockTextEdit, LockFormat, LockGroup, LockCalcWH, LockSelect, LockCustProp, LockFromGroupFormat, LockThemeColors, LockThemeEffects,  **kwargs_)
supermod.Protection_Type.subclass = Protection_TypeSub
# end class Protection_TypeSub


class LockWidth_TypeSub(supermod.LockWidth_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockWidth_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockWidth_Type.subclass = LockWidth_TypeSub
# end class LockWidth_TypeSub


class LockHeight_TypeSub(supermod.LockHeight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockHeight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockHeight_Type.subclass = LockHeight_TypeSub
# end class LockHeight_TypeSub


class LockMoveX_TypeSub(supermod.LockMoveX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockMoveX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockMoveX_Type.subclass = LockMoveX_TypeSub
# end class LockMoveX_TypeSub


class LockMoveY_TypeSub(supermod.LockMoveY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockMoveY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockMoveY_Type.subclass = LockMoveY_TypeSub
# end class LockMoveY_TypeSub


class LockAspect_TypeSub(supermod.LockAspect_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockAspect_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockAspect_Type.subclass = LockAspect_TypeSub
# end class LockAspect_TypeSub


class LockDelete_TypeSub(supermod.LockDelete_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockDelete_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockDelete_Type.subclass = LockDelete_TypeSub
# end class LockDelete_TypeSub


class LockBegin_TypeSub(supermod.LockBegin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockBegin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockBegin_Type.subclass = LockBegin_TypeSub
# end class LockBegin_TypeSub


class LockEnd_TypeSub(supermod.LockEnd_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockEnd_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockEnd_Type.subclass = LockEnd_TypeSub
# end class LockEnd_TypeSub


class LockRotate_TypeSub(supermod.LockRotate_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockRotate_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockRotate_Type.subclass = LockRotate_TypeSub
# end class LockRotate_TypeSub


class LockCrop_TypeSub(supermod.LockCrop_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockCrop_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockCrop_Type.subclass = LockCrop_TypeSub
# end class LockCrop_TypeSub


class LockVtxEdit_TypeSub(supermod.LockVtxEdit_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockVtxEdit_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockVtxEdit_Type.subclass = LockVtxEdit_TypeSub
# end class LockVtxEdit_TypeSub


class LockTextEdit_TypeSub(supermod.LockTextEdit_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockTextEdit_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockTextEdit_Type.subclass = LockTextEdit_TypeSub
# end class LockTextEdit_TypeSub


class LockFormat_TypeSub(supermod.LockFormat_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockFormat_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockFormat_Type.subclass = LockFormat_TypeSub
# end class LockFormat_TypeSub


class LockGroup_TypeSub(supermod.LockGroup_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockGroup_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockGroup_Type.subclass = LockGroup_TypeSub
# end class LockGroup_TypeSub


class LockCalcWH_TypeSub(supermod.LockCalcWH_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockCalcWH_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockCalcWH_Type.subclass = LockCalcWH_TypeSub
# end class LockCalcWH_TypeSub


class LockSelect_TypeSub(supermod.LockSelect_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockSelect_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockSelect_Type.subclass = LockSelect_TypeSub
# end class LockSelect_TypeSub


class LockCustProp_TypeSub(supermod.LockCustProp_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockCustProp_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockCustProp_Type.subclass = LockCustProp_TypeSub
# end class LockCustProp_TypeSub


class LockFromGroupFormat_TypeSub(supermod.LockFromGroupFormat_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockFromGroupFormat_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockFromGroupFormat_Type.subclass = LockFromGroupFormat_TypeSub
# end class LockFromGroupFormat_TypeSub


class LockThemeColors_TypeSub(supermod.LockThemeColors_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockThemeColors_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockThemeColors_Type.subclass = LockThemeColors_TypeSub
# end class LockThemeColors_TypeSub


class LockThemeEffects_TypeSub(supermod.LockThemeEffects_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockThemeEffects_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockThemeEffects_Type.subclass = LockThemeEffects_TypeSub
# end class LockThemeEffects_TypeSub


class Help_TypeSub(supermod.Help_Type):
    def __init__(self, Del=None, HelpTopic=None, Copyright=None, **kwargs_):
        super(Help_TypeSub, self).__init__(Del, HelpTopic, Copyright,  **kwargs_)
supermod.Help_Type.subclass = Help_TypeSub
# end class Help_TypeSub


class HelpTopic_TypeSub(supermod.HelpTopic_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(HelpTopic_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.HelpTopic_Type.subclass = HelpTopic_TypeSub
# end class HelpTopic_TypeSub


class Copyright_TypeSub(supermod.Copyright_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Copyright_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Copyright_Type.subclass = Copyright_TypeSub
# end class Copyright_TypeSub


class B_TypeSub(supermod.B_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, SolutionXML=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(B_TypeSub, self).__init__(Unit, F, Err, V, SolutionXML, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.B_Type.subclass = B_TypeSub
# end class B_TypeSub


class Misc_TypeSub(supermod.Misc_Type):
    def __init__(self, Del=None, NoObjHandles=None, NonPrinting=None, NoCtlHandles=None, NoAlignBox=None, UpdateAlignBox=None, HideText=None, DynFeedback=None, GlueType=None, WalkPreference=None, BegTrigger=None, EndTrigger=None, ObjType=None, Comment=None, IsDropSource=None, NoLiveDynamics=None, LocalizeMerge=None, Calendar=None, LangID=None, ShapeKeywords=None, DropOnPageScale=None, **kwargs_):
        super(Misc_TypeSub, self).__init__(Del, NoObjHandles, NonPrinting, NoCtlHandles, NoAlignBox, UpdateAlignBox, HideText, DynFeedback, GlueType, WalkPreference, BegTrigger, EndTrigger, ObjType, Comment, IsDropSource, NoLiveDynamics, LocalizeMerge, Calendar, LangID, ShapeKeywords, DropOnPageScale,  **kwargs_)
supermod.Misc_Type.subclass = Misc_TypeSub
# end class Misc_TypeSub


class NoObjHandles_TypeSub(supermod.NoObjHandles_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoObjHandles_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoObjHandles_Type.subclass = NoObjHandles_TypeSub
# end class NoObjHandles_TypeSub


class NonPrinting_TypeSub(supermod.NonPrinting_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NonPrinting_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NonPrinting_Type.subclass = NonPrinting_TypeSub
# end class NonPrinting_TypeSub


class NoCtlHandles_TypeSub(supermod.NoCtlHandles_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoCtlHandles_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoCtlHandles_Type.subclass = NoCtlHandles_TypeSub
# end class NoCtlHandles_TypeSub


class NoAlignBox_TypeSub(supermod.NoAlignBox_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoAlignBox_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoAlignBox_Type.subclass = NoAlignBox_TypeSub
# end class NoAlignBox_TypeSub


class UpdateAlignBox_TypeSub(supermod.UpdateAlignBox_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UpdateAlignBox_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UpdateAlignBox_Type.subclass = UpdateAlignBox_TypeSub
# end class UpdateAlignBox_TypeSub


class HideText_TypeSub(supermod.HideText_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(HideText_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.HideText_Type.subclass = HideText_TypeSub
# end class HideText_TypeSub


class DynFeedback_TypeSub(supermod.DynFeedback_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DynFeedback_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DynFeedback_Type.subclass = DynFeedback_TypeSub
# end class DynFeedback_TypeSub


class GlueType_TypeSub(supermod.GlueType_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(GlueType_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.GlueType_Type.subclass = GlueType_TypeSub
# end class GlueType_TypeSub


class WalkPreference_TypeSub(supermod.WalkPreference_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(WalkPreference_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.WalkPreference_Type.subclass = WalkPreference_TypeSub
# end class WalkPreference_TypeSub


class BegTrigger_TypeSub(supermod.BegTrigger_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BegTrigger_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BegTrigger_Type.subclass = BegTrigger_TypeSub
# end class BegTrigger_TypeSub


class EndTrigger_TypeSub(supermod.EndTrigger_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EndTrigger_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EndTrigger_Type.subclass = EndTrigger_TypeSub
# end class EndTrigger_TypeSub


class ObjType_TypeSub(supermod.ObjType_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ObjType_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ObjType_Type.subclass = ObjType_TypeSub
# end class ObjType_TypeSub


class Comment_TypeSub(supermod.Comment_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Comment_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Comment_Type.subclass = Comment_TypeSub
# end class Comment_TypeSub


class IsDropSource_TypeSub(supermod.IsDropSource_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(IsDropSource_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.IsDropSource_Type.subclass = IsDropSource_TypeSub
# end class IsDropSource_TypeSub


class NoLiveDynamics_TypeSub(supermod.NoLiveDynamics_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoLiveDynamics_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoLiveDynamics_Type.subclass = NoLiveDynamics_TypeSub
# end class NoLiveDynamics_TypeSub


class LocalizeMerge_TypeSub(supermod.LocalizeMerge_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LocalizeMerge_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LocalizeMerge_Type.subclass = LocalizeMerge_TypeSub
# end class LocalizeMerge_TypeSub


class Calendar_TypeSub(supermod.Calendar_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Calendar_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Calendar_Type.subclass = Calendar_TypeSub
# end class Calendar_TypeSub


class LangID_TypeSub(supermod.LangID_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LangID_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LangID_Type.subclass = LangID_TypeSub
# end class LangID_TypeSub


class ShapeKeywords_TypeSub(supermod.ShapeKeywords_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeKeywords_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeKeywords_Type.subclass = ShapeKeywords_TypeSub
# end class ShapeKeywords_TypeSub


class DropOnPageScale_TypeSub(supermod.DropOnPageScale_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DropOnPageScale_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DropOnPageScale_Type.subclass = DropOnPageScale_TypeSub
# end class DropOnPageScale_TypeSub


class RulerGrid_TypeSub(supermod.RulerGrid_Type):
    def __init__(self, Del=None, XRulerDensity=None, YRulerDensity=None, XRulerOrigin=None, YRulerOrigin=None, XGridDensity=None, YGridDensity=None, XGridSpacing=None, YGridSpacing=None, XGridOrigin=None, YGridOrigin=None, **kwargs_):
        super(RulerGrid_TypeSub, self).__init__(Del, XRulerDensity, YRulerDensity, XRulerOrigin, YRulerOrigin, XGridDensity, YGridDensity, XGridSpacing, YGridSpacing, XGridOrigin, YGridOrigin,  **kwargs_)
supermod.RulerGrid_Type.subclass = RulerGrid_TypeSub
# end class RulerGrid_TypeSub


class XRulerDensity_TypeSub(supermod.XRulerDensity_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XRulerDensity_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XRulerDensity_Type.subclass = XRulerDensity_TypeSub
# end class XRulerDensity_TypeSub


class YRulerDensity_TypeSub(supermod.YRulerDensity_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YRulerDensity_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YRulerDensity_Type.subclass = YRulerDensity_TypeSub
# end class YRulerDensity_TypeSub


class XRulerOrigin_TypeSub(supermod.XRulerOrigin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XRulerOrigin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XRulerOrigin_Type.subclass = XRulerOrigin_TypeSub
# end class XRulerOrigin_TypeSub


class YRulerOrigin_TypeSub(supermod.YRulerOrigin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YRulerOrigin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YRulerOrigin_Type.subclass = YRulerOrigin_TypeSub
# end class YRulerOrigin_TypeSub


class XGridDensity_TypeSub(supermod.XGridDensity_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XGridDensity_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XGridDensity_Type.subclass = XGridDensity_TypeSub
# end class XGridDensity_TypeSub


class YGridDensity_TypeSub(supermod.YGridDensity_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YGridDensity_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YGridDensity_Type.subclass = YGridDensity_TypeSub
# end class YGridDensity_TypeSub


class XGridSpacing_TypeSub(supermod.XGridSpacing_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XGridSpacing_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XGridSpacing_Type.subclass = XGridSpacing_TypeSub
# end class XGridSpacing_TypeSub


class YGridSpacing_TypeSub(supermod.YGridSpacing_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YGridSpacing_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YGridSpacing_Type.subclass = YGridSpacing_TypeSub
# end class YGridSpacing_TypeSub


class XGridOrigin_TypeSub(supermod.XGridOrigin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XGridOrigin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XGridOrigin_Type.subclass = XGridOrigin_TypeSub
# end class XGridOrigin_TypeSub


class YGridOrigin_TypeSub(supermod.YGridOrigin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YGridOrigin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YGridOrigin_Type.subclass = YGridOrigin_TypeSub
# end class YGridOrigin_TypeSub


class Hyperlink5_TypeSub(supermod.Hyperlink5_Type):
    def __init__(self, **kwargs_):
        super(Hyperlink5_TypeSub, self).__init__( **kwargs_)
supermod.Hyperlink5_Type.subclass = Hyperlink5_TypeSub
# end class Hyperlink5_TypeSub


class Description_TypeSub(supermod.Description_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Description_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Description_Type.subclass = Description_TypeSub
# end class Description_TypeSub


class Address_TypeSub(supermod.Address_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Address_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Address_Type.subclass = Address_TypeSub
# end class Address_TypeSub


class SubAddress_TypeSub(supermod.SubAddress_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(SubAddress_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.SubAddress_Type.subclass = SubAddress_TypeSub
# end class SubAddress_TypeSub


class ExtraInfo_TypeSub(supermod.ExtraInfo_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ExtraInfo_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ExtraInfo_Type.subclass = ExtraInfo_TypeSub
# end class ExtraInfo_TypeSub


class Frame_TypeSub(supermod.Frame_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Frame_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Frame_Type.subclass = Frame_TypeSub
# end class Frame_TypeSub


class NewWindow_TypeSub(supermod.NewWindow_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NewWindow_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NewWindow_Type.subclass = NewWindow_TypeSub
# end class NewWindow_TypeSub


class Default_TypeSub(supermod.Default_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Default_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Default_Type.subclass = Default_TypeSub
# end class Default_TypeSub


class Invisible_TypeSub(supermod.Invisible_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Invisible_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Invisible_Type.subclass = Invisible_TypeSub
# end class Invisible_TypeSub


class SortKey_TypeSub(supermod.SortKey_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(SortKey_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.SortKey_Type.subclass = SortKey_TypeSub
# end class SortKey_TypeSub


class DocProps_TypeSub(supermod.DocProps_Type):
    def __init__(self, Del=None, OutputFormat=None, LockPreview=None, AddMarkup=None, ViewMarkup=None, PreviewQuality=None, PreviewScope=None, DocLangID=None, **kwargs_):
        super(DocProps_TypeSub, self).__init__(Del, OutputFormat, LockPreview, AddMarkup, ViewMarkup, PreviewQuality, PreviewScope, DocLangID,  **kwargs_)
supermod.DocProps_Type.subclass = DocProps_TypeSub
# end class DocProps_TypeSub


class OutputFormat_TypeSub(supermod.OutputFormat_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(OutputFormat_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.OutputFormat_Type.subclass = OutputFormat_TypeSub
# end class OutputFormat_TypeSub


class LockPreview_TypeSub(supermod.LockPreview_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LockPreview_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LockPreview_Type.subclass = LockPreview_TypeSub
# end class LockPreview_TypeSub


class AddMarkup_TypeSub(supermod.AddMarkup_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AddMarkup_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AddMarkup_Type.subclass = AddMarkup_TypeSub
# end class AddMarkup_TypeSub


class ViewMarkup_TypeSub(supermod.ViewMarkup_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ViewMarkup_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ViewMarkup_Type.subclass = ViewMarkup_TypeSub
# end class ViewMarkup_TypeSub


class PreviewQuality_TypeSub(supermod.PreviewQuality_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PreviewQuality_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PreviewQuality_Type.subclass = PreviewQuality_TypeSub
# end class PreviewQuality_TypeSub


class PreviewScope_TypeSub(supermod.PreviewScope_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PreviewScope_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PreviewScope_Type.subclass = PreviewScope_TypeSub
# end class PreviewScope_TypeSub


class DocLangID_TypeSub(supermod.DocLangID_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DocLangID_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DocLangID_Type.subclass = DocLangID_TypeSub
# end class DocLangID_TypeSub


class TextFlags_TypeSub(supermod.TextFlags_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TextFlags_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TextFlags_Type.subclass = TextFlags_TypeSub
# end class TextFlags_TypeSub


class DocExProps_TypeSub(supermod.DocExProps_Type):
    def __init__(self, XProp=None, **kwargs_):
        super(DocExProps_TypeSub, self).__init__(XProp,  **kwargs_)
supermod.DocExProps_Type.subclass = DocExProps_TypeSub
# end class DocExProps_TypeSub


class Image_TypeSub(supermod.Image_Type):
    def __init__(self, Del=None, Gamma=None, Contrast=None, Brightness=None, Sharpen=None, Blur=None, Denoise=None, Transparency=None, **kwargs_):
        super(Image_TypeSub, self).__init__(Del, Gamma, Contrast, Brightness, Sharpen, Blur, Denoise, Transparency,  **kwargs_)
supermod.Image_Type.subclass = Image_TypeSub
# end class Image_TypeSub


class Gamma_TypeSub(supermod.Gamma_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Gamma_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Gamma_Type.subclass = Gamma_TypeSub
# end class Gamma_TypeSub


class Contrast_TypeSub(supermod.Contrast_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Contrast_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Contrast_Type.subclass = Contrast_TypeSub
# end class Contrast_TypeSub


class Brightness_TypeSub(supermod.Brightness_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Brightness_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Brightness_Type.subclass = Brightness_TypeSub
# end class Brightness_TypeSub


class Sharpen_TypeSub(supermod.Sharpen_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Sharpen_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Sharpen_Type.subclass = Sharpen_TypeSub
# end class Sharpen_TypeSub


class Blur_TypeSub(supermod.Blur_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Blur_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Blur_Type.subclass = Blur_TypeSub
# end class Blur_TypeSub


class Denoise_TypeSub(supermod.Denoise_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Denoise_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Denoise_Type.subclass = Denoise_TypeSub
# end class Denoise_TypeSub


class Transparency_TypeSub(supermod.Transparency_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Transparency_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Transparency_Type.subclass = Transparency_TypeSub
# end class Transparency_TypeSub


class Group_TypeSub(supermod.Group_Type):
    def __init__(self, Del=None, SelectMode=None, DisplayMode=None, IsDropTarget=None, IsSnapTarget=None, IsTextEditTarget=None, DontMoveChildren=None, **kwargs_):
        super(Group_TypeSub, self).__init__(Del, SelectMode, DisplayMode, IsDropTarget, IsSnapTarget, IsTextEditTarget, DontMoveChildren,  **kwargs_)
supermod.Group_Type.subclass = Group_TypeSub
# end class Group_TypeSub


class SelectMode_TypeSub(supermod.SelectMode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(SelectMode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.SelectMode_Type.subclass = SelectMode_TypeSub
# end class SelectMode_TypeSub


class DisplayMode_TypeSub(supermod.DisplayMode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DisplayMode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DisplayMode_Type.subclass = DisplayMode_TypeSub
# end class DisplayMode_TypeSub


class IsDropTarget_TypeSub(supermod.IsDropTarget_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(IsDropTarget_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.IsDropTarget_Type.subclass = IsDropTarget_TypeSub
# end class IsDropTarget_TypeSub


class IsSnapTarget_TypeSub(supermod.IsSnapTarget_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(IsSnapTarget_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.IsSnapTarget_Type.subclass = IsSnapTarget_TypeSub
# end class IsSnapTarget_TypeSub


class IsTextEditTarget_TypeSub(supermod.IsTextEditTarget_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(IsTextEditTarget_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.IsTextEditTarget_Type.subclass = IsTextEditTarget_TypeSub
# end class IsTextEditTarget_TypeSub


class DontMoveChildren_TypeSub(supermod.DontMoveChildren_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DontMoveChildren_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DontMoveChildren_Type.subclass = DontMoveChildren_TypeSub
# end class DontMoveChildren_TypeSub


class Layout_TypeSub(supermod.Layout_Type):
    def __init__(self, Del=None, ShapePermeableX=None, ShapePermeableY=None, ShapePermeablePlace=None, ShapeFixedCode=None, ShapePlowCode=None, ShapeRouteStyle=None, ShapePlaceStyle=None, ConFixedCode=None, ConLineJumpCode=None, ConLineJumpStyle=None, ConLineJumpDirX=None, ConLineJumpDirY=None, ShapePlaceFlip=None, ConLineRouteExt=None, ShapeSplit=None, ShapeSplittable=None, DisplayLevel=None, Relationships=None, **kwargs_):
        super(Layout_TypeSub, self).__init__(Del, ShapePermeableX, ShapePermeableY, ShapePermeablePlace, ShapeFixedCode, ShapePlowCode, ShapeRouteStyle, ShapePlaceStyle, ConFixedCode, ConLineJumpCode, ConLineJumpStyle, ConLineJumpDirX, ConLineJumpDirY, ShapePlaceFlip, ConLineRouteExt, ShapeSplit, ShapeSplittable, DisplayLevel, Relationships,  **kwargs_)
supermod.Layout_Type.subclass = Layout_TypeSub
# end class Layout_TypeSub


class ShapePermeableX_TypeSub(supermod.ShapePermeableX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapePermeableX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapePermeableX_Type.subclass = ShapePermeableX_TypeSub
# end class ShapePermeableX_TypeSub


class ShapePermeableY_TypeSub(supermod.ShapePermeableY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapePermeableY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapePermeableY_Type.subclass = ShapePermeableY_TypeSub
# end class ShapePermeableY_TypeSub


class ShapePermeablePlace_TypeSub(supermod.ShapePermeablePlace_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapePermeablePlace_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapePermeablePlace_Type.subclass = ShapePermeablePlace_TypeSub
# end class ShapePermeablePlace_TypeSub


class ShapeFixedCode_TypeSub(supermod.ShapeFixedCode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeFixedCode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeFixedCode_Type.subclass = ShapeFixedCode_TypeSub
# end class ShapeFixedCode_TypeSub


class ShapePlowCode_TypeSub(supermod.ShapePlowCode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapePlowCode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapePlowCode_Type.subclass = ShapePlowCode_TypeSub
# end class ShapePlowCode_TypeSub


class ShapeRouteStyle_TypeSub(supermod.ShapeRouteStyle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeRouteStyle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeRouteStyle_Type.subclass = ShapeRouteStyle_TypeSub
# end class ShapeRouteStyle_TypeSub


class ShapePlaceStyle_TypeSub(supermod.ShapePlaceStyle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapePlaceStyle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapePlaceStyle_Type.subclass = ShapePlaceStyle_TypeSub
# end class ShapePlaceStyle_TypeSub


class ConFixedCode_TypeSub(supermod.ConFixedCode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ConFixedCode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ConFixedCode_Type.subclass = ConFixedCode_TypeSub
# end class ConFixedCode_TypeSub


class ConLineJumpCode_TypeSub(supermod.ConLineJumpCode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ConLineJumpCode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ConLineJumpCode_Type.subclass = ConLineJumpCode_TypeSub
# end class ConLineJumpCode_TypeSub


class ConLineJumpStyle_TypeSub(supermod.ConLineJumpStyle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ConLineJumpStyle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ConLineJumpStyle_Type.subclass = ConLineJumpStyle_TypeSub
# end class ConLineJumpStyle_TypeSub


class ConLineJumpDirX_TypeSub(supermod.ConLineJumpDirX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ConLineJumpDirX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ConLineJumpDirX_Type.subclass = ConLineJumpDirX_TypeSub
# end class ConLineJumpDirX_TypeSub


class ConLineJumpDirY_TypeSub(supermod.ConLineJumpDirY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ConLineJumpDirY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ConLineJumpDirY_Type.subclass = ConLineJumpDirY_TypeSub
# end class ConLineJumpDirY_TypeSub


class ShapePlaceFlip_TypeSub(supermod.ShapePlaceFlip_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapePlaceFlip_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapePlaceFlip_Type.subclass = ShapePlaceFlip_TypeSub
# end class ShapePlaceFlip_TypeSub


class ConLineRouteExt_TypeSub(supermod.ConLineRouteExt_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ConLineRouteExt_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ConLineRouteExt_Type.subclass = ConLineRouteExt_TypeSub
# end class ConLineRouteExt_TypeSub


class ShapeSplit_TypeSub(supermod.ShapeSplit_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeSplit_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeSplit_Type.subclass = ShapeSplit_TypeSub
# end class ShapeSplit_TypeSub


class ShapeSplittable_TypeSub(supermod.ShapeSplittable_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ShapeSplittable_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ShapeSplittable_Type.subclass = ShapeSplittable_TypeSub
# end class ShapeSplittable_TypeSub


class DisplayLevel_TypeSub(supermod.DisplayLevel_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DisplayLevel_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DisplayLevel_Type.subclass = DisplayLevel_TypeSub
# end class DisplayLevel_TypeSub


class Relationships_TypeSub(supermod.Relationships_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Relationships_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Relationships_Type.subclass = Relationships_TypeSub
# end class Relationships_TypeSub


class PageLayout_TypeSub(supermod.PageLayout_Type):
    def __init__(self, Del=None, ResizePage=None, EnableGrid=None, DynamicsOff=None, CtrlAsInput=None, AvoidPageBreaks=None, PlaceStyle=None, RouteStyle=None, PlaceDepth=None, PlowCode=None, LineJumpCode=None, LineJumpStyle=None, PageLineJumpDirX=None, PageLineJumpDirY=None, LineToNodeX=None, LineToNodeY=None, BlockSizeX=None, BlockSizeY=None, AvenueSizeX=None, AvenueSizeY=None, LineToLineX=None, LineToLineY=None, LineJumpFactorX=None, LineJumpFactorY=None, LineAdjustFrom=None, LineAdjustTo=None, PlaceFlip=None, LineRouteExt=None, PageShapeSplit=None, **kwargs_):
        super(PageLayout_TypeSub, self).__init__(Del, ResizePage, EnableGrid, DynamicsOff, CtrlAsInput, AvoidPageBreaks, PlaceStyle, RouteStyle, PlaceDepth, PlowCode, LineJumpCode, LineJumpStyle, PageLineJumpDirX, PageLineJumpDirY, LineToNodeX, LineToNodeY, BlockSizeX, BlockSizeY, AvenueSizeX, AvenueSizeY, LineToLineX, LineToLineY, LineJumpFactorX, LineJumpFactorY, LineAdjustFrom, LineAdjustTo, PlaceFlip, LineRouteExt, PageShapeSplit,  **kwargs_)
supermod.PageLayout_Type.subclass = PageLayout_TypeSub
# end class PageLayout_TypeSub


class ResizePage_TypeSub(supermod.ResizePage_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ResizePage_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ResizePage_Type.subclass = ResizePage_TypeSub
# end class ResizePage_TypeSub


class EnableGrid_TypeSub(supermod.EnableGrid_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EnableGrid_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EnableGrid_Type.subclass = EnableGrid_TypeSub
# end class EnableGrid_TypeSub


class DynamicsOff_TypeSub(supermod.DynamicsOff_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DynamicsOff_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DynamicsOff_Type.subclass = DynamicsOff_TypeSub
# end class DynamicsOff_TypeSub


class CtrlAsInput_TypeSub(supermod.CtrlAsInput_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(CtrlAsInput_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.CtrlAsInput_Type.subclass = CtrlAsInput_TypeSub
# end class CtrlAsInput_TypeSub


class AvoidPageBreaks_TypeSub(supermod.AvoidPageBreaks_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AvoidPageBreaks_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AvoidPageBreaks_Type.subclass = AvoidPageBreaks_TypeSub
# end class AvoidPageBreaks_TypeSub


class PlaceStyle_TypeSub(supermod.PlaceStyle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PlaceStyle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PlaceStyle_Type.subclass = PlaceStyle_TypeSub
# end class PlaceStyle_TypeSub


class RouteStyle_TypeSub(supermod.RouteStyle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(RouteStyle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.RouteStyle_Type.subclass = RouteStyle_TypeSub
# end class RouteStyle_TypeSub


class PlaceDepth_TypeSub(supermod.PlaceDepth_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PlaceDepth_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PlaceDepth_Type.subclass = PlaceDepth_TypeSub
# end class PlaceDepth_TypeSub


class PlowCode_TypeSub(supermod.PlowCode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PlowCode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PlowCode_Type.subclass = PlowCode_TypeSub
# end class PlowCode_TypeSub


class LineJumpCode_TypeSub(supermod.LineJumpCode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineJumpCode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineJumpCode_Type.subclass = LineJumpCode_TypeSub
# end class LineJumpCode_TypeSub


class LineJumpStyle_TypeSub(supermod.LineJumpStyle_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineJumpStyle_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineJumpStyle_Type.subclass = LineJumpStyle_TypeSub
# end class LineJumpStyle_TypeSub


class PageLineJumpDirX_TypeSub(supermod.PageLineJumpDirX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageLineJumpDirX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageLineJumpDirX_Type.subclass = PageLineJumpDirX_TypeSub
# end class PageLineJumpDirX_TypeSub


class PageLineJumpDirY_TypeSub(supermod.PageLineJumpDirY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageLineJumpDirY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageLineJumpDirY_Type.subclass = PageLineJumpDirY_TypeSub
# end class PageLineJumpDirY_TypeSub


class LineToNodeX_TypeSub(supermod.LineToNodeX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineToNodeX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineToNodeX_Type.subclass = LineToNodeX_TypeSub
# end class LineToNodeX_TypeSub


class LineToNodeY_TypeSub(supermod.LineToNodeY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineToNodeY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineToNodeY_Type.subclass = LineToNodeY_TypeSub
# end class LineToNodeY_TypeSub


class BlockSizeX_TypeSub(supermod.BlockSizeX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BlockSizeX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BlockSizeX_Type.subclass = BlockSizeX_TypeSub
# end class BlockSizeX_TypeSub


class BlockSizeY_TypeSub(supermod.BlockSizeY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BlockSizeY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BlockSizeY_Type.subclass = BlockSizeY_TypeSub
# end class BlockSizeY_TypeSub


class AvenueSizeX_TypeSub(supermod.AvenueSizeX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AvenueSizeX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AvenueSizeX_Type.subclass = AvenueSizeX_TypeSub
# end class AvenueSizeX_TypeSub


class AvenueSizeY_TypeSub(supermod.AvenueSizeY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AvenueSizeY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AvenueSizeY_Type.subclass = AvenueSizeY_TypeSub
# end class AvenueSizeY_TypeSub


class LineToLineX_TypeSub(supermod.LineToLineX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineToLineX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineToLineX_Type.subclass = LineToLineX_TypeSub
# end class LineToLineX_TypeSub


class LineToLineY_TypeSub(supermod.LineToLineY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineToLineY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineToLineY_Type.subclass = LineToLineY_TypeSub
# end class LineToLineY_TypeSub


class LineJumpFactorX_TypeSub(supermod.LineJumpFactorX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineJumpFactorX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineJumpFactorX_Type.subclass = LineJumpFactorX_TypeSub
# end class LineJumpFactorX_TypeSub


class LineJumpFactorY_TypeSub(supermod.LineJumpFactorY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineJumpFactorY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineJumpFactorY_Type.subclass = LineJumpFactorY_TypeSub
# end class LineJumpFactorY_TypeSub


class LineAdjustFrom_TypeSub(supermod.LineAdjustFrom_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineAdjustFrom_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineAdjustFrom_Type.subclass = LineAdjustFrom_TypeSub
# end class LineAdjustFrom_TypeSub


class LineAdjustTo_TypeSub(supermod.LineAdjustTo_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineAdjustTo_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineAdjustTo_Type.subclass = LineAdjustTo_TypeSub
# end class LineAdjustTo_TypeSub


class PlaceFlip_TypeSub(supermod.PlaceFlip_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PlaceFlip_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PlaceFlip_Type.subclass = PlaceFlip_TypeSub
# end class PlaceFlip_TypeSub


class LineRouteExt_TypeSub(supermod.LineRouteExt_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LineRouteExt_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LineRouteExt_Type.subclass = LineRouteExt_TypeSub
# end class LineRouteExt_TypeSub


class PageShapeSplit_TypeSub(supermod.PageShapeSplit_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageShapeSplit_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageShapeSplit_Type.subclass = PageShapeSplit_TypeSub
# end class PageShapeSplit_TypeSub


class PrintProps_TypeSub(supermod.PrintProps_Type):
    def __init__(self, Del=None, PageLeftMargin=None, PageRightMargin=None, PageTopMargin=None, PageBottomMargin=None, ScaleX=None, ScaleY=None, PagesX=None, PagesY=None, CenterX=None, CenterY=None, OnPage=None, PrintGrid=None, PrintPageOrientation=None, PaperKind=None, PaperSource=None, **kwargs_):
        super(PrintProps_TypeSub, self).__init__(Del, PageLeftMargin, PageRightMargin, PageTopMargin, PageBottomMargin, ScaleX, ScaleY, PagesX, PagesY, CenterX, CenterY, OnPage, PrintGrid, PrintPageOrientation, PaperKind, PaperSource,  **kwargs_)
supermod.PrintProps_Type.subclass = PrintProps_TypeSub
# end class PrintProps_TypeSub


class PageLeftMargin_TypeSub(supermod.PageLeftMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageLeftMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageLeftMargin_Type.subclass = PageLeftMargin_TypeSub
# end class PageLeftMargin_TypeSub


class PageRightMargin_TypeSub(supermod.PageRightMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageRightMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageRightMargin_Type.subclass = PageRightMargin_TypeSub
# end class PageRightMargin_TypeSub


class PageTopMargin_TypeSub(supermod.PageTopMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageTopMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageTopMargin_Type.subclass = PageTopMargin_TypeSub
# end class PageTopMargin_TypeSub


class PageBottomMargin_TypeSub(supermod.PageBottomMargin_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PageBottomMargin_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PageBottomMargin_Type.subclass = PageBottomMargin_TypeSub
# end class PageBottomMargin_TypeSub


class ScaleX_TypeSub(supermod.ScaleX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ScaleX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ScaleX_Type.subclass = ScaleX_TypeSub
# end class ScaleX_TypeSub


class ScaleY_TypeSub(supermod.ScaleY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ScaleY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ScaleY_Type.subclass = ScaleY_TypeSub
# end class ScaleY_TypeSub


class PagesX_TypeSub(supermod.PagesX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PagesX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PagesX_Type.subclass = PagesX_TypeSub
# end class PagesX_TypeSub


class PagesY_TypeSub(supermod.PagesY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PagesY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PagesY_Type.subclass = PagesY_TypeSub
# end class PagesY_TypeSub


class CenterX_TypeSub(supermod.CenterX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(CenterX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.CenterX_Type.subclass = CenterX_TypeSub
# end class CenterX_TypeSub


class CenterY_TypeSub(supermod.CenterY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(CenterY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.CenterY_Type.subclass = CenterY_TypeSub
# end class CenterY_TypeSub


class OnPage_TypeSub(supermod.OnPage_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(OnPage_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.OnPage_Type.subclass = OnPage_TypeSub
# end class OnPage_TypeSub


class PrintGrid_TypeSub(supermod.PrintGrid_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PrintGrid_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PrintGrid_Type.subclass = PrintGrid_TypeSub
# end class PrintGrid_TypeSub


class PrintPageOrientation_TypeSub(supermod.PrintPageOrientation_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PrintPageOrientation_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PrintPageOrientation_Type.subclass = PrintPageOrientation_TypeSub
# end class PrintPageOrientation_TypeSub


class PaperKind_TypeSub(supermod.PaperKind_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PaperKind_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PaperKind_Type.subclass = PaperKind_TypeSub
# end class PaperKind_TypeSub


class PaperSource_TypeSub(supermod.PaperSource_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(PaperSource_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.PaperSource_Type.subclass = PaperSource_TypeSub
# end class PaperSource_TypeSub


class Char_TypeSub(supermod.Char_Type):
    def __init__(self, IX=None, Del=None, Font=None, Color=None, Style=None, Case=None, Pos=None, FontScale=None, Locale=None, Size=None, DblUnderline=None, Overline=None, Strikethru=None, Highlight=None, Perpendicular=None, DoubleStrikethrough=None, RTLText=None, UseVertical=None, Letterspace=None, ColorTrans=None, AsianFont=None, ComplexScriptFont=None, LocalizeFont=None, ComplexScriptSize=None, LangID=None, **kwargs_):
        super(Char_TypeSub, self).__init__(IX, Del, Font, Color, Style, Case, Pos, FontScale, Locale, Size, DblUnderline, Overline, Strikethru, Highlight, Perpendicular, DoubleStrikethrough, RTLText, UseVertical, Letterspace, ColorTrans, AsianFont, ComplexScriptFont, LocalizeFont, ComplexScriptSize, LangID,  **kwargs_)
supermod.Char_Type.subclass = Char_TypeSub
# end class Char_TypeSub


class Font_TypeSub(supermod.Font_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Font_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Font_Type.subclass = Font_TypeSub
# end class Font_TypeSub


class Color_TypeSub(supermod.Color_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Color_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Color_Type.subclass = Color_TypeSub
# end class Color_TypeSub


class Style_TypeSub(supermod.Style_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Style_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Style_Type.subclass = Style_TypeSub
# end class Style_TypeSub


class Case_TypeSub(supermod.Case_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Case_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Case_Type.subclass = Case_TypeSub
# end class Case_TypeSub


class Pos_TypeSub(supermod.Pos_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Pos_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Pos_Type.subclass = Pos_TypeSub
# end class Pos_TypeSub


class FontScale_TypeSub(supermod.FontScale_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FontScale_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FontScale_Type.subclass = FontScale_TypeSub
# end class FontScale_TypeSub


class Locale_TypeSub(supermod.Locale_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Locale_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Locale_Type.subclass = Locale_TypeSub
# end class Locale_TypeSub


class Size_TypeSub(supermod.Size_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Size_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Size_Type.subclass = Size_TypeSub
# end class Size_TypeSub


class DblUnderline_TypeSub(supermod.DblUnderline_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DblUnderline_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DblUnderline_Type.subclass = DblUnderline_TypeSub
# end class DblUnderline_TypeSub


class Overline_TypeSub(supermod.Overline_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Overline_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Overline_Type.subclass = Overline_TypeSub
# end class Overline_TypeSub


class Strikethru_TypeSub(supermod.Strikethru_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Strikethru_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Strikethru_Type.subclass = Strikethru_TypeSub
# end class Strikethru_TypeSub


class Highlight_TypeSub(supermod.Highlight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Highlight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Highlight_Type.subclass = Highlight_TypeSub
# end class Highlight_TypeSub


class Perpendicular_TypeSub(supermod.Perpendicular_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Perpendicular_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Perpendicular_Type.subclass = Perpendicular_TypeSub
# end class Perpendicular_TypeSub


class DoubleStrikethrough_TypeSub(supermod.DoubleStrikethrough_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DoubleStrikethrough_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DoubleStrikethrough_Type.subclass = DoubleStrikethrough_TypeSub
# end class DoubleStrikethrough_TypeSub


class RTLText_TypeSub(supermod.RTLText_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(RTLText_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.RTLText_Type.subclass = RTLText_TypeSub
# end class RTLText_TypeSub


class UseVertical_TypeSub(supermod.UseVertical_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UseVertical_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UseVertical_Type.subclass = UseVertical_TypeSub
# end class UseVertical_TypeSub


class Letterspace_TypeSub(supermod.Letterspace_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Letterspace_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Letterspace_Type.subclass = Letterspace_TypeSub
# end class Letterspace_TypeSub


class ColorTrans_TypeSub(supermod.ColorTrans_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ColorTrans_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ColorTrans_Type.subclass = ColorTrans_TypeSub
# end class ColorTrans_TypeSub


class Hidden_TypeSub(supermod.Hidden_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Hidden_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Hidden_Type.subclass = Hidden_TypeSub
# end class Hidden_TypeSub


class UseKerning_TypeSub(supermod.UseKerning_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UseKerning_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UseKerning_Type.subclass = UseKerning_TypeSub
# end class UseKerning_TypeSub


class UseNationalDigit_TypeSub(supermod.UseNationalDigit_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UseNationalDigit_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UseNationalDigit_Type.subclass = UseNationalDigit_TypeSub
# end class UseNationalDigit_TypeSub


class NoBreak_TypeSub(supermod.NoBreak_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoBreak_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoBreak_Type.subclass = NoBreak_TypeSub
# end class NoBreak_TypeSub


class Outline_TypeSub(supermod.Outline_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Outline_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Outline_Type.subclass = Outline_TypeSub
# end class Outline_TypeSub


class NoHyphenate_TypeSub(supermod.NoHyphenate_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoHyphenate_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoHyphenate_Type.subclass = NoHyphenate_TypeSub
# end class NoHyphenate_TypeSub


class FontDirection_TypeSub(supermod.FontDirection_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FontDirection_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FontDirection_Type.subclass = FontDirection_TypeSub
# end class FontDirection_TypeSub


class Spelling_TypeSub(supermod.Spelling_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Spelling_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Spelling_Type.subclass = Spelling_TypeSub
# end class Spelling_TypeSub


class Grammar_TypeSub(supermod.Grammar_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Grammar_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Grammar_Type.subclass = Grammar_TypeSub
# end class Grammar_TypeSub


class Inconsistent_TypeSub(supermod.Inconsistent_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Inconsistent_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Inconsistent_Type.subclass = Inconsistent_TypeSub
# end class Inconsistent_TypeSub


class SmartTag_TypeSub(supermod.SmartTag_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(SmartTag_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.SmartTag_Type.subclass = SmartTag_TypeSub
# end class SmartTag_TypeSub


class AsianFont_TypeSub(supermod.AsianFont_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AsianFont_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AsianFont_Type.subclass = AsianFont_TypeSub
# end class AsianFont_TypeSub


class ComplexScriptFont_TypeSub(supermod.ComplexScriptFont_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ComplexScriptFont_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ComplexScriptFont_Type.subclass = ComplexScriptFont_TypeSub
# end class ComplexScriptFont_TypeSub


class LocalizeFont_TypeSub(supermod.LocalizeFont_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LocalizeFont_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LocalizeFont_Type.subclass = LocalizeFont_TypeSub
# end class LocalizeFont_TypeSub


class ComplexScriptSize_TypeSub(supermod.ComplexScriptSize_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ComplexScriptSize_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ComplexScriptSize_Type.subclass = ComplexScriptSize_TypeSub
# end class ComplexScriptSize_TypeSub


class FontPosition_TypeSub(supermod.FontPosition_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FontPosition_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FontPosition_Type.subclass = FontPosition_TypeSub
# end class FontPosition_TypeSub


class Para_TypeSub(supermod.Para_Type):
    def __init__(self, IX=None, Del=None, IndFirst=None, IndLeft=None, IndRight=None, SpLine=None, SpBefore=None, SpAfter=None, HorzAlign=None, Bullet=None, BulletStr=None, BulletFont=None, LocalizeBulletFont=None, BulletFontSize=None, TextPosAfterBullet=None, Flags=None, **kwargs_):
        super(Para_TypeSub, self).__init__(IX, Del, IndFirst, IndLeft, IndRight, SpLine, SpBefore, SpAfter, HorzAlign, Bullet, BulletStr, BulletFont, LocalizeBulletFont, BulletFontSize, TextPosAfterBullet, Flags,  **kwargs_)
supermod.Para_Type.subclass = Para_TypeSub
# end class Para_TypeSub


class IndFirst_TypeSub(supermod.IndFirst_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(IndFirst_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.IndFirst_Type.subclass = IndFirst_TypeSub
# end class IndFirst_TypeSub


class IndLeft_TypeSub(supermod.IndLeft_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(IndLeft_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.IndLeft_Type.subclass = IndLeft_TypeSub
# end class IndLeft_TypeSub


class IndRight_TypeSub(supermod.IndRight_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(IndRight_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.IndRight_Type.subclass = IndRight_TypeSub
# end class IndRight_TypeSub


class SpLine_TypeSub(supermod.SpLine_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(SpLine_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.SpLine_Type.subclass = SpLine_TypeSub
# end class SpLine_TypeSub


class SpBefore_TypeSub(supermod.SpBefore_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(SpBefore_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.SpBefore_Type.subclass = SpBefore_TypeSub
# end class SpBefore_TypeSub


class SpAfter_TypeSub(supermod.SpAfter_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(SpAfter_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.SpAfter_Type.subclass = SpAfter_TypeSub
# end class SpAfter_TypeSub


class HorzAlign_TypeSub(supermod.HorzAlign_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(HorzAlign_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.HorzAlign_Type.subclass = HorzAlign_TypeSub
# end class HorzAlign_TypeSub


class Bullet_TypeSub(supermod.Bullet_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Bullet_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Bullet_Type.subclass = Bullet_TypeSub
# end class Bullet_TypeSub


class BulletStr_TypeSub(supermod.BulletStr_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BulletStr_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BulletStr_Type.subclass = BulletStr_TypeSub
# end class BulletStr_TypeSub


class BulletFont_TypeSub(supermod.BulletFont_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BulletFont_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BulletFont_Type.subclass = BulletFont_TypeSub
# end class BulletFont_TypeSub


class LocalizeBulletFont_TypeSub(supermod.LocalizeBulletFont_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(LocalizeBulletFont_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.LocalizeBulletFont_Type.subclass = LocalizeBulletFont_TypeSub
# end class LocalizeBulletFont_TypeSub


class BulletFontSize_TypeSub(supermod.BulletFontSize_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BulletFontSize_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BulletFontSize_Type.subclass = BulletFontSize_TypeSub
# end class BulletFontSize_TypeSub


class TextPosAfterBullet_TypeSub(supermod.TextPosAfterBullet_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TextPosAfterBullet_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TextPosAfterBullet_Type.subclass = TextPosAfterBullet_TypeSub
# end class TextPosAfterBullet_TypeSub


class Tabs_TypeSub(supermod.Tabs_Type):
    def __init__(self, IX=None, Del=None, Tab=None, **kwargs_):
        super(Tabs_TypeSub, self).__init__(IX, Del, Tab,  **kwargs_)
supermod.Tabs_Type.subclass = Tabs_TypeSub
# end class Tabs_TypeSub


class Tab_TypeSub(supermod.Tab_Type):
    def __init__(self, IX=None, Position=None, Alignment=None, Leader=None, **kwargs_):
        super(Tab_TypeSub, self).__init__(IX, Position, Alignment, Leader,  **kwargs_)
supermod.Tab_Type.subclass = Tab_TypeSub
# end class Tab_TypeSub


class Position_TypeSub(supermod.Position_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Position_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Position_Type.subclass = Position_TypeSub
# end class Position_TypeSub


class Alignment_TypeSub(supermod.Alignment_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Alignment_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Alignment_Type.subclass = Alignment_TypeSub
# end class Alignment_TypeSub


class Leader_TypeSub(supermod.Leader_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Leader_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Leader_Type.subclass = Leader_TypeSub
# end class Leader_TypeSub


class Scratch_TypeSub(supermod.Scratch_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, B=None, C=None, D=None, **kwargs_):
        super(Scratch_TypeSub, self).__init__(IX, Del, X, Y, A, B, C, D,  **kwargs_)
supermod.Scratch_Type.subclass = Scratch_TypeSub
# end class Scratch_TypeSub


class Connection_TypeSub(supermod.Connection_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, IX=None, X=None, Y=None, DirX=None, DirY=None, Type=None, AutoGen=None, Prompt=None, **kwargs_):
        super(Connection_TypeSub, self).__init__(Name, NameU, Del, ID, IX, X, Y, DirX, DirY, Type, AutoGen, Prompt,  **kwargs_)
supermod.Connection_Type.subclass = Connection_TypeSub
# end class Connection_TypeSub


class DirX_TypeSub(supermod.DirX_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DirX_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DirX_Type.subclass = DirX_TypeSub
# end class DirX_TypeSub


class DirY_TypeSub(supermod.DirY_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(DirY_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.DirY_Type.subclass = DirY_TypeSub
# end class DirY_TypeSub


class Type_TypeSub(supermod.Type_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Type_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Type_Type.subclass = Type_TypeSub
# end class Type_TypeSub


class AutoGen_TypeSub(supermod.AutoGen_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(AutoGen_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.AutoGen_Type.subclass = AutoGen_TypeSub
# end class AutoGen_TypeSub


class Prompt_TypeSub(supermod.Prompt_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Prompt_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Prompt_Type.subclass = Prompt_TypeSub
# end class Prompt_TypeSub


class ConnectionABCD_TypeSub(supermod.ConnectionABCD_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, IX=None, X=None, Y=None, A=None, B=None, C=None, D=None, **kwargs_):
        super(ConnectionABCD_TypeSub, self).__init__(Name, NameU, Del, ID, IX, X, Y, A, B, C, D,  **kwargs_)
supermod.ConnectionABCD_Type.subclass = ConnectionABCD_TypeSub
# end class ConnectionABCD_TypeSub


class Field_TypeSub(supermod.Field_Type):
    def __init__(self, IX=None, Del=None, Value=None, EditMode=None, Format=None, Type=None, UICat=None, UICod=None, UIFmt=None, Calendar=None, ObjectKind=None, **kwargs_):
        super(Field_TypeSub, self).__init__(IX, Del, Value, EditMode, Format, Type, UICat, UICod, UIFmt, Calendar, ObjectKind,  **kwargs_)
supermod.Field_Type.subclass = Field_TypeSub
# end class Field_TypeSub


class Value_TypeSub(supermod.Value_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, SolutionXML=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(Value_TypeSub, self).__init__(Unit, F, Err, V, SolutionXML, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Value_Type.subclass = Value_TypeSub
# end class Value_TypeSub


class EditMode_TypeSub(supermod.EditMode_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(EditMode_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.EditMode_Type.subclass = EditMode_TypeSub
# end class EditMode_TypeSub


class Format_TypeSub(supermod.Format_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Format_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Format_Type.subclass = Format_TypeSub
# end class Format_TypeSub


class UICat_TypeSub(supermod.UICat_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UICat_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UICat_Type.subclass = UICat_TypeSub
# end class UICat_TypeSub


class UICod_TypeSub(supermod.UICod_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UICod_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UICod_Type.subclass = UICod_TypeSub
# end class UICod_TypeSub


class UIFmt_TypeSub(supermod.UIFmt_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(UIFmt_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.UIFmt_Type.subclass = UIFmt_TypeSub
# end class UIFmt_TypeSub


class ObjectKind_TypeSub(supermod.ObjectKind_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ObjectKind_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ObjectKind_Type.subclass = ObjectKind_TypeSub
# end class ObjectKind_TypeSub


class Control_TypeSub(supermod.Control_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, IX=None, X=None, Y=None, XDyn=None, YDyn=None, XCon=None, YCon=None, CanGlue=None, Prompt=None, **kwargs_):
        super(Control_TypeSub, self).__init__(Name, NameU, Del, ID, IX, X, Y, XDyn, YDyn, XCon, YCon, CanGlue, Prompt,  **kwargs_)
supermod.Control_Type.subclass = Control_TypeSub
# end class Control_TypeSub


class XDyn_TypeSub(supermod.XDyn_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XDyn_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XDyn_Type.subclass = XDyn_TypeSub
# end class XDyn_TypeSub


class YDyn_TypeSub(supermod.YDyn_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YDyn_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YDyn_Type.subclass = YDyn_TypeSub
# end class YDyn_TypeSub


class XCon_TypeSub(supermod.XCon_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XCon_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XCon_Type.subclass = XCon_TypeSub
# end class XCon_TypeSub


class YCon_TypeSub(supermod.YCon_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YCon_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YCon_Type.subclass = YCon_TypeSub
# end class YCon_TypeSub


class CanGlue_TypeSub(supermod.CanGlue_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(CanGlue_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.CanGlue_Type.subclass = CanGlue_TypeSub
# end class CanGlue_TypeSub


class Geom_TypeSub(supermod.Geom_Type):
    def __init__(self, IX=None, Del=None, NoFill=None, NoLine=None, NoShow=None, NoSnap=None, MoveTo=None, LineTo=None, ArcTo=None, InfiniteLine=None, Ellipse=None, EllipticalArcTo=None, SplineStart=None, SplineKnot=None, PolylineTo=None, NURBSTo=None, NoQuickDrag=None, **kwargs_):
        super(Geom_TypeSub, self).__init__(IX, Del, NoFill, NoLine, NoShow, NoSnap, MoveTo, LineTo, ArcTo, InfiniteLine, Ellipse, EllipticalArcTo, SplineStart, SplineKnot, PolylineTo, NURBSTo, NoQuickDrag,  **kwargs_)
supermod.Geom_Type.subclass = Geom_TypeSub
# end class Geom_TypeSub


class NoFill_TypeSub(supermod.NoFill_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoFill_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoFill_Type.subclass = NoFill_TypeSub
# end class NoFill_TypeSub


class NoLine_TypeSub(supermod.NoLine_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoLine_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoLine_Type.subclass = NoLine_TypeSub
# end class NoLine_TypeSub


class NoShow_TypeSub(supermod.NoShow_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoShow_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoShow_Type.subclass = NoShow_TypeSub
# end class NoShow_TypeSub


class NoSnap_TypeSub(supermod.NoSnap_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoSnap_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoSnap_Type.subclass = NoSnap_TypeSub
# end class NoSnap_TypeSub


class MoveTo_TypeSub(supermod.MoveTo_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, **kwargs_):
        super(MoveTo_TypeSub, self).__init__(IX, Del, X, Y,  **kwargs_)
supermod.MoveTo_Type.subclass = MoveTo_TypeSub
# end class MoveTo_TypeSub


class LineTo_TypeSub(supermod.LineTo_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, **kwargs_):
        super(LineTo_TypeSub, self).__init__(IX, Del, X, Y,  **kwargs_)
supermod.LineTo_Type.subclass = LineTo_TypeSub
# end class LineTo_TypeSub


class ArcTo_TypeSub(supermod.ArcTo_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, **kwargs_):
        super(ArcTo_TypeSub, self).__init__(IX, Del, X, Y, A,  **kwargs_)
supermod.ArcTo_Type.subclass = ArcTo_TypeSub
# end class ArcTo_TypeSub


class InfiniteLine_TypeSub(supermod.InfiniteLine_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, B=None, **kwargs_):
        super(InfiniteLine_TypeSub, self).__init__(IX, Del, X, Y, A, B,  **kwargs_)
supermod.InfiniteLine_Type.subclass = InfiniteLine_TypeSub
# end class InfiniteLine_TypeSub


class Ellipse_TypeSub(supermod.Ellipse_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, B=None, C=None, D=None, **kwargs_):
        super(Ellipse_TypeSub, self).__init__(IX, Del, X, Y, A, B, C, D,  **kwargs_)
supermod.Ellipse_Type.subclass = Ellipse_TypeSub
# end class Ellipse_TypeSub


class EllipticalArcTo_TypeSub(supermod.EllipticalArcTo_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, B=None, C=None, D=None, **kwargs_):
        super(EllipticalArcTo_TypeSub, self).__init__(IX, Del, X, Y, A, B, C, D,  **kwargs_)
supermod.EllipticalArcTo_Type.subclass = EllipticalArcTo_TypeSub
# end class EllipticalArcTo_TypeSub


class SplineStart_TypeSub(supermod.SplineStart_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, B=None, C=None, D=None, **kwargs_):
        super(SplineStart_TypeSub, self).__init__(IX, Del, X, Y, A, B, C, D,  **kwargs_)
supermod.SplineStart_Type.subclass = SplineStart_TypeSub
# end class SplineStart_TypeSub


class SplineKnot_TypeSub(supermod.SplineKnot_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, **kwargs_):
        super(SplineKnot_TypeSub, self).__init__(IX, Del, X, Y, A,  **kwargs_)
supermod.SplineKnot_Type.subclass = SplineKnot_TypeSub
# end class SplineKnot_TypeSub


class PolylineTo_TypeSub(supermod.PolylineTo_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, **kwargs_):
        super(PolylineTo_TypeSub, self).__init__(IX, Del, X, Y, A,  **kwargs_)
supermod.PolylineTo_Type.subclass = PolylineTo_TypeSub
# end class PolylineTo_TypeSub


class NURBSTo_TypeSub(supermod.NURBSTo_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, A=None, B=None, C=None, D=None, E=None, **kwargs_):
        super(NURBSTo_TypeSub, self).__init__(IX, Del, X, Y, A, B, C, D, E,  **kwargs_)
supermod.NURBSTo_Type.subclass = NURBSTo_TypeSub
# end class NURBSTo_TypeSub


class NoQuickDrag_TypeSub(supermod.NoQuickDrag_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NoQuickDrag_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NoQuickDrag_Type.subclass = NoQuickDrag_TypeSub
# end class NoQuickDrag_TypeSub


class Act_TypeSub(supermod.Act_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, IX=None, Menu=None, Action=None, Checked=None, Disabled=None, ReadOnly=None, Invisible=None, BeginGroup=None, FlyoutChild=None, TagName=None, ButtonFace=None, SortKey=None, **kwargs_):
        super(Act_TypeSub, self).__init__(Name, NameU, Del, ID, IX, Menu, Action, Checked, Disabled, ReadOnly, Invisible, BeginGroup, FlyoutChild, TagName, ButtonFace, SortKey,  **kwargs_)
supermod.Act_Type.subclass = Act_TypeSub
# end class Act_TypeSub


class Menu_TypeSub(supermod.Menu_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Menu_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Menu_Type.subclass = Menu_TypeSub
# end class Menu_TypeSub


class Action_TypeSub(supermod.Action_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Action_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Action_Type.subclass = Action_TypeSub
# end class Action_TypeSub


class Checked_TypeSub(supermod.Checked_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Checked_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Checked_Type.subclass = Checked_TypeSub
# end class Checked_TypeSub


class Disabled_TypeSub(supermod.Disabled_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Disabled_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Disabled_Type.subclass = Disabled_TypeSub
# end class Disabled_TypeSub


class ReadOnly_TypeSub(supermod.ReadOnly_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ReadOnly_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ReadOnly_Type.subclass = ReadOnly_TypeSub
# end class ReadOnly_TypeSub


class BeginGroup_TypeSub(supermod.BeginGroup_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(BeginGroup_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.BeginGroup_Type.subclass = BeginGroup_TypeSub
# end class BeginGroup_TypeSub


class FlyoutChild_TypeSub(supermod.FlyoutChild_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(FlyoutChild_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.FlyoutChild_Type.subclass = FlyoutChild_TypeSub
# end class FlyoutChild_TypeSub


class TagName_TypeSub(supermod.TagName_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(TagName_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.TagName_Type.subclass = TagName_TypeSub
# end class TagName_TypeSub


class ButtonFace_TypeSub(supermod.ButtonFace_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ButtonFace_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ButtonFace_Type.subclass = ButtonFace_TypeSub
# end class ButtonFace_TypeSub


class Layer_TypeSub(supermod.Layer_Type):
    def __init__(self, IX=None, Del=None, Name=None, Color=None, Status=None, Visible=None, Print=None, Active=None, Lock=None, Snap=None, Glue=None, NameUniv=None, ColorTrans=None, **kwargs_):
        super(Layer_TypeSub, self).__init__(IX, Del, Name, Color, Status, Visible, Print, Active, Lock, Snap, Glue, NameUniv, ColorTrans,  **kwargs_)
supermod.Layer_Type.subclass = Layer_TypeSub
# end class Layer_TypeSub


class Name_TypeSub(supermod.Name_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Name_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Name_Type.subclass = Name_TypeSub
# end class Name_TypeSub


class Status_TypeSub(supermod.Status_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Status_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Status_Type.subclass = Status_TypeSub
# end class Status_TypeSub


class Visible_TypeSub(supermod.Visible_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Visible_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Visible_Type.subclass = Visible_TypeSub
# end class Visible_TypeSub


class Print_TypeSub(supermod.Print_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Print_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Print_Type.subclass = Print_TypeSub
# end class Print_TypeSub


class Active_TypeSub(supermod.Active_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Active_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Active_Type.subclass = Active_TypeSub
# end class Active_TypeSub


class Lock_TypeSub(supermod.Lock_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Lock_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Lock_Type.subclass = Lock_TypeSub
# end class Lock_TypeSub


class Snap_TypeSub(supermod.Snap_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Snap_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Snap_Type.subclass = Snap_TypeSub
# end class Snap_TypeSub


class Glue_TypeSub(supermod.Glue_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Glue_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Glue_Type.subclass = Glue_TypeSub
# end class Glue_TypeSub


class NameUniv_TypeSub(supermod.NameUniv_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(NameUniv_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.NameUniv_Type.subclass = NameUniv_TypeSub
# end class NameUniv_TypeSub


class User_TypeSub(supermod.User_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, Value=None, Prompt=None, **kwargs_):
        super(User_TypeSub, self).__init__(Name, NameU, Del, ID, Value, Prompt,  **kwargs_)
supermod.User_Type.subclass = User_TypeSub
# end class User_TypeSub


class Prop_TypeSub(supermod.Prop_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, Value=None, Prompt=None, Label=None, Format=None, SortKey=None, Type=None, Invisible=None, Verify=None, LangID=None, Calendar=None, **kwargs_):
        super(Prop_TypeSub, self).__init__(Name, NameU, Del, ID, Value, Prompt, Label, Format, SortKey, Type, Invisible, Verify, LangID, Calendar,  **kwargs_)
supermod.Prop_Type.subclass = Prop_TypeSub
# end class Prop_TypeSub


class Label_TypeSub(supermod.Label_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Label_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Label_Type.subclass = Label_TypeSub
# end class Label_TypeSub


class Verify_TypeSub(supermod.Verify_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Verify_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Verify_Type.subclass = Verify_TypeSub
# end class Verify_TypeSub


class Hyperlink_TypeSub(supermod.Hyperlink_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, Description=None, Address=None, SubAddress=None, ExtraInfo=None, Frame=None, NewWindow=None, Default=None, Invisible=None, SortKey=None, **kwargs_):
        super(Hyperlink_TypeSub, self).__init__(Name, NameU, Del, ID, Description, Address, SubAddress, ExtraInfo, Frame, NewWindow, Default, Invisible, SortKey,  **kwargs_)
supermod.Hyperlink_Type.subclass = Hyperlink_TypeSub
# end class Hyperlink_TypeSub


class Reviewer_TypeSub(supermod.Reviewer_Type):
    def __init__(self, IX=None, Del=None, Name=None, Initials=None, Color=None, ReviewerID=None, CurrentIndex=None, **kwargs_):
        super(Reviewer_TypeSub, self).__init__(IX, Del, Name, Initials, Color, ReviewerID, CurrentIndex,  **kwargs_)
supermod.Reviewer_Type.subclass = Reviewer_TypeSub
# end class Reviewer_TypeSub


class Initials_TypeSub(supermod.Initials_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Initials_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Initials_Type.subclass = Initials_TypeSub
# end class Initials_TypeSub


class ReviewerID_TypeSub(supermod.ReviewerID_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(ReviewerID_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.ReviewerID_Type.subclass = ReviewerID_TypeSub
# end class ReviewerID_TypeSub


class CurrentIndex_TypeSub(supermod.CurrentIndex_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(CurrentIndex_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.CurrentIndex_Type.subclass = CurrentIndex_TypeSub
# end class CurrentIndex_TypeSub


class Annotation_TypeSub(supermod.Annotation_Type):
    def __init__(self, IX=None, Del=None, X=None, Y=None, ReviewerID=None, MarkerIndex=None, Date=None, Comment=None, LangID=None, **kwargs_):
        super(Annotation_TypeSub, self).__init__(IX, Del, X, Y, ReviewerID, MarkerIndex, Date, Comment, LangID,  **kwargs_)
supermod.Annotation_Type.subclass = Annotation_TypeSub
# end class Annotation_TypeSub


class MarkerIndex_TypeSub(supermod.MarkerIndex_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(MarkerIndex_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.MarkerIndex_Type.subclass = MarkerIndex_TypeSub
# end class MarkerIndex_TypeSub


class Date_TypeSub(supermod.Date_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(Date_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.Date_Type.subclass = Date_TypeSub
# end class Date_TypeSub


class SmartTagDef_TypeSub(supermod.SmartTagDef_Type):
    def __init__(self, Name=None, NameU=None, Del=None, ID=None, X=None, Y=None, TagName=None, XJustify=None, YJustify=None, DisplayMode=None, ButtonFace=None, Disabled=None, Description=None, **kwargs_):
        super(SmartTagDef_TypeSub, self).__init__(Name, NameU, Del, ID, X, Y, TagName, XJustify, YJustify, DisplayMode, ButtonFace, Disabled, Description,  **kwargs_)
supermod.SmartTagDef_Type.subclass = SmartTagDef_TypeSub
# end class SmartTagDef_TypeSub


class XJustify_TypeSub(supermod.XJustify_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(XJustify_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.XJustify_Type.subclass = XJustify_TypeSub
# end class XJustify_TypeSub


class YJustify_TypeSub(supermod.YJustify_Type):
    def __init__(self, Unit=None, F=None, Err=None, V=None, valueOf_=None, **kwargs_):
        super(YJustify_TypeSub, self).__init__(Unit, F, Err, V, valueOf_,  **kwargs_)
supermod.YJustify_Type.subclass = YJustify_TypeSub
# end class YJustify_TypeSub


class DataConnections_TypeSub(supermod.DataConnections_Type):
    def __init__(self, NextID=None, DataConnection=None, **kwargs_):
        super(DataConnections_TypeSub, self).__init__(NextID, DataConnection,  **kwargs_)
supermod.DataConnections_Type.subclass = DataConnections_TypeSub
# end class DataConnections_TypeSub


class DataConnection_TypeSub(supermod.DataConnection_Type):
    def __init__(self, ID=None, FileName=None, ConnectionString=None, Command=None, FriendlyName=None, Timeout=None, AlwaysUseConnectionFile=None, **kwargs_):
        super(DataConnection_TypeSub, self).__init__(ID, FileName, ConnectionString, Command, FriendlyName, Timeout, AlwaysUseConnectionFile,  **kwargs_)
supermod.DataConnection_Type.subclass = DataConnection_TypeSub
# end class DataConnection_TypeSub


class DataRecordSets_TypeSub(supermod.DataRecordSets_Type):
    def __init__(self, NextID=None, ActiveRecordsetID=None, DataWindowOrder=None, DataRecordSet=None, **kwargs_):
        super(DataRecordSets_TypeSub, self).__init__(NextID, ActiveRecordsetID, DataWindowOrder, DataRecordSet,  **kwargs_)
supermod.DataRecordSets_Type.subclass = DataRecordSets_TypeSub
# end class DataRecordSets_TypeSub


class DataRecordSet_TypeSub(supermod.DataRecordSet_Type):
    def __init__(self, ID=None, ConnectionID=None, Command=None, Options=None, TimeRefreshed=None, NextRowID=None, Name=None, RowOrder=None, RefreshOverwriteAll=None, RefreshNoReconciliationUI=None, RefreshInterval=None, ReplaceLinks=None, Checksum=None, ADOData=None, DataColumns=None, PrimaryKey=None, RowMap=None, RefreshConflict=None, AutoLinkComparison=None, **kwargs_):
        super(DataRecordSet_TypeSub, self).__init__(ID, ConnectionID, Command, Options, TimeRefreshed, NextRowID, Name, RowOrder, RefreshOverwriteAll, RefreshNoReconciliationUI, RefreshInterval, ReplaceLinks, Checksum, ADOData, DataColumns, PrimaryKey, RowMap, RefreshConflict, AutoLinkComparison,  **kwargs_)
supermod.DataRecordSet_Type.subclass = DataRecordSet_TypeSub
# end class DataRecordSet_TypeSub


class ADOData_TypeSub(supermod.ADOData_Type):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(ADOData_TypeSub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.ADOData_Type.subclass = ADOData_TypeSub
# end class ADOData_TypeSub


class DataColumns_TypeSub(supermod.DataColumns_Type):
    def __init__(self, SortColumn=None, SortAsc=None, DataColumn=None, **kwargs_):
        super(DataColumns_TypeSub, self).__init__(SortColumn, SortAsc, DataColumn,  **kwargs_)
supermod.DataColumns_Type.subclass = DataColumns_TypeSub
# end class DataColumns_TypeSub


class PrimaryKey_TypeSub(supermod.PrimaryKey_Type):
    def __init__(self, valueOf_=None, **kwargs_):
        super(PrimaryKey_TypeSub, self).__init__(valueOf_,  **kwargs_)
supermod.PrimaryKey_Type.subclass = PrimaryKey_TypeSub
# end class PrimaryKey_TypeSub


class RowMap_TypeSub(supermod.RowMap_Type):
    def __init__(self, RowID=None, PageID=None, ShapeID=None, **kwargs_):
        super(RowMap_TypeSub, self).__init__(RowID, PageID, ShapeID,  **kwargs_)
supermod.RowMap_Type.subclass = RowMap_TypeSub
# end class RowMap_TypeSub


class RefreshConflict_TypeSub(supermod.RefreshConflict_Type):
    def __init__(self, RowID=None, ShapeID=None, PageID=None, **kwargs_):
        super(RefreshConflict_TypeSub, self).__init__(RowID, ShapeID, PageID,  **kwargs_)
supermod.RefreshConflict_Type.subclass = RefreshConflict_TypeSub
# end class RefreshConflict_TypeSub


class AutoLinkComparison_TypeSub(supermod.AutoLinkComparison_Type):
    def __init__(self, ColumnName=None, ContextType=None, ContextTypeLabel=None, **kwargs_):
        super(AutoLinkComparison_TypeSub, self).__init__(ColumnName, ContextType, ContextTypeLabel,  **kwargs_)
supermod.AutoLinkComparison_Type.subclass = AutoLinkComparison_TypeSub
# end class AutoLinkComparison_TypeSub


class DataColumn_TypeSub(supermod.DataColumn_Type):
    def __init__(self, ColumnNameID=None, Name=None, Label=None, OrigLabel=None, LangID=None, Calendar=None, DataType=None, UnitType=None, Currency=None, Degree=None, DisplayWidth=None, DisplayOrder=None, Mapped=None, Hyperlink=None, **kwargs_):
        super(DataColumn_TypeSub, self).__init__(ColumnNameID, Name, Label, OrigLabel, LangID, Calendar, DataType, UnitType, Currency, Degree, DisplayWidth, DisplayOrder, Mapped, Hyperlink,  **kwargs_)
supermod.DataColumn_Type.subclass = DataColumn_TypeSub
# end class DataColumn_TypeSub


class RibbonX_TypeSub(supermod.RibbonX_Type):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(RibbonX_TypeSub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.RibbonX_Type.subclass = RibbonX_TypeSub
# end class RibbonX_TypeSub


class UserCustomUI_TypeSub(supermod.UserCustomUI_Type):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(UserCustomUI_TypeSub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.UserCustomUI_Type.subclass = UserCustomUI_TypeSub
# end class UserCustomUI_TypeSub


class Validation_TypeSub(supermod.Validation_Type):
    def __init__(self, ValidationProperties=None, RuleSets=None, Issues=None, **kwargs_):
        super(Validation_TypeSub, self).__init__(ValidationProperties, RuleSets, Issues,  **kwargs_)
supermod.Validation_Type.subclass = Validation_TypeSub
# end class Validation_TypeSub


class ValidationProperties_TypeSub(supermod.ValidationProperties_Type):
    def __init__(self, LastValidated=None, ShowIgnored=None, **kwargs_):
        super(ValidationProperties_TypeSub, self).__init__(LastValidated, ShowIgnored,  **kwargs_)
supermod.ValidationProperties_Type.subclass = ValidationProperties_TypeSub
# end class ValidationProperties_TypeSub


class RuleSets_TypeSub(supermod.RuleSets_Type):
    def __init__(self, RuleSet=None, **kwargs_):
        super(RuleSets_TypeSub, self).__init__(RuleSet,  **kwargs_)
supermod.RuleSets_Type.subclass = RuleSets_TypeSub
# end class RuleSets_TypeSub


class RuleSet_TypeSub(supermod.RuleSet_Type):
    def __init__(self, ID=None, Name=None, NameU=None, Description=None, Enabled=None, RuleSetFlags=None, Rule=None, **kwargs_):
        super(RuleSet_TypeSub, self).__init__(ID, Name, NameU, Description, Enabled, RuleSetFlags, Rule,  **kwargs_)
supermod.RuleSet_Type.subclass = RuleSet_TypeSub
# end class RuleSet_TypeSub


class RuleSetFlags_TypeSub(supermod.RuleSetFlags_Type):
    def __init__(self, Hidden=None, **kwargs_):
        super(RuleSetFlags_TypeSub, self).__init__(Hidden,  **kwargs_)
supermod.RuleSetFlags_Type.subclass = RuleSetFlags_TypeSub
# end class RuleSetFlags_TypeSub


class Rule_TypeSub(supermod.Rule_Type):
    def __init__(self, ID=None, NameU=None, Category=None, Description=None, RuleTarget=None, Ignored=None, RuleFilter=None, RuleTest=None, **kwargs_):
        super(Rule_TypeSub, self).__init__(ID, NameU, Category, Description, RuleTarget, Ignored, RuleFilter, RuleTest,  **kwargs_)
supermod.Rule_Type.subclass = Rule_TypeSub
# end class Rule_TypeSub


class RuleFilter_TypeSub(supermod.RuleFilter_Type):
    def __init__(self, valueOf_=None, **kwargs_):
        super(RuleFilter_TypeSub, self).__init__(valueOf_,  **kwargs_)
supermod.RuleFilter_Type.subclass = RuleFilter_TypeSub
# end class RuleFilter_TypeSub


class RuleTest_TypeSub(supermod.RuleTest_Type):
    def __init__(self, valueOf_=None, **kwargs_):
        super(RuleTest_TypeSub, self).__init__(valueOf_,  **kwargs_)
supermod.RuleTest_Type.subclass = RuleTest_TypeSub
# end class RuleTest_TypeSub


class Issues_TypeSub(supermod.Issues_Type):
    def __init__(self, Issue=None, **kwargs_):
        super(Issues_TypeSub, self).__init__(Issue,  **kwargs_)
supermod.Issues_Type.subclass = Issues_TypeSub
# end class Issues_TypeSub


class Issue_TypeSub(supermod.Issue_Type):
    def __init__(self, ID=None, Ignored=None, IssueTarget=None, RuleInfo=None, **kwargs_):
        super(Issue_TypeSub, self).__init__(ID, Ignored, IssueTarget, RuleInfo,  **kwargs_)
supermod.Issue_Type.subclass = Issue_TypeSub
# end class Issue_TypeSub


class IssueTarget_TypeSub(supermod.IssueTarget_Type):
    def __init__(self, PageID=None, ShapeID=None, **kwargs_):
        super(IssueTarget_TypeSub, self).__init__(PageID, ShapeID,  **kwargs_)
supermod.IssueTarget_Type.subclass = IssueTarget_TypeSub
# end class IssueTarget_TypeSub


class RuleInfo_TypeSub(supermod.RuleInfo_Type):
    def __init__(self, RuleSetID=None, RuleID=None, **kwargs_):
        super(RuleInfo_TypeSub, self).__init__(RuleSetID, RuleID,  **kwargs_)
supermod.RuleInfo_Type.subclass = RuleInfo_TypeSub
# end class RuleInfo_TypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RibbonX_Type'
        rootClass = supermod.RibbonX_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RibbonX_Type'
        rootClass = supermod.RibbonX_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RibbonX_Type'
        rootClass = supermod.RibbonX_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RibbonX_Type'
        rootClass = supermod.RibbonX_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
