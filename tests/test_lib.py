#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from __future__ import unicode_literals

import pytest
import sys

from ascii_graph import Pyasciigraph

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Red = "\x1b[31m"
    Bold_Red = "\x1b[31;1m"
    Green = "\x1b[32m"
    Bold_Green = "\x1b[32;1m"
    Yellow = "\x1b[33m"
    Bold_Yellow = "\x1b[33;1m"
    Blue = "\x1b[34m"
    Bold_Blue = "\x1b[34;1m"
    Magenta = "\x1b[35m"
    Bold_Magenta = "\x1b[35;1m"
    Cyan = "\x1b[36m"
    Bold_Cyan = "\x1b[36;1m"
    White = "\x1b[37"
    Bold_White = "\x1b[37;1m"

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
            test = [ ('testval0', 600), ('testval1', 400, bcolors.Red), ('testval2', 300, bcolors.Green), ('testval3', 200, bcolors.Yellow), ('testval2', 100, bcolors.Cyan), ('testval3', 50, bcolors.Blue) ]
            graph = Pyasciigraph()
            res = graph.graph('test graph', test)
            print res
            expected = [
'test graph',
'###############################################################################',
u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588  600  testval0',
u'\x1b[31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                        \x1b[0m\x1b[31m400\x1b[0m  testval1',
u'\x1b[32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                  \x1b[0m\x1b[32m300\x1b[0m  testval2',
u'\x1b[33m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                             \x1b[0m\x1b[33m200\x1b[0m  testval3',
u'\x1b[36m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                                        \x1b[0m\x1b[36m100\x1b[0m  testval2',
u'\x1b[34m\u2588\u2588\u2588\u2588\u2588                                                             \x1b[0m \x1b[34m50\x1b[0m  testval3']
            assert res == expected

        def test_mulivalue_color_graphs(self):
            test = [ ('testval0', 600), ('testval1', 400, bcolors.Red), ('testval2', [(300, bcolors.Green), (500, bcolors.Blue)]),
            ('testval3', [(200, bcolors.Yellow), (100,)]), ('testval4', 100, bcolors.Cyan), ('testval5', 50, bcolors.Blue),
            ('testval6', [(100, bcolors.Green), (150, bcolors.Red), (200, bcolors.Yellow), (600, bcolors.Blue)]) ]
            graph = Pyasciigraph(separator_length=4)
            res = graph.graph('test graph', test)
            print res
            expected = [
'test graph',
'#################################################################################',
u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                600    testval0',
u'\x1b[31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                     \x1b[0m            \x1b[31m400\x1b[0m    testval1',
u'\x1b[32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588             \x1b[0m        \x1b[32m300\x1b[0m,\x1b[34m500\x1b[0m    testval2',
u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[33m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                      \x1b[0m        \x1b[33m200\x1b[0m,100    testval3',
u'\x1b[36m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                              \x1b[0m            \x1b[36m100\x1b[0m    testval4',
u'\x1b[34m\u2588\u2588\u2588\u2588                                                  \x1b[0m             \x1b[34m50\x1b[0m    testval5',
u'\x1b[32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[31m\u2588\u2588\u2588\u2588\x1b[0m\x1b[33m\u2588\u2588\u2588\u2588\x1b[0m\x1b[34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588     \x1b[0m\x1b[32m100\x1b[0m,\x1b[31m150\x1b[0m,\x1b[33m200\x1b[0m,\x1b[34m600\x1b[0m    testval6']
            assert res == expected
