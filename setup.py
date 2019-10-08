#!/usr/bin/env python

from distutils.core import setup
from os.path import abspath, dirname, join

from setuptools import find_packages

with open(
    join(dirname(abspath(__file__)), "timeout_routines", "version.py")
) as version_file:
    exec(compile(version_file.read(), "version.py", "exec"))

setup(
    name="timeout_routines",
    version=version,  # noqa
    author="Eric Berquist",
    author_email="berquist@isi.edu",
    description="A short description of the project",
    url="https://github.com/berquist/timeout_routines",
    packages=[],
    # 3.6 and up, but not Python 4
    python_requires="~=3.6",
    install_requires=[],
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
