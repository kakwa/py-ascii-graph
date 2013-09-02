#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import pytest

from ascii_graph import Pyasciigraph

class TestLib(object):

        def test_unsorted_default_params(self):
            test = [('long_label', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph('test print', test)
            expected = [
'test print', 
'###############################################################################', 
'████████████████████                                            423  long_label',
'█████████████████████████████████████████████████████████████  1234  sl        ',
'██████████████████████████                                      531  line3     ',
'█████████                                                       200  line4     ',
'█████████████████████████████████████████                       834  line5     ',
]
            assert res == expected

        def test_convert_label(self):
            test = [(1, 423), (2, 1234), (3, 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph('test print', test)
            expected = [
'test print', 
'###############################################################################', 
'██████████████████████                                               423  1    ',
'██████████████████████████████████████████████████████████████████  1234  2    ',
'████████████████████████████                                         531  3    ',
'██████████                                                           200  line4',
'████████████████████████████████████████████                         834  line5',
]
            assert res == expected

