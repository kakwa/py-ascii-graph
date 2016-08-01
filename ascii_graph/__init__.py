#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import collections
import copy


class Pyasciigraph:

    def __init__(self, line_length=79,
                 min_graph_length=50,
                 separator_length=2,
                 graphsymbol=None,
                 multivalue=True,
                 human_readable=None,
                 float_format='{0:.0f}'
                 ):
        """Constructor of Pyasciigraph

        :param line_length: the max number of char on a line
          if any line cannot be shorter,
          it will go over this limit.
          Default: 79
        :type line_length: int
        :param min_graph_length: the min number of char
          used by the graph itself.
          Default: 50
        :type min_graph_length: int
        :param separator_length: the length of field separator.
          Default: 2
        :type separator_length: int
        :param graphsymbol: the symbol used for the graph bar.
          Default: '█'
        :type graphsymbol: str or unicode (length one)
        :param multivalue: displays all the values if multivalued when True.
          displays only the max value if False
          Default: True
        :type multivalue: boolean
        :param human_readable: trigger human readable display (K, G, etc)
          Default: None (raw value display)

          * 'si' for power of 1000

          * 'cs' for power of 1024

          * any other value for raw value display)

        :type human_readable: string (si, cs, none)
        :param float_format: formatting of the float value
          Default: '{0:.0f}' (convert to integers).
          expample: '{:,.2f}' (2 decimals, '.' to separate decimal and int,
          ',' every three power of tens).
        """

        self.line_length = line_length
        self.separator_length = separator_length
        self.min_graph_length = min_graph_length
        self.float_format = float_format
        if graphsymbol is None:
            self.graphsymbol = self._u('█')
        else:
            self.graphsymbol = graphsymbol
        if len(self.graphsymbol) != 1:
            raise Exception('Bad graphsymbol length, must be 1',
                            len(self.graphsymbol))
        self.multivalue = multivalue
        self.hsymbols = [self._u(''), self._u('K'), self._u('M'),
                         self._u('G'), self._u('T'), self._u('P'),
                         self._u('E'), self._u('Z'), self._u('Y')]

        if human_readable == 'si':
            self.divider = 1000
        elif human_readable == 'cs':
            self.divider = 1024
        else:
            self.divider = None

    def _trans_hr(self, value):

        if self.divider is None:
            return self.float_format.format(value)
        vl = value
        for hs in self.hsymbols:
            new_val = vl / self.divider
            if new_val < 1:
                return self.float_format.format(vl) + hs
            else:
                vl = new_val
        return self.float_format.format(vl * self.divider) + hs

    @staticmethod
    def _u(x):
        if sys.version < '3':
            return x + ''.decode("utf-8")
        else:
            return x

    @staticmethod
    def _color_string(string, color):
        if color is None:
            return string
        else:
            return color + string + '\033[0m'

    def _get_maximum(self, data):
        all_max = {}
        all_max['value_max_length'] = 0
        all_max['info_max_length'] = 0
        all_max['max_value'] = 0

        for (info, value, color) in data:
            totalvalue_len = 0
            if isinstance(value, collections.Iterable):
                icount = 0
                maxvalue = 0
                for (ivalue, icolor) in value:
                    if ivalue > maxvalue:
                        maxvalue = ivalue
                    totalvalue_len += len("," + self._trans_hr(ivalue))

                if self.multivalue:
                    # remove one comma
                    totalvalue_len = totalvalue_len - 1
                else:
                    totalvalue_len = len(self._trans_hr(maxvalue))
            else:
                totalvalue_len = len(self._trans_hr(value))
                maxvalue = value

            if maxvalue > all_max['max_value']:
                all_max['max_value'] = maxvalue

            if len(info) > all_max['info_max_length']:
                all_max['info_max_length'] = len(info)

            if totalvalue_len > all_max['value_max_length']:
                all_max['value_max_length'] = totalvalue_len

        return all_max

    def _gen_graph_string(
            self, value, max_value, graph_length, start_value, color):
        def _gen_graph_string_part(
                value, max_value, graph_length, start_value, color, total_value, lastgraph):
            if max_value == 0:
                number_of_square = 0
            else:
                number_of_square = int(value * graph_length / max_value)
            if lastgraph:
                number_of_space = int(
                    start_value - (number_of_square + total_value))
            else:
                number_of_space = 0
            return (Pyasciigraph._color_string(self.graphsymbol * number_of_square + Pyasciigraph._u(' ') * number_of_space, color), number_of_square)

        if isinstance(value, collections.Iterable):
            accuvalue = 0
            totalstring = ""
            totalsquares = 0
            sortedvalue = copy.deepcopy(value)
            sortedvalue.sort(reverse=False, key=lambda tup: tup[0])
            for i in sortedvalue:
                ivalue = i[0]
                icolor = i[1]
                scaled_value = ivalue - accuvalue
                # Check if last item in list, if so then add spaces to the end
                # to align the value and label
                if i == sortedvalue[-1]:
                    (partstr, squares) = _gen_graph_string_part(
                        scaled_value, max_value, graph_length, start_value, icolor, totalsquares, True)
                    totalstring += partstr
                    totalsquares += squares
                else:
                    (partstr, squares) = _gen_graph_string_part(
                        scaled_value, max_value, graph_length, start_value, icolor, totalsquares, False)
                    totalstring += partstr
                    totalsquares += squares
                accuvalue += scaled_value
            return totalstring
        else:
            (partstr, squares) = _gen_graph_string_part(
                value, max_value, graph_length, start_value, color, 0, True)
            return partstr

    def _gen_info_string(self, info, start_info, line_length):
        number_of_space = (line_length - start_info - len(info))
        return info + Pyasciigraph._u(' ') * number_of_space

    def _gen_value_string(self, value, color, start_value, start_info):

        icount = 0
        if isinstance(value, collections.Iterable) and self.multivalue:
            for (ivalue, icolor) in value:
                if icount == 0:
                    # total_len is needed because the color characters count
                    # with the len() function even when they are not printed to
                    # the screen.
                    totalvalue_len = len(self._trans_hr(ivalue))
                    totalvalue = Pyasciigraph._color_string(
                        self._trans_hr(ivalue), icolor)
                else:
                    totalvalue_len += len("," + self._trans_hr(ivalue))
                    totalvalue += "," + \
                        Pyasciigraph._color_string(
                            self._trans_hr(ivalue),
                            icolor)
                icount += 1
        elif isinstance(value, collections.Iterable):
            max_value = 0
            color = None
            for (ivalue, icolor) in value:
                if ivalue > max_value:
                    max_value = ivalue
                    color = icolor
            totalvalue_len = len(self._trans_hr(max_value))
            totalvalue = Pyasciigraph._color_string(
                self._trans_hr(max_value), color)

        else:
            totalvalue_len = len(self._trans_hr(value))
            totalvalue = Pyasciigraph._color_string(
                self._trans_hr(value), color)

        number_space = start_info -\
            start_value -\
            totalvalue_len -\
            self.separator_length

        # This must not be negitive, this happens when the string length is
        # larger than the separator length
        if number_space < 0:
            number_space = 0

        return  ' ' * number_space + totalvalue +\
                ' ' * \
            ((start_info - start_value - totalvalue_len)
             - number_space)

    def _sanitize_string(self, string):
        # get the type of a unicode string
        unicode_type = type(Pyasciigraph._u('t'))
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

    def _sanitize_value(self, value):
        if isinstance(value, collections.Iterable):
            newcollection = []
            for i in value:
                if len(i) == 1:
                    newcollection.append((i[0], None))
                elif len(i) >= 2:
                    newcollection.append((i[0], i[1]))
            return newcollection
        else:
            return value

    def _sanitize_data(self, data):
        ret = []
        for item in data:
            if (len(item) == 2):
                if isinstance(item[1], collections.Iterable):
                    ret.append(
                        (self._sanitize_string(item[0]),
                         self._sanitize_value(item[1]),
                         None))
                else:
                    ret.append(
                        (self._sanitize_string(item[0]),
                         self._sanitize_value(item[1]),
                         None))
            if (len(item) == 3):
                ret.append(
                    (self._sanitize_string(item[0]),
                     self._sanitize_value(item[1]),
                     item[2]))
        return ret

    def graph(self, label=None, data=[]):
        """function generating the graph

        :param string label: the label of the graph
        :param iterable data: the data (list of tuple (info, value))
                info must be "castable" to a unicode string
                value must be an int or a float
        :rtype: a list of strings (each lines of the graph)

        """
        result = []
        san_data = self._sanitize_data(data)
        all_max = self._get_maximum(san_data)

        if not label is None:
            san_label = self._sanitize_string(label)
            label_len = len(san_label)
        else:
            label_len = 0

        real_line_length = max(self.line_length, label_len)

        min_line_length = self.min_graph_length +\
            2 * self.separator_length +\
            all_max['value_max_length'] +\
            all_max['info_max_length']

        if min_line_length < real_line_length:
            # calcul of where to start info
            start_info = self.line_length -\
                all_max['info_max_length']
            # calcul of where to start value
            start_value = start_info -\
                self.separator_length -\
                all_max['value_max_length']
            # calcul of where to end graph
            graph_length = start_value -\
                self.separator_length
        else:
            # calcul of where to start value
            start_value = self.min_graph_length +\
                self.separator_length
            # calcul of where to start info
            start_info = start_value +\
                all_max['value_max_length'] +\
                self.separator_length
            # calcul of where to end graph
            graph_length = start_value -\
                self.separator_length
            # calcul of the real line length
            real_line_length = min_line_length

        if not label is None:
            result.append(san_label)
            result.append(Pyasciigraph._u('#') * real_line_length)

        for info, value, color in san_data:

            graph_string = self._gen_graph_string(
                value,
                    all_max['max_value'],
                    graph_length,
                    start_value,
                    color
            )

            value_string = self._gen_value_string(
                value,
                    color,
                    start_value,
                    start_info,
            )

            info_string = self._gen_info_string(
                info,
                    start_info,
                    real_line_length
            )
            new_line = graph_string + value_string + info_string
            result.append(new_line)

        return result
