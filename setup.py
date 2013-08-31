#!/usr/bin/env python
import os
from distutils.core import setup

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place.
try:
   import pypandoc
   description = pypandoc.convert('README.md', 'rst')
except (OSError, IOError, ImportError):
   description = ''

try:
   license = open('LICENSE').read()
except IOError:
   license = 'MIT'

setup(
   name = 'ascii_graph',
   version = '0.1.0',
   author = 'Pierre-Francois Carpentier',
   author_email = 'carpentier.pf@gmail.com',
   packages = ['ascii_graph'],
   scripts = [],
   url = 'https://github.com/kakwa/ascii_graph',
   license = license,
   description = 'A simple python lib to print data as ascii histograms.',
   long_description = description,
   install_requires = [],
)

