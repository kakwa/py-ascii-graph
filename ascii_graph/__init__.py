#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

class Pyasciigraph:

    def __init__(self, line_length=79, 
            min_graph_length=50, 
            separator_length=2
            ):
        """Constructor of Pyasciigraph
        
        :param int line_length: the max number of char on a line
                if any line cannot be shorter, 
                it will go over this limit
        :param int min_graph_length: the min number of char used by the graph
        :param int separator_length: the length of field separator
        """
        self.line_length = line_length
        self.separator_length = separator_length
        self.min_graph_length = min_graph_length

    def _u(self, x):
        if sys.version < '3':
            import codecs
            return codecs.unicode_escape_decode(x)[0]
        else:
            return x

    def _get_maximum(self, data):
        all_max = {}
        all_max['value_max_length'] = 0
        all_max['info_max_length'] = 0
        all_max['max_value'] = 0

        for (info, value) in data:
            if value > all_max['max_value']:
                all_max['max_value'] = value

            if len(info) > all_max['info_max_length']:
                all_max['info_max_length'] = len(info)
            
            if len(str(value)) > all_max['value_max_length']:
                all_max['value_max_length'] = len(str(value))
        return all_max

    def _gen_graph_string(self, value, max_value, graph_length, start_value):
        number_of_square = int(value * graph_length / max_value)
        number_of_space = int(start_value - number_of_square)
        return '█' * number_of_square + self._u(' ') * number_of_space

    def _gen_info_string(self, info, start_info, line_length):
        number_of_space = (line_length - start_info - len(info))
        return info + self._u(' ') * number_of_space

    def _gen_value_string(self, value, start_value, start_info):
        number_space = start_info -\
                start_value -\
                len(str(value)) -\
                self.separator_length

        return  ' ' * number_space +\
                str(value) +\
                ' ' * self.separator_length

    def _sanitize_string(self, string):
        #get the type of a unicode string
        unicode_type = type(self._u('t'))
        input_type = type(string)
        if input_type is str:
            if sys.version < '3':
                info = unicode(string)
            else: 
                info = string
        elif input_type is unicode_type:
            info = string
        elif input_type is int or input_type is float:
            if sys.version < '3':
                info = unicode(string)
            else:
                info = str(string)
        return info

    def _sanitize_data(self, data):
        ret = []
        for item in data:
            ret.append((self._sanitize_string(item[0]), item[1]))
        return ret

    def graph(self, label, data, sort=0, with_value=True):
        """function generating the graph
        
        :param string label: the label of the graph
        :param iterable data: the data (list of tuple (info, value))
                info must be "castable" to a unicode string
                value must be an int or a float
        :param int sort: flag sorted
                0: not sorted (same order as given) (default)
                1: increasing order
                2: decreasing order
        :param boolean with_value: flag printing value
                True: print the numeric value (default)
                False: don't print the numeric value
        :rtype: a list of strings (each lines)

        """
        result = []
        san_data = self._sanitize_data(data)
        san_label = self._sanitize_string(label)

        if sort == 1:
            san_data = sorted(san_data, key=lambda value: value[1], reverse=False)
        elif sort == 2:
            san_data = sorted(san_data, key=lambda value: value[1], reverse=True)

        all_max = self._get_maximum(san_data)
        
        real_line_length = max(self.line_length, len(label))
        
        min_line_length = self.min_graph_length +\
                2 * self.separator_length +\
                all_max['value_max_length'] +\
                all_max['info_max_length']

        if min_line_length < real_line_length:
            #calcul of where to start info
            start_info = self.line_length -\
                    all_max['info_max_length']
            #calcul of where to start value
            start_value = start_info -\
                    self.separator_length -\
                    all_max['value_max_length']
            #calcul of where to end graph
            graph_length = start_value -\
                    self.separator_length
        else:
            #calcul of where to start value
            start_value = self.min_graph_length +\
                    self.separator_length
            #calcul of where to start info
            start_info = start_value +\
                    all_max['value_max_length'] +\
                    self.separator_length
            #calcul of where to end graph
            graph_length = self.min_graph_length
            #calcul of the real line length
            real_line_length = min_line_length

        result.append(san_label)
        result.append(self._u('#')* real_line_length)
        

        for item in san_data:
            info = item[0]
            value = item[1]

            graph_string = self._gen_graph_string(
                    value, 
                    all_max['max_value'], 
                    graph_length,
                    start_value
                    )

            value_string = self._gen_value_string(
                    value,
                    start_value,
                    start_info
                    )

            info_string = self._gen_info_string(
                    info,
                    start_info,
                    real_line_length
                    )
            new_line = graph_string + value_string + info_string
            result.append(new_line)

        return result

if __name__ == '__main__':
    test = [('long_label', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
    graph = Pyasciigraph()
    for line in  graph.graph('test print', test):
        print(line)
