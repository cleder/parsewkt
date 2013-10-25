# -*- coding: utf-8 -*-

from .parse import WktSemantics, WktParser

class Semantics(WktSemantics):

    def _coordinates(self, ast):
        if 'EMPTY' in ast[1:]:
            return None
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            return ast[2]
        else:
            return ast[1]


    def well_known_text_representation(self, ast):
        ast = super(Semantics, self).well_known_text_representation(ast)
        return ast

    def point_text_representation(self, ast):
        ast = super(Semantics, self).point_text_representation(ast)
        return ast

    def curve_text_representation(self, ast):
        ast = super(Semantics, self).curve_text_representation(ast)
        return ast

    def linestring_text_representation(self, ast):
        ast = super(Semantics, self).linestring_text_representation(ast)
        return ast

    def circularstring_text_representation(self, ast):
        ast = super(Semantics, self).circularstring_text_representation(ast)
        return ast

    def compoundcurve_text_representation(self, ast):
        ast = super(Semantics, self).compoundcurve_text_representation(ast)
        return ast

    def surface_text_representation(self, ast):
        ast = super(Semantics, self).surface_text_representation(ast)
        return ast

    def curvepolygon_text_representation(self, ast):
        ast = super(Semantics, self).curvepolygon_text_representation(ast)
        return ast

    def polygon_text_representation(self, ast):
        ast = super(Semantics, self).polygon_text_representation(ast)
        return ast

    def triangle_text_representation(self, ast):
        ast = super(Semantics, self).triangle_text_representation(ast)
        return ast

    def collection_text_representation(self, ast):
        ast = super(Semantics, self).collection_text_representation(ast)
        return ast

    def multipoint_text_representation(self, ast):
        ast = super(Semantics, self).multipoint_text_representation(ast)
        return ast

    def multicurve_text_representation(self, ast):
        ast = super(Semantics, self).multicurve_text_representation(ast)
        return ast

    def multilinestring_text_representation(self, ast):
        ast = super(Semantics, self).multilinestring_text_representation(ast)
        return ast

    def multisurface_text_representation(self, ast):
        ast = super(Semantics, self).multisurface_text_representation(ast)
        return ast

    def multipolygon_text_representation(self, ast):
        ast = super(Semantics, self).multipolygon_text_representation(ast)
        return ast

    def polyhedralsurface_text_representation(self, ast):
        ast = super(Semantics, self).polyhedralsurface_text_representation(ast)
        return ast

    def tin_text_representation(self, ast):
        ast = super(Semantics, self).tin_text_representation(ast)
        return ast

    def geometrycollection_text_representation(self, ast):
        ast = super(Semantics, self).geometrycollection_text_representation(ast)
        d = {'type': 'GeometryCollection', 'geometries': self._coordinates[ast] }
        print d
        return d

    def linestring_text_body(self, ast):
        ast = super(Semantics, self).linestring_text_body(ast)
        return ast

    def curvepolygon_text_body(self, ast):
        ast = super(Semantics, self).curvepolygon_text_body(ast)
        return ast

    def polygon_text_body(self, ast):
        ast = super(Semantics, self).polygon_text_body(ast)
        return ast

    def triangle_text_body(self, ast):
        ast = super(Semantics, self).triangle_text_body(ast)
        return ast

    def point_text(self, ast):
        ast = super(Semantics, self).point_text(ast)
        if ast != 'EMPTY':
            assert(len(ast) == 3)
            ast = tuple(ast[1])
        return ast

    def point(self, ast):
        ast = super(Semantics, self).point(ast)
        return ast

    def x(self, ast):
        ast = super(Semantics, self).x(ast)
        return ast

    def y(self, ast):
        ast = super(Semantics, self).y(ast)
        return ast

    def z(self, ast):
        ast = super(Semantics, self).z(ast)
        return ast

    def m(self, ast):
        ast = super(Semantics, self).m(ast)
        return ast

    def linestring_text(self, ast):
        ast = super(Semantics, self).linestring_text(ast)
        if ast != 'EMPTY':
            assert(ast[0] == '(')
            assert(ast[-1]==')')
            ast = ast[1:-1]
            ast = [tuple(ast[0])] + [tuple(v) for v in ast[1] if v != ',']
            ast = tuple(ast)
        return ast

    def circularstring_text(self, ast):
        ast = super(Semantics, self).circularstring_text(ast)
        return ast

    def compoundcurve_text(self, ast):
        ast = super(Semantics, self).compoundcurve_text(ast)
        return ast

    def single_curve_text(self, ast):
        ast = super(Semantics, self).single_curve_text(ast)
        return ast

    def curve_text(self, ast):
        ast = super(Semantics, self).curve_text(ast)
        return ast

    def ring_text(self, ast):
        ast = super(Semantics, self).ring_text(ast)
        return ast

    def surface_text(self, ast):
        ast = super(Semantics, self).surface_text(ast)
        return ast

    def curvepolygon_text(self, ast):
        ast = super(Semantics, self).curvepolygon_text(ast)
        return ast

    def polygon_text(self, ast):
        ast = super(Semantics, self).polygon_text(ast)
        if ast != 'EMPTY':
            assert(ast[0] == '(')
            assert(ast[-1]==')')
            ast = ast[1:-1]
            if ast[0] == 'EMPTY':
                ast = 'EMPTY'
            else:
                ast = tuple([tuple(ast[0])]  +
                    [tuple(v) for v in ast[1]
                        if v != ',' and v])
        return ast

    def triangle_text(self, ast):
        ast = super(Semantics, self).triangle_text(ast)
        return ast

    def multipoint_text(self, ast):
        ast = super(Semantics, self).multipoint_text(ast)
        if ast != 'EMPTY':
            assert(ast[0] == '(')
            assert(ast[-1]==')')
            ast = ast[1:-1]
            if ast[0] == 'EMPTY':
                ast = 'EMPTY'
            else:
                ast = tuple([tuple(ast[0])]  +
                    [tuple(v) for v in ast[1]
                        if v != ',' and v])
        return ast

    def multicurve_text(self, ast):
        ast = super(Semantics, self).multicurve_text(ast)
        return ast

    def multilinestring_text(self, ast):
        ast = super(Semantics, self).multilinestring_text(ast)
        if ast != 'EMPTY':
            assert(ast[0] == '(')
            assert(ast[-1]==')')
            ast = ast[1:-1]
            if ast[0] == 'EMPTY':
                ast = 'EMPTY'
            else:
                ast = tuple([tuple(ast[0])]  +
                    [tuple(v) for v in ast[1]
                        if v != ',' and v])
        return ast

    def multisurface_text(self, ast):
        ast = super(Semantics, self).multisurface_text(ast)
        return ast

    def multipolygon_text(self, ast):
        ast = super(Semantics, self).multipolygon_text(ast)
        if ast != 'EMPTY':
            assert(ast[0] == '(')
            assert(ast[-1]==')')
            ast = ast[1:-1]
            if ast[0] == 'EMPTY':
                ast = 'EMPTY'
            else:
                ast = tuple([tuple(ast[0])]  +
                    [tuple(v) for v in ast[1]
                        if v != ',' and v])
                print ast
        return ast

    def polyhedralsurface_text(self, ast):
        ast = super(Semantics, self).polyhedralsurface_text(ast)
        return ast

    def tin_text(self, ast):
        ast = super(Semantics, self).tin_text(ast)
        return ast

    def geometrycollection_text(self, ast):
        ast = super(Semantics, self).geometrycollection_text(ast)
        if ast != 'EMPTY':
            assert(ast[0] == '(')
            assert(ast[-1]==')')
            ast = ast[1:-1]
        return ast

    def empty_set(self, ast):
        ast = super(Semantics, self).empty_set(ast)
        return ast

    def z_m(self, ast):
        ast = super(Semantics, self).z_m(ast)
        return ast

    def left_paren(self, ast):
        ast = super(Semantics, self).left_paren(ast)
        return ast

    def right_paren(self, ast):
        ast = super(Semantics, self).right_paren(ast)
        return ast

    def number(self, ast):
        ast = super(Semantics, self).number(ast)
        ast = float(ast)
        return ast

    def comma(self, ast):
        ast = super(Semantics, self).comma(ast)
        return ast

def from_wkt(text):
    parser = WktParser(parseinfo=False)
    ast = parser.parse(text, rule_name='well_known_text_representation', semantics=Semantics())
    if ast[0] == 'POINT':
        d = {'type': 'Point', 'coordinates': None}
        if 'EMPTY' in ast[1:]:
            return d
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            assert(len(ast[2]) == 3)
            d['coordinates'] = ast[2]
        else:
            assert(len(ast)==2)
            assert(2<=len(ast[1])<=3)
            d['coordinates'] = ast[1]
        return d
    elif ast[0] == 'LINESTRING':
        d = {'type': 'LineString', 'coordinates': None}
        if 'EMPTY' in ast[1:]:
            return d
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            #assert(len(ast[2]) == 3)
            #d['coordinates'] = ast[2]
            pass
            #XXX need a test for this
            raise NotImplementedError
        else:
            assert(len(ast)==2)
            assert(len(ast[1])>1)
            assert(2<=len(ast[1][1])<=3)
            d['coordinates'] = ast[1]
        return d
    elif ast[0] == 'POLYGON':
        d = {'type': 'Polygon', 'coordinates': None}
        if 'EMPTY' in ast[1:]:
            return d
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            #assert(len(ast[2]) == 3)
            #d['coordinates'] = ast[2]
            pass
            #XXX need a test for this
            raise NotImplementedError
        else:
            assert(len(ast)==2)
            d['coordinates'] = ast[1]
        return d
    elif ast[0] == 'MULTIPOINT':
        d = {'type': 'MultiPoint', 'coordinates': None}
        if 'EMPTY' in ast[1:]:
            return d
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            #assert(len(ast[2]) == 3)
            #d['coordinates'] = ast[2]
            pass
            #XXX need a test for this
            raise NotImplementedError
        else:
            assert(len(ast)==2)
            d['coordinates'] = ast[1]
        return d
    elif ast[0] == 'MULTILINESTRING':
        d = {'type': 'MultiLineString', 'coordinates': None}
        if 'EMPTY' in ast[1:]:
            return d
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            #assert(len(ast[2]) == 3)
            #d['coordinates'] = ast[2]
            pass
            #XXX need a test for this
            raise NotImplementedError
        else:
            assert(len(ast)==2)
            d['coordinates'] = ast[1]
        return d
    elif ast[0] == 'MULTIPOLYGON':
        d = {'type': 'MultiPolygon', 'coordinates': None}
        if 'EMPTY' in ast[1:]:
            return d
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            #assert(len(ast[2]) == 3)
            #d['coordinates'] = ast[2]
            pass
            #XXX need a test for this
            raise NotImplementedError
        else:
            assert(len(ast)==2)
            d['coordinates'] = ast[1]
        return d
    elif ast[0] == 'GEOMETRYCOLLECTION':
        d = {'type': 'GeometryCollection', 'coordinates': None}
        if 'EMPTY' in ast[1:]:
            return d
        elif 'M' in ast[1:]:
            raise NotImplementedError
        elif 'ZM' in ast[1:]:
            raise NotImplementedError
        elif 'Z' in ast[1:]:
            #assert(len(ast[2]) == 3)
            #d['coordinates'] = ast[2]
            pass
            #XXX need a test for this
            raise NotImplementedError
        else:
            assert(len(ast)==2)
            d['coordinates'] = ast[1]
        return d

    raise NotImplementedError

