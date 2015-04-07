from ascii_graph import Pyasciigraph

test = [('long_label', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
graph = Pyasciigraph()
for line in graph.graph('test 1', test):
    print(line)

#take also anything castable to utf-8
test = [(1, 423), (2, 1234), (3, 531), ('line4', 200), ('line5', 834)]
for line in graph.graph('test 2', test):
    print(line)

#example of sort
test.sort(reverse=False, key=lambda tup: tup[1] )
for line in graph.graph('test 2', test):
    print(line)

#example of reverse sort
test.sort(reverse=True, key=lambda tup: tup[1] )
for line in graph.graph('test 2', test):
    print(line)
