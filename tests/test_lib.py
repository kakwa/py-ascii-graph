#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from __future__ import unicode_literals
from ascii_graph.colors import *

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

        def test_color_graphs(self):
            test = [('testval0', 142),
                       ('testval1', 204, BPur),
                       ('testval2', 501, URed),
                       ('testval3', 103, IRed),
                       ('testval4',  29, BIGre),
                       ('testval5',  19, UYel),
                       ('testval6',  99, ICya),
                       ('testval7', 404, BBlu)]
            graph = Pyasciigraph()
            res = graph.graph('test graph', test)
            expected = [u'test graph', u'###############################################################################', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                                142  testval0', u'\x1b[1;35m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                        \x1b[0m\x1b[1;35m204\x1b[0m  testval1', u'\x1b[4;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588  \x1b[0m\x1b[4;31m501\x1b[0m  testval2', u'\x1b[0;91m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                                     \x1b[0m\x1b[0;91m103\x1b[0m  testval3', u'\x1b[1;92m\u2588\u2588\u2588                                                               \x1b[0m \x1b[1;92m29\x1b[0m  testval4', u'\x1b[4;33m\u2588\u2588                                                                \x1b[0m \x1b[4;33m19\x1b[0m  testval5', u'\x1b[0;96m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                                      \x1b[0m \x1b[0;96m99\x1b[0m  testval6', u'\x1b[1;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588               \x1b[0m\x1b[1;34m404\x1b[0m  testval7']
            assert res == expected

        def test_mulivalue_color_graphs(self):
            test = [('testval0', 600),
                       ('testval1', 400, Red),
                       ('testval2', [(300, Gre),(500, Blu)]),
                       ('testval3', [(200, Yel),(100,)]),
                       ('testval4', 100, Cya),
                       ('testval5', 50, Blu),
                       ('testval6', [(100, Gre), (150, Red), (200, Yel), (600, Blu)]) ]
            graph = Pyasciigraph(separator_length=4)
            res = graph.graph('test graph', test)
            expected = [u'test graph', u'#################################################################################', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                600    testval0', u'\x1b[0;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                     \x1b[0m            \x1b[0;31m400\x1b[0m    testval1', u'\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588             \x1b[0m        \x1b[0;32m300\x1b[0m,\x1b[0;34m500\x1b[0m    testval2', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0;33m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                      \x1b[0m        \x1b[0;33m200\x1b[0m,100    testval3', u'\x1b[0;36m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                              \x1b[0m            \x1b[0;36m100\x1b[0m    testval4', u'\x1b[0;34m\u2588\u2588\u2588\u2588                                                  \x1b[0m             \x1b[0;34m50\x1b[0m    testval5', u'\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;31m\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;33m\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588     \x1b[0m\x1b[0;32m100\x1b[0m,\x1b[0;31m150\x1b[0m,\x1b[0;33m200\x1b[0m,\x1b[0;34m600\x1b[0m    testval6']
            assert res == expected
