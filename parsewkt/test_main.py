# -*- coding: utf-8 -*-
import unittest

import pygeoif

from .parse import WktParser
from .wkt import from_wkt, Semantics

cc0 = "COMPOUNDCURVE(CIRCULARSTRING(0 0,1 1,1 0),(1 0,0 1))"
cc1 = """COMPOUNDCURVE(CIRCULARSTRING(
                0 0 0,
                0.26794919243112270647255365849413 1 3,
                0.5857864376269049511983112757903 1.4142135623730950488016887242097 1),
                (0.5857864376269049511983112757903 1.4142135623730950488016887242097 1,
                2 0 0,
                0 0 0))"""

cp0 = "CURVEPOLYGON(CIRCULARSTRING(-2 0,-1 -1,0 0,1 -1,2 0,0 2,-2 0),(-1 0,0 0.5,1 0,0 1,-1 0))"
cp1 = """CURVEPOLYGON(CIRCULARSTRING(
                -2 0 0 0,
                -1 -1 1 2,
                0 0 2 4,
                1 -1 3 6,
                2 0 4 8,
                0 2 2 4,
                -2 0 0 0),
                (-1 0 1 2,
                0 0.5 2 4,
                1 0 3 6,
                0 1 3 4,
                -1 0 1 2))"""

cs0 = "CIRCULARSTRING(1 5, 6 2, 7 3)"
cs1 = "CIRCULARSTRING(1 5, 5 5, 7 3)"
cs2 = "CIRCULARSTRING(4 1, 7 4, 4 7, 1 4, 4 1)"
cs3 = """CIRCULARSTRING( 0 0 0 0,
    0.26794919243112270647255365849413 1 3 -2,
    0.5857864376269049511983112757903 1.4142135623730950488016887242097 1 2)"""
cs4 = """CIRCULARSTRING(
                0 -2,
                -2 0,
                0 2,
                2 0,
                0 -2)"""
cs5 = "CIRCULARSTRING(-2 0,0 2,2 0,0 2,2 4)"

gc0 = "GEOMETRYCOLLECTION(POINT(4 6),LINESTRING(4 6,7 10))"
gc1 = """GEOMETRYCOLLECTION(
          POINT(99 98),
          LINESTRING(1 1, 3 3),
          POLYGON((0 0, 0 1, 1 1, 0 0)),
          POLYGON((0 0, 0 9, 9 9, 9 0, 0 0), (5 5, 5 6, 6 6, 5 5)),
          MULTIPOLYGON(((0 0, 0 9, 9 9, 9 0, 0 0), (5 5, 5 6, 6 6, 5 5)))
        )"""
gc2 = """GEOMETRYCOLLECTION(MULTIPOINT((3433276.43 5795308.93),
    (3428545.3 5795827.75), (3431576.99 5799084.19), (3431724.2 5797152.59),
    (3431984.2 5796564.79), (3435147.61 5797649.58), (3434660.86 5796941.74)
    ),
    MULTILINESTRING((3429562.6 5799490.68,3429750.99 5799199.87,
    3429825.45 5799078.39,3429901.8 5798961.45,3429995.54 5798822.93,
    3430072.89 5798719.46,3430216 5798558.95,3430272.08 5798489.33,
    3430393.87 5798328.51,3430463.53 5798251.11,3430532.22 5798190.16,
    3430591.24 5798149.53,3430667.67 5798108.9,3430723.78 5798088.58,
    3430797.33 5798067.95,3430857.34 5798056.34,3430912.52 5798051.5,
    3430961.89 5798048.59,3431052.88 5798053.43,3431159.36 5798059.24,
    3431218.41 5798061.18,3431366.56 5798056.09,3431474.07 5798044.47,
    3431568.02 5798028.97,3431644.53 5798012.51),(3433260.06 5797002.92,
    3433234.61 5797070.25,3433138.56 5797278.81,3433074.19 5797398.94,
    3433033.73 5797461.79,3432961.43 5797551.84,3432882.76 5797626.57,
    3432780.32 5797701.09,3432706.28 5797743.23,3432542.66 5797808.05,
    3432360.32 5797842.47,3432258.52 5797836.77,3432197.62 5797837.57,
    3432081.75 5797865.64,3431876.6 5797945.1,3431865.15 5797948.73),
    (3431865.15 5797948.73,3431644.53 5798012.51),
    (3431865.15 5797948.73,3431815.75 5797807.76),
    (3433260.06 5797002.92,3433361.19 5796788.54,3433467.4 5796572.78,3433670.6 5796160.06),
    (3433670.6 5796160.06,3433709.27 5796096.88,3433744.46 5796021.84,
    3433861.98 5795869.38,3434029.1 5795680.43,3434229.42 5795456.34,
    3434239.36 5795425.11,3434296.02 5795363.18)))"""
gc3 = "GEOMETRYCOLLECTION(POINT( 1 2 ))"
gc4 = "GEOMETRYCOLLECTION(POINT( 1 2 3))"
gc5 = "GEOMETRYCOLLECTION(LINESTRING( 1 2 3 , 4 5 6 , 7 8 9 , 10 11 12, 13 14 15))"
gc6 = """GEOMETRYCOLLECTION(
    POLYGON( (0 0 1, 10 0 1, 10 10 1, 0 10 1, 0 0 1),
    (5 5 1, 7 5 1, 7 7 1 , 5 7 1, 5 5 1) ))"""
ls0 = "LINESTRING (30 10, 10 30, 40 40)"
ls1 = """LINESTRING (
                0 0,
                0 9,
                9 9,
                9 0,
                0 0
            )"""

ls2 = """LINESTRING(3429562.6 5799490.68,3429750.99 5799199.87,3429825.45
    5799078.39,3429901.8 5798961.45,3429995.54 5798822.93,3430072.89
    5798719.46,3430216 5798558.95,3430272.08 5798489.33,3430393.87
    5798328.51,3430463.53 5798251.11,3430532.22 5798190.16,3430591.24
    5798149.53,3430667.67 5798108.9,3430723.78 5798088.58,3430797.33
    5798067.95,3430857.34 5798056.34,3430912.52 5798051.5,3430961.89
    5798048.59,3431052.88 5798053.43,3431159.36 5798059.24,3431218.41
    5798061.18,3431366.56 5798056.09,3431474.07 5798044.47,3431568.02
    5798028.97,3431644.53 5798012.51)"""
ls3 = "LINESTRING(0 0 2, 10 0 4, 10 10 6, 0 10 8, 0 0 10)"


mc0 = "MULTICURVE((5 5,3 5,3 3,0 3),CIRCULARSTRING(0 0,2 1,2 2))"
mc1 = """MULTICURVE(
                (0 0, 3 2),
                (4 8, 9 8),
                (2 9, 4 8))"""
mc2 = """MULTICURVE((
    5 5 1 3,
    3 5 2 2,
    3 3 3 1,
    0 3 1 1)
    ,CIRCULARSTRING(
    0 0 0 0,
    0.26794919243112270647255365849413 1 3 -2,
    0.5857864376269049511983112757903 1.4142135623730950488016887242097 1 2))
    """
mc3 = """MULTICURVE M((
    5 5 3,
    3 5 2,
    3 3 1,
    0 3 1)
    ,CIRCULARSTRING(
    0 0 0,
    0.26794919243112270647255365849413 1 -2,
    0.5857864376269049511983112757903 1.4142135623730950488016887242097 2))"""
mls0 = "MULTILINESTRING ((10 10, 20 20, 10 40),(40 40, 30 30, 40 20, 30 10))"
mls1 = """MULTILINESTRING((3429562.6 5799490.68,3429750.99 5799199.87,
    3429825.45 5799078.39,3429901.8 5798961.45,3429995.54 5798822.93,
    3430072.89 5798719.46,3430216 5798558.95,3430272.08 5798489.33,
    3430393.87 5798328.51,3430463.53 5798251.11,3430532.22 5798190.16,
    3430591.24 5798149.53,3430667.67 5798108.9,3430723.78 5798088.58,
    3430797.33 5798067.95,3430857.34 5798056.34,3430912.52 5798051.5,
    3430961.89 5798048.59,3431052.88 5798053.43,3431159.36 5798059.24,
    3431218.41 5798061.18,3431366.56 5798056.09,3431474.07 5798044.47,
    3431568.02 5798028.97,3431644.53 5798012.51),(3433260.06 5797002.92,
    3433234.61 5797070.25,3433138.56 5797278.81,3433074.19 5797398.94,
    3433033.73 5797461.79,3432961.43 5797551.84,3432882.76 5797626.57,
    3432780.32 5797701.09,3432706.28 5797743.23,3432542.66 5797808.05,
    3432360.32 5797842.47,3432258.52 5797836.77,3432197.62 5797837.57,
    3432081.75 5797865.64,3431876.6 5797945.1,3431865.15 5797948.73),
    (3431865.15 5797948.73,3431644.53 5798012.51),
    (3431865.15 5797948.73,3431815.75 5797807.76),
    (3433260.06 5797002.92,3433361.19 5796788.54,3433467.4 5796572.78,
    3433670.6 5796160.06),
    (3433670.6 5796160.06,3433709.27 5796096.88,3433744.46 5796021.84,
    3433861.98 5795869.38,3434029.1 5795680.43,3434229.42 5795456.34,
    3434239.36 5795425.11,3434296.02 5795363.18))"""
mls2 = """MULTILINESTRING( (0 0 0, 1 1 0, 2 2 0, 3 3 0, 4 4 0),
    (0 0 0, 1 1 0, 2 2 0, 3 3 0, 4 4 0),
    (1 2 3 , 4 5 6 , 7 8 9 , 10 11 12, 13 14 15) )"""
mls3 = """MULTILINESTRING((0 0 2, 10 0 4, 10 10 6, 0 10 8, 0 0 10),
    (2 2 1, 2 4 2, 4 4 3, 4 2 4, 2 2 5),
    (5 5 10, 5 7 9, 7 7 8, 7 5 7, 5 5 6))"""
#3dm
mls4 = """MULTILINESTRING M((0 0 2, 10 0 4, 10 10 6, 0 10 8, 0 0 10),
    (2 2 1, 2 4 2, 4 4 3, 4 2 4, 2 2 5),
    (5 5 10, 5 7 9, 7 7 8, 7 5 7, 5 5 6))"""
#4dm
mls5 = """MULTILINESTRING((0 0 2 9, 10 0 4 9, 10 10 6 9, 0 10 8 9, 0 0 10 9),
    (2 2 1 9, 2 4 2 9, 4 4 3 9, 4 2 4 9, 2 2 5 9),
    (5 5 10 9, 5 7 9 9, 7 7 8 9, 7 5 7 9, 5 5 6 9))"""

mp0 = "MULTIPOINT ((10 40), (40 30), (20 20), (30 10))"
mp1 = "MULTIPOINT (10 40, 40 30, 20 20, 30 10)"
mp2 = """MULTIPOINT(3433276.43 5795308.93,3428545.3 5795827.75,3431576.99
    5799084.19,3431724.2 5797152.59,3431984.2 5796564.79,3435147.61
    5797649.58,3434660.86 5796941.74,3434674.52 5797030.54,3435714.36
    5797022.6,3436368.88 5796951.04,3436730.03 5796768.6,3435538.55
    5796267.1,3435847.22 5795917.96,3434312.09 5794846.02,3433121.69
    5793670.73,3433176.36 5793489.29,3434316.04 5793940.09,3433222.92
    5793040.49,3433416.13 5792891.62,3430717.47 5792600.58,3435384.08
    5792877.68,3435229.15 5792177.25,3435120 5792319.07,3435088.72
    5792111.21,3434484.89 5792110.2,3435777.91 5792419.49,3435717.37
    5794318.12,3436895.13 5794569.43,3437621.86 5793931.6,3435597.14
    5793467.9,3435246.51 5793394.63,3434722.1 5793374.87,3434712.16
    5793810.3,3434773.28 5793816.87,3434629.91 5793855.31,3434992.34
    5794140.1,3434927.13 5794252.29,3434958.58 5794286.16,3435120.48
    5794163.36,3435850.1 5791727.49,3435930.75 5791636.32,3436268.87
    5791882.68,3437110.23 5791664.12,3435960.34 5790928.2,3433545.81
    5789755.43,3439096.86 5790884.26,3438576.87 5795046.69,3438396.95
    5794858.59,3438193.25 5794695.6,3438447.92 5796130.77,
    3440688.22 5793670.37)"""
mp3 = "MULTIPOINTM(1 2 8, 2 2 5, 2 1 0)"
mp4 = "MULTIPOINT M((1 2 2))"
mpoly0 = """MULTIPOLYGON (((30 20, 10 40, 45 40, 30 20)),
    ((15 5, 40 10, 10 20, 5 10, 15 5)))"""
mpoly1 = """MULTIPOLYGON (((40 40, 20 45, 45 30, 40 40)),
    ((20 35, 45 20, 30 5, 10 10, 10 30, 20 35),
    (30 20, 20 25, 20 15, 30 20)))"""
mpoly2 = """MULTIPOLYGON (((
                0 0,
                0 3,
                4 3,
                4 0,
                0 0
            )), ((
                2 4,
                1 6,
                4 5,
                2 4
            ), (
                7 6,
                6 8,
                8 8,
                7 6
            )))"""
mpoly3 = """MULTIPOLYGON(((3429699.81 5795851.64,3429736.72 5795796.01,
    3429754.71 5795768.88,3429996.1 5795489.98,3430100.67 5795435.76,
    3430122.61 5795446.09,3430138.1 5795560.98,3430311.09 5795559.69,
    3430309.8 5795470.62,3430329.16 5795416.4,3430326.58 5795399.62,
    3430157.47 5795418.98,3430156.14 5795407.32,3430139.36 5795396.99,
    3429983.19 5795394.41,3429976.74 5795420.22,3429789.59 5795418.93,
    3429643.74 5795475.72,3429635.72 5795615.31,3429484.94 5795556.38,
    3429315.44 5795496.32,3429326.12 5795748.57,3429129.92 5795704.53,
    3429176.64 5795776.6,3429100.6 5795797.17,3428900.44 5795742.46,
    3428896.43 5795779.82,3428805.69 5795953.3,3428897.77 5796025.35,
    3428897.77 5796225.99,3428696.32 5796199.31,3428681.64 5796217.99,
    3428680.31 5796290.03,3428290.14 5796351.8,3428389.67 5796413.87,
    3428837.71 5796561.12,3428991.08 5796495.01,3429076.4 5796760.29,
    3429428.31 5796723.61,3429474.96 5796690.29,3429696.2 5796600.99,
    3429658.88 5796429.06,3429536.27 5796363.75,3429529.6 5796333.1,
    3429446.08 5796253.84,3429699.81 5795851.64)),
    ((3429857.62 5799440.07,3429873.86 5799496.16,3429904.86 5799503.55,
    3429972.77 5799561.12,3430034.77 5799577.36,3430031.82 5799639.36,
    3430139.59 5799691.03,3430146.97 5799724.99,3430271.57 5799792.88,
    3430289.29 5799776.64,3430312.91 5799662.95,3430416.27 5799710.2,
    3430419.22 5799614.22,3430268.61 5799612.75,3430291.3 5799203.76,
    3430255.86 5799175.7,3430214.51 5799347,3430183.49 5799355.87,
    3430180.54 5799366.2,3430146.57 5799367.68,3430142.14 5799349.96,
    3430065.35 5799375.06,3429961.97 5799426.75,3429857.62 5799440.07)))"""
mpoly_empty = "MULTIPOLYGON EMPTY"
ms0 = """MULTISURFACE(CURVEPOLYGON(
    CIRCULARSTRING(-2 0,-1 -1,0 0,1 -1,2 0,0 2,-2 0),(-1 0,0 0.5,1 0,0 1,-1 0)),
    ((7 8,10 10,6 14,4 11,7 8)))"""
ms1 = """MULTISURFACE(CURVEPOLYGON(CIRCULARSTRING(
                -2 0 0 0,
                -1 -1 1 2,
                0 0 2 4,
                1 -1 3 6,
                2 0 4 8,
                0 2 2 4,
                -2 0 0 0),
                (-1 0 1 2,
                0 0.5 2 4,
                1 0 3 6,
                0 1 3 4,
                -1 0 1 2)),
                ((7 8 7 8,
                10 10 5 5,
                6 14 3 1,
                4 11 4 6,
                7 8 7 8),
                (9 9 7 8,
                8 12 7 8,
                7 10 7 8,
                9 9 7 8)))"""


point_m0 = "POINT M (1 1 80)"
point_m1 = "POINT M(1 2 4.00001)"
p0 = "POINT (30 10)"
p_zm = "POINT ZM (1 1 5 60)"
p_z = "POINT Z (1 1 5)"
poly0 = "POLYGON ((30 10, 10 20, 20 40, 40 40, 30 10))"
poly1 = """POLYGON ((35 10, 10.1 20.0, 15 40, 45 45, 35 10),
    (20 30, 35 35, 30 20, 20 30))"""
poly2 = """POLYGON ((
                0 0,
                0 9,
                9 9,
                9 0,
                0 0
            ), (
                1 1,
                1 3,
                3 2,
                1 1
            ), (
                7 6,
                6 8,
                8 8,
                7 6
            ))"""
poly3 = """POLYGON ((
                0 0,
                0 9,
                9 9,
                9 0,
                0 0
            ))"""
poly4 = """POLYGON((3429857.62 5799440.07,3429873.86
    5799496.16,3429904.86 5799503.55,3429972.77 5799561.12,3430034.77
    5799577.36,3430031.82 5799639.36,3430139.59 5799691.03,3430146.97
    5799724.99,3430271.57 5799792.88,3430289.29 5799776.64,3430312.91
    5799662.95,3430416.27 5799710.2,3430419.22 5799614.22,3430268.61
    5799612.75,3430291.3 5799203.76,3430255.86 5799175.7,3430214.51
    5799347,3430183.49 5799355.87,3430180.54 5799366.2,3430146.57
    5799367.68,3430142.14 5799349.96,3430065.35 5799375.06,3429961.97
    5799426.75,3429857.62 5799440.07))"""

empty_p0 = "POINT EMPTY"
empty_p1 = 'POINT(EMPTY)'
empty_mp0 = 'MULTIPOINT EMPTY'
empty_mp1 = 'MULTIPOINT(EMPTY)'
empty_ls0 = 'LINESTRING EMPTY'
empty_ls1 = 'LINESTRING(EMPTY)'
empty_mls0 = 'MULTILINESTRING EMPTY'
empty_mls1 = 'MULTILINESTRING(EMPTY)'
empty_poly0 = 'POLYGON EMPTY'
empty_poly1 = 'POLYGON(EMPTY)'
empty_mpoly0 = 'MULTIPOLYGON EMPTY'
empty_mpoly1 = 'MULTIPOLYGON(EMPTY)'
empty_gc0 = 'GEOMETRYCOLLECTION EMPTY'
empty_gc1 = 'GEOMETRYCOLLECTION(EMPTY)'
empty_gc2 = 'GEOMETRYCOLLECTION((EMPTY))'

phs0 = """POLYHEDRALSURFACE(
((0 0 0, 0 0 1, 0 1 1, 0 1 0, 0 0 0)),
((0 0 0, 0 1 0, 1 1 0, 1 0 0, 0 0 0)),
((0 0 0, 1 0 0, 1 0 1, 0 0 1, 0 0 0)),
((1 1 0, 1 1 1, 1 0 1, 1 0 0, 1 1 0)),
((0 1 0, 0 1 1, 1 1 1, 1 1 0, 0 1 0)),
((0 0 1, 1 0 1, 1 1 1, 0 1 1, 0 0 1))
)"""

phs1 = """POLYHEDRALSURFACE Z (
    ((0 0 0, 0 1 0, 1 1 0, 1 0 0, 0 0 0)),
    ((0 0 0, 0 1 0, 0 1 1, 0 0 1, 0 0 0)),
    ((0 0 0, 1 0 0, 1 0 1, 0 0 1, 0 0 0)),
    ((1 1 1, 1 0 1, 0 0 1, 0 1 1, 1 1 1)),
    ((1 1 1, 1 0 1, 1 0 0, 1 1 0, 1 1 1)),
    ((1 1 1, 1 1 0, 0 1 0, 0 1 1, 1 1 1))
  )"""

tin0 = """TIN (((
                0 0 0,
                0 0 1,
                0 1 0,
                0 0 0
            )), ((
                0 0 0,
                0 1 0,
                1 1 0,
                0 0 0
            ))
            )"""
tri0 = """TRIANGLE((0 0 0,0 1 0,1 1 0,0 0 0))"""



start = 'well_known_text_representation'

class ParserTestCase(unittest.TestCase):

    def testCompoundcurve(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(cc0, rule_name=start)
        self.assertEqual(ast[0], 'COMPOUNDCURVE')
        ast = parser.parse(cc1, rule_name=start)
        self.assertEqual(ast[0], 'COMPOUNDCURVE')

    def testCurvepolygon(self):
        parser = WktParser(parseinfo=True)
        ast = parser.parse(cp0, rule_name=start)
        self.assertEqual(ast[0], 'CURVEPOLYGON')
        ast = parser.parse(cp1, rule_name=start)
        self.assertEqual(ast[0], 'CURVEPOLYGON')

    def testCircularstring(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(cs0, rule_name=start)
        self.assertEqual(ast[0], 'CIRCULARSTRING')
        ast = parser.parse(cs1, rule_name=start)
        self.assertEqual(ast[0], 'CIRCULARSTRING')
        ast = parser.parse(cs2, rule_name=start)
        self.assertEqual(ast[0], 'CIRCULARSTRING')
        ast = parser.parse(cs3, rule_name=start)
        self.assertEqual(ast[0], 'CIRCULARSTRING')
        ast = parser.parse(cs4, rule_name=start)
        self.assertEqual(ast[0], 'CIRCULARSTRING')
        ast = parser.parse(cs5, rule_name=start)
        self.assertEqual(ast[0], 'CIRCULARSTRING')

    def testGeometrycollection(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(gc0, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        ast = parser.parse(gc1, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        ast = parser.parse(gc2, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        ast = parser.parse(gc3, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        ast = parser.parse(gc4, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        ast = parser.parse(gc5, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        ast = parser.parse(gc6, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        ast = parser.parse(empty_gc0, rule_name=start)
        self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        self.assertEqual(ast[1], 'EMPTY')
        #ast = parser.parse(empty_gc1, rule_name=start)
        #self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')
        #ast = parser.parse(empty_gc2, rule_name=start)
        #self.assertEqual(ast[0], 'GEOMETRYCOLLECTION')

    def testLinestring(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(ls0, rule_name=start)
        self.assertEqual(ast[0], 'LINESTRING')
        ast = parser.parse(ls1, rule_name=start)
        self.assertEqual(ast[0], 'LINESTRING')
        ast = parser.parse(ls2, rule_name=start)
        self.assertEqual(ast[0], 'LINESTRING')
        ast = parser.parse(ls3, rule_name=start)
        self.assertEqual(ast[0], 'LINESTRING')
        ast = parser.parse(empty_ls0, rule_name=start)
        self.assertEqual(ast[0], 'LINESTRING')
        self.assertEqual(ast[1], 'EMPTY')
        #ast = parser.parse(empty_ls1, rule_name=start)

    def testMulticurve(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(mc0, rule_name=start)
        self.assertEqual(ast[0], 'MULTICURVE')
        ast = parser.parse(mc1, rule_name=start)
        self.assertEqual(ast[0], 'MULTICURVE')
        ast = parser.parse(mc2, rule_name=start)
        self.assertEqual(ast[0], 'MULTICURVE')
        ast = parser.parse(mc3, rule_name=start)
        self.assertEqual(ast[0], 'MULTICURVE')
        self.assertEqual(ast[1], 'M')

    def testMultilinestring(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(mls0, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')
        ast = parser.parse(mls1, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')
        ast = parser.parse(mls2, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')
        ast = parser.parse(mls3, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')
        ast = parser.parse(mls4, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')
        ast = parser.parse(mls5, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')
        ast = parser.parse(empty_mls0, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')
        ast = parser.parse(empty_mls1, rule_name=start)
        self.assertEqual(ast[0], 'MULTILINESTRING')



    def testMultipoint(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(mp0, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOINT')
        #ast = parser.parse(mp1, rule_name=start)
        #self.assertEqual(ast[0], 'MULTIPOINT')
        #ast = parser.parse(mp2, rule_name=start)
        #self.assertEqual(ast[0], 'MULTIPOINT')
        #ast = parser.parse(mp3, rule_name=start)
        #self.assertEqual(ast[0], 'MULTIPOINT')
        ast = parser.parse(mp4, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOINT')
        self.assertEqual(ast[1], 'M')
        ast = parser.parse(empty_mp0, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOINT')
        self.assertEqual(ast[1], 'EMPTY')
        ast = parser.parse(empty_mp1, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOINT')
        self.assertEqual(ast[1], ['(', 'EMPTY', [], ')'])


    def testMultipolygon(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(mpoly0, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOLYGON')
        ast = parser.parse(mpoly1, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOLYGON')
        ast = parser.parse(mpoly2, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOLYGON')
        ast = parser.parse(mpoly3, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOLYGON')
        ast = parser.parse(mpoly_empty, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOLYGON')
        self.assertEqual(ast[1], 'EMPTY')
        ast = parser.parse(empty_mpoly0, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOLYGON')
        self.assertEqual(ast[1], 'EMPTY')
        ast = parser.parse(empty_mpoly1, rule_name=start)
        self.assertEqual(ast[0], 'MULTIPOLYGON')
        self.assertEqual(ast[1], ['(', 'EMPTY', [], ')'])

    def testMultisurface(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(ms0, rule_name=start)
        self.assertEqual(ast[0], 'MULTISURFACE')
        ast = parser.parse(ms1, rule_name=start)
        self.assertEqual(ast[0], 'MULTISURFACE')

    def testPoint(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(point_m0, rule_name=start)
        self.assertEqual(ast[0], 'POINT')
        self.assertEqual(ast[1], 'M')
        ast = parser.parse(point_m1, rule_name=start)
        self.assertEqual(ast[0], 'POINT')
        self.assertEqual(ast[1], 'M')
        ast = parser.parse(p0, rule_name=start)
        self.assertEqual(ast[0], 'POINT')
        ast = parser.parse(p_z, rule_name=start)
        self.assertEqual(ast[0], 'POINT')
        self.assertEqual(ast[1], 'Z')
        ast = parser.parse(p_zm, rule_name=start)
        self.assertEqual(ast[0], 'POINT')
        self.assertEqual(ast[1], 'ZM')
        ast = parser.parse(empty_p0, rule_name=start)
        self.assertEqual(ast[0], 'POINT')
        self.assertEqual(ast[1], 'EMPTY')
        #ast = parser.parse(empty_p1, rule_name=start)
        #self.assertEqual(ast[0], 'POINT')
        #self.assertEqual(ast[1], 'EMPTY')

    def testPolygon(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(poly0, rule_name=start)
        self.assertEqual(ast[0], 'POLYGON')
        ast = parser.parse(poly1, rule_name=start)
        self.assertEqual(ast[0], 'POLYGON')
        ast = parser.parse(poly2, rule_name=start)
        self.assertEqual(ast[0], 'POLYGON')
        ast = parser.parse(poly3, rule_name=start)
        self.assertEqual(ast[0], 'POLYGON')
        ast = parser.parse(poly4, rule_name=start)
        self.assertEqual(ast[0], 'POLYGON')
        ast = parser.parse(empty_poly0, rule_name=start)
        self.assertEqual(ast[0], 'POLYGON')
        self.assertEqual(ast[1], 'EMPTY')
        ast = parser.parse(empty_poly1, rule_name=start)
        self.assertEqual(ast[0], 'POLYGON')
        self.assertEqual(ast[1], ['(', 'EMPTY', [], ')'])

    def testPolyhedralsurface(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(phs0, rule_name=start)
        self.assertEqual(ast[0], 'POLYHEDRALSURFACE')
        ast = parser.parse(phs1, rule_name=start)
        self.assertEqual(ast[0], 'POLYHEDRALSURFACE')

    def testTin(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(tin0, rule_name=start)
        self.assertEqual(ast[0], 'TIN')

    def testTriangle(self):
        parser = WktParser(parseinfo=False)
        ast = parser.parse(tri0, rule_name=start)
        self.assertEqual(ast[0], 'TRIANGLE')



class WKTParserTestCase(unittest.TestCase):

    def testPoint(self):
        p = from_wkt(empty_p0)
        self.assertEqual(p, {'type': 'Point', 'coordinates': None})
        self.assertRaises(NotImplementedError, from_wkt, p_zm)
        self.assertRaises(NotImplementedError, from_wkt, point_m0)
        p = from_wkt(p0)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        self.assertEqual(p, {'type': 'Point', 'coordinates': (30.0, 10.0)})
        p = from_wkt(p_z)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        self.assertEqual(p, {'type': 'Point', 'coordinates': (1.0, 1.0, 5.0)})

    def testLinestring(self):
        p = from_wkt(empty_ls0)
        self.assertEqual(p, {'type': 'LineString', 'coordinates': None})
        p = from_wkt(ls0)
        self.assertEqual(p, {'type': 'LineString', 'coordinates':
            ((30.0, 10.0), (10.0, 30.0), (40.0, 40.0))})
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(ls1)
        self.assertEqual(p, {'type': 'LineString', 'coordinates':
            ((0.0, 0.0), (0.0, 9.0), (9.0, 9.0), (9.0, 0.0), (0.0, 0.0))})
        p = from_wkt(ls2)
        self.assertEqual(p['type'], 'LineString')
        self.assertEqual(p['coordinates'][0], (3429562.6, 5799490.68))
        self.assertEqual(p['coordinates'][-1], (3431644.53, 5798012.51))
        self.assertEqual(len(p['coordinates']), 25)
        p = from_wkt(ls3)
        self.assertEqual(p, {'type': 'LineString', 'coordinates':
            ((0.0, 0.0, 2.0),
             (10.0, 0.0, 4.0),
             (10.0, 10.0, 6.0),
             (0.0, 10.0, 8.0),
             (0.0, 0.0, 10.0))})

    def testPolygon(self):
        p = from_wkt(poly0)
        self.assertEqual(p, {'type': 'Polygon', 'coordinates':
            (((30.0, 10.0), (10.0, 20.0), (20.0, 40.0),
            (40.0, 40.0), (30.0, 10.0)),)
            })
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(poly1)
        self.assertEqual(p, {'type': 'Polygon', 'coordinates':
                        (((35.0, 10.0), (10.1, 20.0),
                        (15.0, 40.0), (45.0, 45.0),
                        (35.0, 10.0)),
                        ((20.0, 30.0), (35.0, 35.0),
                        (30.0, 20.0), (20.0, 30.0)))})
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(poly2)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(poly3)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(poly4)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(empty_poly0)
        self.assertEqual(p, {'type': 'Polygon', 'coordinates': None})
        p = from_wkt(empty_poly1)
        self.assertEqual(p, {'type': 'Polygon', 'coordinates': None})

    def testMultipoint(self):
        p = from_wkt(empty_mp0)
        self.assertEqual(p, {'type': 'MultiPoint', 'coordinates': None})
        p = from_wkt(empty_mp1)
        self.assertEqual(p, {'type': 'MultiPoint', 'coordinates': None})
        p = from_wkt(mp0)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        self.assertEqual(p, {'type': 'MultiPoint', 'coordinates':
            ((10.0, 40.0), (40.0, 30.0), (20.0, 20.0), (30.0, 10.0))})

    def testMultilinestring(self):
        p = from_wkt(empty_mls0)
        self.assertEqual(p, {'type': 'MultiLineString', 'coordinates': None})
        p = from_wkt(empty_mls1)
        self.assertEqual(p, {'type': 'MultiLineString', 'coordinates': None})
        p = from_wkt(mls0)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        self.assertEqual(p, {'type': 'MultiLineString', 'coordinates':
                (((10.0, 10.0), (20.0, 20.0), (10.0, 40.0)),
                ((40.0, 40.0), (30.0, 30.0), (40.0, 20.0), (30.0, 10.0)))})
        p = from_wkt(mls0)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(mls0)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(mls1)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(mls3)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        #p = from_wkt(mls4)
        #self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        #p = from_wkt(mls5)
        #self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)

    def testMultipolygon(self):
        p = from_wkt(mpoly_empty)
        self.assertEqual(p, {'type': 'MultiPolygon', 'coordinates': None})
        p = from_wkt(empty_mpoly0)
        self.assertEqual(p, {'type': 'MultiPolygon', 'coordinates': None})
        p = from_wkt(empty_mpoly1)
        self.assertEqual(p, {'type': 'MultiPolygon', 'coordinates': None})
        p = from_wkt(mpoly0)
        #self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        self.assertEqual(p, {'type': 'MultiPolygon', 'coordinates':
            ((((30.0, 20.0), (10.0, 40.0), (45.0, 40.0), (30.0, 20.0)),),
            (((15.0, 5.0), (40.0, 10.0), (10.0, 20.0),
            (5.0, 10.0), (15.0, 5.0)),))})
        p = from_wkt(mpoly0)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(mpoly1)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(mpoly2)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(mpoly3)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)


    def testGeometrycollection(self):
        p = from_wkt(empty_gc0)
        self.assertEqual(p, {'type': 'GeometryCollection', 'geometries': None})
        p = from_wkt(gc0)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(gc1)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(gc2)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(gc3)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(gc4)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(gc5)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)
        p = from_wkt(gc6)
        self.assertEqual(p, pygeoif.as_shape(p).__geo_interface__)

class SpeedTest(unittest.TestCase):

    def test_speed(self):
        def parse_wkt(text):
            ast = parser.parse(text, rule_name='well_known_text_representation', semantics=semantics)
            if isinstance(ast, dict):
                return ast
            else:
                raise NotImplementedError
        from time import time
        arr = [
            #tri0, tin0, phs1, phs0,
            #empty_gc0, empty_gc1, empty_gc2,
            #empty_mpoly0, empty_mpoly1, empty_poly0, empty_poly1,
            #empty_mls1, empty_mls0, empty_ls1, empty_ls0, empty_mp0,
            #empty_mp1, empty_p0, empty_p1, mpoly_empty,
            poly0, poly1, poly2, poly3,
            poly4, point_m0, point_m1, p0, p_zm, p_z, ms0, ms1,
            mpoly0, mpoly1, mpoly2, mpoly3, mp0, mp1, mp2, mp3, mp4,
            mls0, mls1, mls2, mls3, mls4, mls5,
            #mc0, mc1, mc2, mc3,
            ls0, ls1, ls2, ls3, gc0, gc1, gc2, gc3, gc4, gc5, gc6,
            #cs0, cs1,
            #cs2, cs3, cs4, cs5, cp0, cp1, cc0, cc1
            ]
        parser = WktParser(parseinfo=False)
        semantics=Semantics()
        pwktf = 0
        pgif = 0
        for g in arr:
            try:
                from_wkt(g)
            except:
                pwktf +=1
            try:
                pygeoif.from_wkt(g)
            except:
                pgif +=1
        #print('Pygeoif Failures:', pgif)
        #print('ParseWKT failures:', pwktf)
        num_loops = 10
        t0 = time()
        for i in xrange(1, num_loops):
            for g in arr:
                try:
                    parse_wkt(g)
                except:
                    pwktf +=1
        pwktt = time() - t0
        t0 = time()
        for i in xrange(1, num_loops):
            for g in arr:
                try:
                    pygeoif.from_wkt(g)
                except:
                    pgif +=1
        pygit = time() - t0
        #print('Pygeoif time:', pygit)
        #print('ParseWKT time:', pwktt)
        #print('wkt/re:', pwktt/pygit)
        self.assertTrue(pwktt/pygit > 0)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParserTestCase))
    suite.addTest(unittest.makeSuite(WKTParserTestCase))
    return suite





if __name__ == '__main__':
    unittest.main()
