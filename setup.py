#-*- coding:utf-8 -*-

from setuptools import setup, find_packages
import sys, os

setup(
    name='tstl',
    version='1.2.12',
    description='Template scripting testing language (TSTL)',
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
    tstl_rt = src.randomtester:main
    tstl_standalone = src.standalone:main
    tstl_replay = src.replay:main
    tstl_reduce = src.reduce:main
    tstl_generalize = src.generalize:main
    tstl_regress = src.runregressions:main
    tstl_markov = src.markov:main
    tstl_graph = src.graph:main
    tstl_afl = src.tstl_afl:main
    tstl_aflcorpus = src.makecorpus:main
    tstl_toafl = src.tocorpus:main
    tstl_fromafl = src.fromafl:main
    tstl_triage = src.triage:main
    tstl_afl_fuzz = src.tstl_afl_fuzz:main
    tstl_calibrate = src.calibrate:main
    """,
    keywords='testing tstl',
    classifiers=[
      "Intended Audience :: Developers",
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 3",
      ],
    install_requires=[
      'coverage',
    ],
    url='https://github.com/agroce/tstl',
)
