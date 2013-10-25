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
            assert(len(ast)==2)
            return ast[1]

    def point_text_representation(self, ast):
        ast = super(Semantics, self).point_text_representation(ast)
        d = {'type': 'Point', 'coordinates': self._coordinates(ast)}
        return d

    def linestring_text_representation(self, ast):
        ast = super(Semantics, self).linestring_text_representation(ast)
        d = {'type': 'LineString', 'coordinates': self._coordinates(ast)}
        return d


    def polygon_text_representation(self, ast):
        ast = super(Semantics, self).polygon_text_representation(ast)
        d = {'type': 'Polygon', 'coordinates': self._coordinates(ast)}
        return d

    def multipoint_text_representation(self, ast):
        ast = super(Semantics, self).multipoint_text_representation(ast)
        d = {'type': 'MultiPoint', 'coordinates': self._coordinates(ast)}
        return d

    def multilinestring_text_representation(self, ast):
        ast = super(Semantics, self).multilinestring_text_representation(ast)
        d = {'type': 'MultiLineString', 'coordinates': self._coordinates(ast)}
        return d

    def multipolygon_text_representation(self, ast):
        ast = super(Semantics, self).multipolygon_text_representation(ast)
        d = {'type': 'MultiPolygon', 'coordinates': self._coordinates(ast)}
        return d

    def geometrycollection_text_representation(self, ast):
        ast = super(Semantics, self).geometrycollection_text_representation(ast)
        self._coordinates(ast)
        if 'EMPTY' in ast[1:]:
            return {'type': 'GeometryCollection', 'geometries': None}
        else:
            ast = tuple([ast[1][0]]  +
                    [v for v in ast[1][1]
                        if v != ',' and v])
            d = {'type': 'GeometryCollection', 'geometries': ast }
        return d

    def point_text(self, ast):
        ast = super(Semantics, self).point_text(ast)
        if ast != 'EMPTY':
            assert(len(ast) == 3)
            ast = tuple(ast[1])
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
        return ast

    def geometrycollection_text(self, ast):
        ast = super(Semantics, self).geometrycollection_text(ast)
        if ast != 'EMPTY':
            assert(ast[0] == '(')
            assert(ast[-1]==')')
            ast = ast[1:-1]
        return ast

    def number(self, ast):
        ast = super(Semantics, self).number(ast)
        ast = float(ast)
        return ast


def from_wkt(text):
    parser = WktParser(parseinfo=False)
    ast = parser.parse(text, rule_name='well_known_text_representation', semantics=Semantics())
    if isinstance(ast, dict):
        return ast
    else:
        raise NotImplementedError


