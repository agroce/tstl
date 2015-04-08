#-*- coding:utf-8 -*-

from setuptools import setup, find_packages
import sys, os

setup(
    name='tstl',
    version='0.1',
    description='Template scripting testing language (TSTL) based on research by by Dr. Alex Groce & Jervis Pinto. EECS, Oregon State University',
    long_description=open('README.md').read(),
    packages=['src',],
    include_package_data = True,
    package_data = {
        'src': ['static/boilerplate.py', 'static/boilerplate_cov.py'],
    },
    license='MIT',
    entry_points="""
    [console_scripts]
    tstl = src.harnessmaker:main
    """,
    keywords='testing tstl',
    classifiers=[
      "Intended Audience :: Developers",
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 2",
      ],
    url='https://github.com/agroce/tstl',
)
