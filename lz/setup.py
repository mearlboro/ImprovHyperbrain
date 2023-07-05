# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:31:00 2019

@author: hardi
"""

from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize('lz76.pyx'))