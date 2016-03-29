#!/usr/bin/env python
import os
import sys
from distutils.core import setup


try:
    f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
    description = f.read()
    f.close()
except IOError:
    description = 'ascii_graph'
    
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
    version = '1.1.4',
    author = 'Pierre-Francois Carpentier',
    author_email = 'carpentier.pf@gmail.com',
    packages = ['ascii_graph'],
    scripts = ['scripts/asciigraph'],
    url = 'https://github.com/kakwa/py-ascii-graph',
    license = license,
    description = 'A simple python lib to print data as ascii histograms.',
    long_description = description,
    install_requires = [],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: System Administrators',
	'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5']
)
