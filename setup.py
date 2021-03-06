#!/usr/bin/env python
# Author:  mozman
# Purpose: setup
# Created: 10.03.2011
# License: MIT License


import os
from setuptools import setup

VERSION = "0.8.2"  # also update VERSION in __init__.py
AUTHOR_NAME = 'Manfred Moitzi'
AUTHOR_EMAIL = 'mozman@gmx.at'


def read(fname, until=""):
    def read_until(lines):
        last_index = -1
        for index, line in enumerate(lines):
            if line.startswith(until):
                last_index = index
                break
        return "".join(lines[:last_index])
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as f:
            return read_until(f.readlines()) if until else f.read()
    except IOError:
        return "File '%s' not found.\n" % fname

setup(
    name='ezdxf',
    version=VERSION,
    description='A Python package to create/manipulate DXF drawings.',
    author=AUTHOR_NAME,
    url='http://github.com/mozman/ezdxf.git',
    download_url='http://github.com/mozman/ezdxf/releases',
    author_email=AUTHOR_EMAIL,
    packages=['ezdxf',
              'ezdxf.legacy',
              'ezdxf.modern',
              'ezdxf.lldxf',
              'ezdxf.pp',
              'ezdxf.sections',
              'ezdxf.templates',
              'ezdxf.tools',
              ],
    package_data={'ezdxf': ['templates/*.dxf',
                            'pp/dxf2html.html',
                            'pp/dxf2html.js',
                            'pp/dxf2html.css']},
    provides=['ezdxf'],
    install_requires=['pyparsing>=2.0.1'],
    keywords=['DXF', 'CAD'],
    long_description=read('README.rst')+read('NEWS.rst', until='Version 0.6.5'),
    platforms="OS Independent",
    license="MIT License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
