#!/usr/bin/env python

from distutils.core import setup

with open('README.txt') as file:
    long_description = file.read()

setup(name='isbnutils',
      version='1.0',
      description='ISBN validation and conversion utilities',
      long_description = long_description,
      author='Darren J Wilkinson',
      maintainer='Jyotirmoy Bhattacharya',
      maintainer_email='jyotirmoy@jyotirmoy.net',
      license = 'GPL',
      url = 'https://github.com/jmoy/isbnutils',
      download_url = 'https://github.com/downloads/jmoy/isbnutils/isbnutils-1.0.zip',
      py_modules=['isbnutils'],
     )
