#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        number_of_square = value * graph_length / max_value
        number_of_space = start_value - number_of_square
        return u'█' * number_of_square + u' ' * number_of_space

    def _gen_info_string(self, info, start_info,line_length):
        number_of_space = (line_length - start_info - len(info))
        return info + u' ' * number_of_space

    def _gen_value_string(self, value, start_value, start_info):
        number_space = start_info -\
                start_value -\
                len(unicode(value)) -\
                self.separator_length

        return  u' ' * number_space +\
                unicode(value) +\
                u' ' * self.separator_length

    def graph(self, label, data, sort=0, with_value=True):
        """function generating the graph
        
        :param string label: the label of the graph
        :param iterable data: the data (list of tuple (info, value))
        :param int sort: flag sorted
                0: not sorted (same order as given) (default)
                1: ascending order
                2: discendinf order
        :param boolean with_value: flag printing value
                True: print the numeric value (default)
                False: don't print the numeric value
        :rtype: a list of strings (each lines)

        """
        result = []
        all_max = self._get_maximum(data)
        
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

        result.append(label)
        result.append(u'#' * real_line_length)
        

        for item in data:
            graph_string = self._gen_graph_string(
                    item[1], 
                    all_max['max_value'], 
                    graph_length,
                    start_value
                    )

            value_string = self._gen_value_string(
                    item[1],
                    start_value,
                    start_info
                    )

            info_string = self._gen_info_string(
                    item[0],
                    start_info,
                    real_line_length
                    )
            new_line = graph_string + value_string + info_string
            result.append(new_line)

        return result

if __name__ == '__main__':
    test=[('long_label', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
    graph=Pyasciigraph()
    for line in  graph.graph('test print', test):
        print line
