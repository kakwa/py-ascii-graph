py-ascii-graph
==============

A simple python lib to print data as ascii histograms

.. image:: https://secure.travis-ci.org/kakwa/py-ascii-graph.png?branch=master
        :target: http://travis-ci.org/kakwa/py-ascii-graph
        :alt: Travis CI

.. image:: https://pypip.in/d/ascii_graph/badge.png
    :target: https://pypi.python.org/pypi/ascii_graph
    :alt: Number of PyPI downloads

License
=======

py-ascii-graph is released under the MIT License.

Description
===========

py-ascii-graph is a simple python library to build ascii histograms. 
Just give it a label and a list of tuples (description, value) 
and it will automaticaly creates a nice histogram, 
with all the stuff aligned and fitting in a fixed width line (if possible).

py-asciigraph although comes with a command line utility.

Examples
========

code:

.. sourcecode:: python

    from ascii_graph import Pyasciigraph

    test = [('long_label', 423), ('sl', 1234), ('line3', 531), ('line4', 200), ('line5', 834)]
    graph = Pyasciigraph()
    for line in  graph.graph('test print', test):
        print(line)

result:

.. sourcecode:: none

    test print
    ###############################################################################
    ████████████████████                                            423  long_label
    █████████████████████████████████████████████████████████████  1234  sl        
    ██████████████████████████                                      531  line3     
    █████████                                                       200  line4     
    █████████████████████████████████████████                       834  line5

command line:

.. sourcecode:: bash

    $ asciigraph -h
    Usage: asciigraph [-l <label>] [-f file] [-s inc|dec] [-w <number of char>] [-m <min len of char>]

    examples:
        printf 'label1:10\nlabel2:100\n' | asciigraph -l 'my graph'
        printf 'l1:10\nl2:100\n' > ./mf; asciigraph -l 'my graph' -f ./mf
        asciigraph -l 'my graph' -f mf -s inc
        asciigraph -l 'my graph' -f mf -s dec -w 60 -m 10


    Options:
        -h, --help            show this help message and exit
        -f FILE, --file=FILE  import data from FILE (one data per line,
                        format: <label>:<value>)
        -s SORT, --sort=SORT  sort type: inc (increasing) or dec (decreasing)
        -l LAB, --label=LAB   label of the graph
        -w WIDTH, --width=WIDTH
                              width of the graph
        -m LEN, --min_graph=LEN
                              minimum length of the graph bar

    $ printf "ced:1000\nasd:123\nyu:890\n" | asciigraph -l test -s dec
    test
    ###############################################################################
    ██████████████████████████████████████████████████████████████████  1000.0  ced
    ██████████████████████████████████████████████████████████           890.0  yu 
    ████████                                                             123.0  asd


See the examples/ directory for more examples.

Installation
============

.. sourcecode:: bash 

    $ pip install ascii_graph

or

.. sourcecode:: bash

    $ easy_install ascii_graph


.. image:: https://d2weczhvl823v0.cloudfront.net/kakwa/py-ascii-graph/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

