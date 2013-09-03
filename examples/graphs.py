from ascii_graph import Pyasciigraph

test = [('long_label', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
graph = Pyasciigraph()
for line in graph.graph('test 1', test):
    print(line)

test = [(1, 423), (2, 1234), (3, 531), ('line4', 200), ('line5', 834)]
for line in graph.graph('test 2', test):
    print(line)
