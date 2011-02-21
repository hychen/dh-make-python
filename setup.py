#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Copyright © 2011 Hsin Yi Chen
from distutils.core import setup

setup(
    name = 'dh-make-python',
    version = open('VERSION.txt').read().strip(),
    description = 'helper for creating Debian Package from Python modules',
    long_description=open('README.txt').read(),
    author = 'Hsin-Yi Chen 陳信屹 (hychen)',
    author_email = 'ossug.hychen@gmail.com',
    license = 'BSD-2-clause License',
    packages=['dh_make_python'],
    scripts=['bin/dh_make_python']
)
