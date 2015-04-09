#!/bin/env python2

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *

# Simple coloring
test = [('testval0', 600),
        ('testval1', 500, Pur),
        ('testval2', 400, Red),
        ('testval3', 400, Red),
        ('testval4', 300, Gre),
        ('testval5', 200, Yel),
        ('testval6', 100, Cya),
        ('testval7', 50,  Blu) ]

graph = Pyasciigraph()
for line in graph.graph('test graph', test):
    print(line)


# Bold and underline
test = [('testval0', 142),
        ('testval1', 204, BPur),
        ('testval2', 501, URed),
        ('testval3', 103, IRed),
        ('testval4',  29, BIGre),
        ('testval5',  19, UYel),
        ('testval6',  99, ICya),
        ('testval7', 404, BBlu)]
graph = Pyasciigraph()
for line in graph.graph('test graph', test):
    print(line)


# Coloring data according to a pattern (one color each line)
from ascii_graph.colordata import vcolor

test = [('testval0', 600),
        ('testval1', 500),
        ('testval2', 400),
        ('testval3', 400),
        ('testval4', 300),
        ('testval5', 200),
        ('testval6', 100),
        ('testval7', 50 )]

pattern = [Gre, Yel, Red]

data = vcolor(test, pattern)
for line in graph.graph('vcolor test', data):
    print(line)

exit(0)
