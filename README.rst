The WKT Parser was gernerated using grako https://pypi.python.org/pypi/grako

The ebnf file is the translation of http://svn.osgeo.org/postgis/trunk/doc/bnf-wkt.txt

The bnf to ebnf conversion was guided by http://stackoverflow.com/questions/14922242/how-to-convert-bnf-to-ebnf

The generation of parse.py is as easy as: /path/to/grako Wkt.ebnf -o parse.py

parsewkt is continually tested with *Travis CI*

.. image:: https://api.travis-ci.org/cleder/parsewkt.png
    :target: https://travis-ci.org/cleder/parsewkt

.. image:: https://coveralls.io/repos/cleder/parsewkt/badge.png?branch=master
    :target: https://coveralls.io/r/cleder/parsewkt?branch=master
