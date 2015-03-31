#!/bin/env python2

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

test = [ ('testval0', 600), ('testval1', 400, bcolors.Red), ('testval2', 300, bcolors.Green), ('testval3', 200, bcolors.Yellow), ('testval2', 100, bcolors.Cyan), ('testval3', 50, bcolors.Blue) ]
graph = Pyasciigraph()
for line in graph.graph('test graph', test):
    print(line)

exit(0)
