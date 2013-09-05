#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from __future__ import unicode_literals

import pytest
import sys

from ascii_graph import Pyasciigraph

def u(x):
    if sys.version < '3':
        import codecs
        return codecs.unicode_escape_decode(x)[0]
    else:
        return x

class TestLib(object):

        def test_unsorted_default_params(self):
            test = [('long_labe☭', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph('☭test print', test)
            expected = [
'☭test print', 
'###############################################################################', 
'████████████████████                                            423  long_labe☭',
'█████████████████████████████████████████████████████████████  1234  sl        ',
'██████████████████████████                                      531  line3     ',
'█████████                                                       200  line4     ',
'█████████████████████████████████████████                       834  line5     ',
]
            assert res == expected

        def test_type_output(self):
            test = [('long_labe☭', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph('test print', test)
            if sys.version < '3':
                expected = unicode
            else:
                expected = str
            for line in res:
                assert type(line) == expected


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

        def test_sorted(self):
            test = [(1, 423), (2, 1234), (3, 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph('test 2', test, sort=1)
            expected = [
'test 2',
'###############################################################################',
'██████████                                                           200  line4',
'██████████████████████                                               423  1    ',
'████████████████████████████                                         531  3    ',
'████████████████████████████████████████████                         834  line5',
'██████████████████████████████████████████████████████████████████  1234  2    ',
]
            assert res == expected

        def test_reverse_sorted(self):
            test = [(1, 423), (2, 1234), (3, 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph('test 2', test, sort=2)
            expected = [
'test 2',
'###############################################################################',
'██████████████████████████████████████████████████████████████████  1234  2    ',
'████████████████████████████████████████████                         834  line5',
'████████████████████████████                                         531  3    ',
'██████████████████████                                               423  1    ',
'██████████                                                           200  line4',
]
            assert res == expected

