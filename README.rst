The WKT Parser was gernerated using grako https://pypi.python.org/pypi/grako

The ebnf file is the translation of https://github.com/ahinz/postgis/blob/master/doc/bnf-wkt.txt .

The bnf to ebnf conversion was guided by http://stackoverflow.com/questions/14922242/how-to-convert-bnf-to-ebnf

The generation of parse.py is as easy as: /path/to/grako Wkt.ebnf -o parse.py
