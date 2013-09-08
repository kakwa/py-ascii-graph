#!/usr/bin/env python
import os
import sys
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

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            #import here, cause outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.test_args)
            sys.exit(errno)

except ImportError:

    from distutils.core import setup
    PyTest = lambda x: x


setup(
    name = 'ascii_graph',
    version = '0.2.0',
    author = 'Pierre-Francois Carpentier',
    author_email = 'carpentier.pf@gmail.com',
    packages = ['ascii_graph'],
    scripts = ['scripts/asciigraph'],
    url = 'https://github.com/kakwa/ascii_graph',
    license = license,
    description = 'A simple python lib to print data as ascii histograms.',
    long_description = description,
    install_requires = [],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)

