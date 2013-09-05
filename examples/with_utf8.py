#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if sys.version > '3':
    print "this example only work with python 2"
    exit(1)

from ascii_graph import Pyasciigraph

data = [(u'long_labe☭', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]

graph = Pyasciigraph()
for line in graph.graph(u'☭test print', data):
        print(line.encode('utf-8'))

