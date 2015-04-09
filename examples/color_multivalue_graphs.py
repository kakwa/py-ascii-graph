#!/bin/env python2

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *

test = [('testval0', 600),
           ('testval1', 400, Red),
           ('testval2', [(600, Gre), (500, Blu)]),
           ('testval3', [(200, Yel), (100,)]),
           ('testval4', 100, Cya),
           ('testval5', 50, Blu),
           ('testval6', [(100, Gre), (150, Red), (200, Yel), (600, Blu)])]

# Multicolor with all the values displayed
graph = Pyasciigraph(separator_length=4)
for line in graph.graph('test graph', test):
    print(line)

# Multicolor with only the max value displayed
graph = Pyasciigraph(separator_length=4, multivalue=False)
for line in graph.graph('test graph mono value', test):
    print(line)

# Coloring data according to thresholds
from ascii_graph.colordata import hcolor

test = [('testval0', 600),
        ('testval1', 500),
        ('testval2', 400),
        ('testval3', 400),
        ('testval4', 300),
        ('testval5', 200),
        ('testval6', 100),
        ('testval7', 50 )]

thresholds = {
  51:  Gre,
  100: Blu,
  350: Yel,
  500: Red,
}

data = hcolor(test, thresholds)
for line in graph.graph('hcolor test', data):
    print(line)

exit(0)
