#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def u(x):
    if sys.version < '3':
        import codecs
        return codecs.unicode_escape_decode(x)[0]
    else:
        return x


from ascii_graph import Pyasciigraph

data = [(u'long_labe☭', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]

graph = Pyasciigraph()
for line in graph.graph(u'☭test print', data):
        print(line)

