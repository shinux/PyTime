#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

import pytime

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytime',
    version=pytime.__version__,
    description='A easy-use module to operate datetime by string',
    long_description=long_description,
    url='https://github.com/shinux/PyTime',
    author='Sinux',
    author_email='nsinux@gmail.com',
    license='MIT',
    keywords='datetime time datetime timeparser',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'': ['README.md']},
    tests_require=['coverage'],
    extras_require={
        'coveralls': ['coveralls']
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
