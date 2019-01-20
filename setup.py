# -*- coding: utf-8 -*-
import os, shutil
from distutils.command.clean import clean as Clean

from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in frappe/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

with open('google_api_integration/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
    name='google_api_integration',
	version=version,
	description='Google API Integration',
	author='Pau Rosello',
	author_email='pau@servipro.eu',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
	dependency_links=[]
)