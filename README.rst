The WKT Parser was gernerated using grako https://pypi.python.org/pypi/grako

The ebnf file is the translation of http://svn.osgeo.org/postgis/trunk/doc/bnf-wkt.txt

The bnf to ebnf conversion was guided by http://stackoverflow.com/questions/14922242/how-to-convert-bnf-to-ebnf

The generation of parse.py is as easy as: /path/to/grako Wkt.ebnf -o parse.py

parsewkt is continually tested with *Travis CI*

.. image:: https://api.travis-ci.org/cleder/parsewkt.png
    :target: https://travis-ci.org/cleder/parsewkt

.. image:: https://coveralls.io/repos/cleder/parsewkt/badge.png?branch=master
    :target: https://coveralls.io/r/cleder/parsewkt?branch=master

Implementation Status
=====================

Currently implemented is parsing from WKT to a __geo_interface__ compliant
dictionary for the following types:

- POINT
- LINESTRING
- POLYGON
- MULTIPOINT
- MULTILINESTRING
- MULTIPOLYGON
- GEOMETRYCOLLECTION

The parser can parse the following types but they are currently not
translated into python objects:

- COMPOUNDCURVE
- CIRCULARSTRING
- CURVEPOLYGON
- MULTICURVE
- POLYHEDRALSURFACE
- TIN
- TRIANGLE

Rationale
=========

The parser was written to have a clean and complete parser for WKT.
Other WKT to python parsers use regular expression to do the same and are
more or less complete.
I wanted to have a reference implementation that could handle any kind
of valid WKT that you throw at it. You can also use it as a reference
if you want to write your own parser with grako.

Usage
======

    >>> from parsewkt import from_wkt
    >>> gc = """GEOMETRYCOLLECTION(
    ...           POINT(99 98),
    ...           LINESTRING(1 1, 3 3),
    ...           POLYGON((0 0, 0 1, 1 1, 0 0)),
    ...           POLYGON((0 0, 0 9, 9 9, 9 0, 0 0), (5 5, 5 6, 6 6, 5 5)),
    ...           MULTIPOLYGON(((0 0, 0 9, 9 9, 9 0, 0 0), (5 5, 5 6, 6 6, 5 5)))
    ...         )"""
    >>> from_wkt(gc)
    {'type': 'GeometryCollection', 'geometries': (
        {'type': 'Point', 'coordinates': (99.0, 98.0)},
        {'type': 'LineString', 'coordinates': ((1.0, 1.0), (3.0, 3.0))},
        {'type': 'Polygon', 'coordinates': (((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.0, 0.0)),)},
        {'type': 'Polygon', 'coordinates': (((0.0, 0.0), (0.0, 9.0), (9.0, 9.0), (9.0, 0.0), (0.0, 0.0)), ((5.0, 5.0), (5.0, 6.0), (6.0, 6.0), (5.0, 5.0)))},
        {'type': 'MultiPolygon', 'coordinates': ((((0.0, 0.0), (0.0, 9.0), (9.0, 9.0), (9.0, 0.0), (0.0, 0.0)), ((5.0, 5.0), (5.0, 6.0), (6.0, 6.0), (5.0, 5.0))),)})}

    >>> tri = """TRIANGLE((0 0 0,0 1 0,1 1 0,0 0 0))"""
    >>> from_wkt(tri)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "/home/.../parsewkt/parsewkt/wkt.py", line 307, in from_wkt
        raise NotImplementedError
    NotImplementedError

License
=======

**parsewkt** is Copyright (C) 2013 by Christian Ledermann

You may use the tool under the terms of the BSD_-style license described in the enclosed **LICENSE.txt** file.

.. _BSD: http://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_.28.22Simplified_BSD_License.22_or_.22FreeBSD_License.22.29
