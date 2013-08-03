#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="ctypeslib2",
    version="2.3.3",
    description="ctypeslib2 - FFI toolkit, relies on clang",
    long_description=open("README").read(),
    author="Loic Jaquemet",
    author_email="loic.jaquemet+python@gmail.com",
    classifiers = [
    'Development Status :: 4 - Beta',
##    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url="https://github.com/trolldbois/ctypeslib",
    download_url="https://github.com/trolldbois/ctypeslib/releases",
    license="License :: OSI Approved :: MIT License",
    packages = ['ctypeslib',
                'ctypeslib.codegen',
                'ctypeslib.contrib',
                'ctypeslib.util',
                'ctypeslib.test'],
    scripts = ['scripts/clang2py'],
    install_requires = ["clang"],
    test_suite= "test.alltests",
)
