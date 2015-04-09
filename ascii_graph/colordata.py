def vcolor(data, pattern):
    """ Color a graph line by line

    :param data: the data
    :type data: list of tuples (info, value)
    :param pattern: list of colors, this list defines
      the pattern to color each line of the graph.
    :type pattern: list of 'colors' (str)
    :return: the colored graph
    :rtype: list of arrays (<info>, <value>, <color>)
    """
    ret=[]
    l=len(pattern)
    c=0
    for info,value in data:
        ret.append((info, value, pattern[c]))
        c = (c + 1) % l 
    return ret

