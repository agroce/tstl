#-*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='tstl',
    version='1.2.24',
    description='Template scripting testing language (TSTL)',
    long_description=open('README.md').read(),
    packages=['tstl',],
    include_package_data = True,
    package_data = {
        'tstl': ['static/boilerplate', 'static/boilerplate_cov'],
    },
    license='MIT',
    entry_points="""
    [console_scripts]
    tstl = tstl.harnessmaker:main
    tstl_rt = tstl.randomtester:main
    tstl_standalone = tstl.standalone:main
    tstl_replay = tstl.replay:main
    tstl_reduce = tstl.reduce:main
    tstl_smallcheck = tstl.smallcheck:main
    tstl_generalize = tstl.generalize:main
    tstl_regress = tstl.runregressions:main
    tstl_markov = tstl.markov:main
    tstl_directedswarm = tstl.directedswarm:main
    tstl_graph = tstl.graph:main
    tstl_afl = tstl.tstl_afl:main
    tstl_aflcorpus = tstl.makecorpus:main
    tstl_toafl = tstl.tocorpus:main
    tstl_fromafl = tstl.fromafl:main
    tstl_triage = tstl.triage:main
    tstl_afl_fuzz = tstl.tstl_afl_fuzz:main
    tstl_calibrate = tstl.calibrate:main
    """,
    keywords='testing tstl',
    test_suite='nose.collector',
    tests_require=['nose'],
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
