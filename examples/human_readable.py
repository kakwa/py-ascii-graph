#!/bin/env python2

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *

test = [('testval0', 123456),
           ('testval1', 918829, Red),
           ('testval2', [(600192, Gre), (500203, Blu)]),
           ('testval3', [(2, Yel), (10,)]),
           ('testval4', 10, Cya),
           ('testval5', 50, Blu),
           ('testval6', [(1001233, Gre), (150000, Red), (100000, Yel), (60, Blu)])]

# Multicolor with all the values displayed
graph = Pyasciigraph(separator_length=4, human_readable='cs')
for line in graph.graph('test graph', test):
    print(line)

# Multicolor with only the max value displayed
graph = Pyasciigraph(separator_length=4, multivalue=False, human_readable='cs')
for line in graph.graph('test graph mono value', test):
    print(line)

# Coloring data according to thresholds
from ascii_graph.colordata import hcolor

test = [('testval0', 6003),
        ('testval1', 900),
        ('testval2', 4920),
        ('testval3', 400),
        ('testval4', 30),
        ('testval5', 200),
        ('testval6', 1025),
        ('testval7', 5023 )]

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
