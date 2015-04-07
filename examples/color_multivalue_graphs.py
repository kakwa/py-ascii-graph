#!/bin/env python2

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *

test = [('testval0', 600),
           ('testval1', 400, Red),
           ('testval2', [(300, Gre), (500, Blu)]),
           ('testval3', [(200, Yel), (100,)]),
           ('testval4', 100, Cya),
           ('testval5', 50, Blu),
           ('testval6', [(100, Gre), (150, Red), (200, Yel), (600, Blu)])]
graph = Pyasciigraph(separator_length=4)
for line in graph.graph('test graph', test):
    print(line)

exit(0)
