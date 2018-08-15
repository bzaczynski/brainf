#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2018 Bartosz Zaczynski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import re

from setuptools import setup, find_packages


def version():
    """Return package __version__."""
    with open(os.path.join('src', 'brainf', '__init__.py')) as fp:
        match = re.search("__version__ = '([^']+)'", fp.read())
        if match:
            return match.group(1)


def readme():
    """Return the contents of readme file."""
    with open('README.md', encoding='utf-8') as fp:
        return fp.read()


def requirements(filename='requirements.txt'):
    """Return a list of requirements."""
    with open(filename) as fp:
        return fp.read().splitlines()


setup(
    name='brainf',
    version=version(),
    license='MIT',
    description='Brainfuck interpreter',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Bartosz Zaczyński',
    author_email='bartosz.zaczynski@gmail.com',
    url='https://github.com/bzaczynski/brainf',
    download_url='git@github.com:bzaczynski/brainf.git',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    dependency_links=[],
    install_requires=requirements(),
    test_require=requirements('requirements-test.txt'),
    test_suite='tests',
    scripts=[
        'bin/brainfuck.py'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Interpreters',
    ],
    keywords='brainfuck interpreter brainf'
    #include_package_data=True,
    #package_data={},
    #zip_safe=True
)
