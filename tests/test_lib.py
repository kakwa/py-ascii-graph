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
u'###############################################################################', 
u'████████████████████                                            423  long_label',
u'█████████████████████████████████████████████████████████████  1234  sl        ',
u'██████████████████████████                                      531  line3     ',
u'█████████                                                       200  line4     ',
u'█████████████████████████████████████████                       834  line5     ',
]
            assert res == expected
