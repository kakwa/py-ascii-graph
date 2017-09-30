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

def gprint(res):
    for l in res:
        print(l)

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
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_noansi_info(self):
            test = [('long_labe☭ (\033[92m+\033[0m)', 423), ('sl (\033[91m-\033[0m)', 1234), ('line3 (\033[91m-\033[0m)', 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph('☭test print', test)
            expected = [u'\u262dtest print', u'###############################################################################', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                         423  long_labe\u262d (\x1b[92m+\x1b[0m)', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588  1234  sl (\x1b[91m-\x1b[0m)        ', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                    531  line3 (\x1b[91m-\x1b[0m)     ', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                                   200  line4         ', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                      834  line5         ']
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_float_format(self):
            test = [('long_labe☭', 423.197), ('sl', 1234.12341), ('line3', 531.11), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph(float_format='{0:,.2f}')
            res = graph.graph('☭test print', test)
            expected = [
'☭test print',
'###############################################################################',
'███████████████████                                          423.20  long_labe☭',
'█████████████████████████████████████████████████████████  1,234.12  sl        ',
'████████████████████████                                     531.11  line3     ',
'█████████                                                    200.00  line4     ',
'██████████████████████████████████████                       834.00  line5     ',
]
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_zeros(self):
            test = [('long_labe☭', 0), ('sl', 0), ('line3', 0), ('line4', 0), ('line5', 0)]
            graph = Pyasciigraph()
            res = graph.graph('☭test print', test)
            expected = [
'☭test print',
'###############################################################################',
'                                                                  0  long_labe☭',
'                                                                  0  sl        ',
'                                                                  0  line3     ',
'                                                                  0  line4     ',
'                                                                  0  line5     ',
]
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_human_readable_si(self):
            test = [('long_labe☭', 1234), ('sl', 1231234), ('line3', 1231231234), ('line4', 1231231231234), ('line5', 1231231231231234), ('line6', 1231231231231231234), ('line7', 1231231231231231231234), ('line8', 1231231231231231231231234), ('line9', 123231231231231231231231234)]
            graph = Pyasciigraph(human_readable='si')
            res = graph.graph('☭test print', test)
            expected = [
'☭test print',
'###############################################################################',          
'                                                                 1K  long_labe☭',                    
'                                                                 1M  sl        ',
'                                                                 1G  line3     ',
'                                                                 1T  line4     ',
'                                                                 1P  line5     ',
'                                                                 1E  line6     ',
'                                                                 1Z  line7     ',
'                                                                 1Y  line8     ',
'█████████████████████████████████████████████████████████████  123Y  line9     ',
]
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_human_readable_cs(self):
            test = [('long_labe☭', 1234), ('sl', 1231234), ('line3', 1231231234), ('line4', 1231231231234), ('line5', 1231231231231234), ('line6', 1231231231231231234), ('line7', 1231231231231231231234), ('line8', 1231231231231231231231234)]
            graph = Pyasciigraph(human_readable='cs')
            res = graph.graph('☭test print', test)
            expected = [
'☭test print', 
'###############################################################################',          
'                                                                 1K  long_labe☭',                    
'                                                                 1M  sl        ',
'                                                                 1G  line3     ',
'                                                                 1T  line4     ',
'                                                                 1P  line5     ',
'                                                                 1E  line6     ',
'                                                                 1Z  line7     ',
'███████████████████████████████████████████████████████████████  1Y  line8     '
]
            gprint(res)
            gprint(expected)
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
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_no_label(self):
            test = [(1, 423), (2, 1234), (3, 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph()
            res = graph.graph(data=test)
            expected = [
'██████████████████████                                               423  1    ',
'██████████████████████████████████████████████████████████████████  1234  2    ',
'████████████████████████████                                         531  3    ',
'██████████                                                           200  line4',
'████████████████████████████████████████████                         834  line5',
]
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_vcolor(self):
            from ascii_graph.colordata import vcolor
            
            test = [('testval0', 600),
                    ('testval1', 500),
                    ('testval2', 400),
                    ('testval3', 400),
                    ('testval4', 300),
                    ('testval5', 200),
                    ('testval6', 100),
                    ('testval7', 50 )]
            
            expected = [('testval0', 600, Gre),
                    ('testval1', 500, Yel),
                    ('testval2', 400, Red),
                    ('testval3', 400, Gre),
                    ('testval4', 300, Yel),
                    ('testval5', 200, Red),
                    ('testval6', 100, Gre),
                    ('testval7', 50,  Yel)]
 
            pattern = [Gre, Yel, Red]
            
            data = vcolor(test, pattern)
            assert data == expected

        def test_alternate_graphsymbol(self):
            test = [('long_labe☭', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph(graphsymbol='*')
            res = graph.graph('☭test print', test)
            expected = [
'☭test print',
'###############################################################################',
'********************                                            423  long_labe☭',
'*************************************************************  1234  sl        ',
'**************************                                      531  line3     ',
'*********                                                       200  line4     ',
'*****************************************                       834  line5     ',
]
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_graphsymbol_bad_length(self):
            test = [('long_labe☭', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
            with pytest.raises(Exception) as e:
                graph = Pyasciigraph(graphsymbol='*0')

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
            expected = [u'test graph', u'###############################################################################', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                                                142  testval0', u'\x1b[1;35m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                        \x1b[1;35m204\x1b[0m  testval1', u'\x1b[4;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m  \x1b[4;31m501\x1b[0m  testval2', u'\x1b[0;91m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                                     \x1b[0;91m103\x1b[0m  testval3', u'\x1b[1;92m\u2588\u2588\u2588\x1b[0m                                                                \x1b[1;92m29\x1b[0m  testval4', u'\x1b[4;33m\u2588\u2588\x1b[0m                                                                 \x1b[4;33m19\x1b[0m  testval5', u'\x1b[0;96m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                                       \x1b[0;96m99\x1b[0m  testval6', u'\x1b[1;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m               \x1b[1;34m404\x1b[0m  testval7'] 
            gprint(res)
            gprint(expected)
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
            expected = [u'test graph', u'#################################################################################', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                600    testval0', u'\x1b[0;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                 \x1b[0;31m400\x1b[0m    testval1', u'\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                     \x1b[0;32m300\x1b[0m,\x1b[0;34m500\x1b[0m    testval2', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0;33m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                              \x1b[0;33m200\x1b[0m,100    testval3', u'\x1b[0;36m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                                          \x1b[0;36m100\x1b[0m    testval4', u'\x1b[0;34m\u2588\u2588\u2588\u2588\x1b[0m                                                               \x1b[0;34m50\x1b[0m    testval5', u'\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;31m\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;33m\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m     \x1b[0;32m100\x1b[0m,\x1b[0;31m150\x1b[0m,\x1b[0;33m200\x1b[0m,\x1b[0;34m600\x1b[0m    testval6']
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_mulivalue_color_graphs_max(self):
            test = [('testval0', 600),
                       ('testval1', 400, Red),
                       ('testval2', [(300, Gre),(500, Blu)]),
                       ('testval3', [(200, Yel),(100,)]),
                       ('testval4', 100, Cya),
                       ('testval5', 50, Blu),
                       ('testval6', [(100, Gre), (150, Red), (200, Yel), (600, Blu)]) ]
            graph = Pyasciigraph(separator_length=4, multivalue=False)
            res = graph.graph('test graph', test)
            expected = [u'test graph', u'###############################################################################', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588    600    testval0', u'\x1b[0;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                        \x1b[0;31m400\x1b[0m    testval1', u'\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m              \x1b[0;34m500\x1b[0m    testval2', u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0;33m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                            \x1b[0;33m200\x1b[0m    testval3', u'\x1b[0;36m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                                      \x1b[0;36m100\x1b[0m    testval4', u'\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\x1b[0m                                                            \x1b[0;34m50\x1b[0m    testval5', u'\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;31m\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;33m\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m    \x1b[0;34m600\x1b[0m    testval6']

            gprint(res)
            gprint(expected)
            assert res == expected

        def test_force_max_value_param(self):
            test = [('long_labe☭', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
            graph = Pyasciigraph(force_max_value=2000)
            res = graph.graph('☭test print', test)
            expected = [
'☭test print',
'###############################################################################',
'████████████                                                    423  long_labe☭',
'█████████████████████████████████████                          1234  sl        ',
'████████████████                                                531  line3     ',
'██████                                                          200  line4     ',
'█████████████████████████                                       834  line5     '
]
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_neg_simple(self):
            test = [('testval0', 600),
                    ('testval1', 500),
                    ('testval2', -400),
                    ('testval3', 400),
                    ('testval4', 300),
                    ('testval5', 200),
                    ('testval6', 100),
                    ('testval7', 50 )]
            graph = Pyasciigraph()
            res = graph.graph('☭test print', test)
            expected = [
'☭test print',
'###############################################################################',
'                         █████████████████████████████████████    600  testval0',
'                         ███████████████████████████████          500  testval1',
'█████████████████████████                                        -400  testval2',
'                         █████████████████████████                400  testval3',
'                         ██████████████████                       300  testval4',
'                         ████████████                             200  testval5',
'                         ██████                                   100  testval6',
'                         ███                                       50  testval7',
]
            gprint(res)
            gprint(expected)
            assert res == expected

        def test_neg_multicolor(self):
            test = [('testval0', 600),
                    ('testval1', 400, Red),
                    ('testval2', [(600, Gre), (500, Blu)]),
                    ('testval3', [(200, Yel), (100,)]),
                    ('testval4', -170, Cya),
                    ('testval5', 50, Blu),
                    ('testval6', [(-300, Gre), (-230, Red)]),
                    ('testval7', [(-100, Gre), (-230, Red), (200, Yel), (600, Blu)])]
            graph = Pyasciigraph()
            res = graph.graph('☭test print', test)
            expected = [u'\u262dtest print', u'###############################################################################', u'                \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588                 600  testval0', u'                \x1b[0;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                            \x1b[0;31m400\x1b[0m  testval1', u'                \x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\x1b[0m              \x1b[0;32m600\x1b[0m,\x1b[0;34m500\x1b[0m  testval2', u'                \u2588\u2588\u2588\u2588\u2588\x1b[0;33m\u2588\u2588\u2588\u2588\u2588\x1b[0m                                    \x1b[0;33m200\x1b[0m,100  testval3', u'       \x1b[0;36m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                                 \x1b[0;36m-170\x1b[0m  testval4', u'                \x1b[0;34m\u2588\u2588\x1b[0m                                                 \x1b[0;34m50\x1b[0m  testval5', u' \x1b[0;32m\u2588\u2588\u2588\x1b[0m\x1b[0;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m                                            \x1b[0;32m-300\x1b[0m,\x1b[0;31m-230\x1b[0m  testval6', u'    \x1b[0;31m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;32m\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;33m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m\x1b[0;34m\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\x1b[0m   \x1b[0;32m-100\x1b[0m,\x1b[0;31m-230\x1b[0m,\x1b[0;33m200\x1b[0m,\x1b[0;34m600\x1b[0m  testval7']
            gprint(res)
            gprint(expected)
            assert res == expected
