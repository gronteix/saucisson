#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="saucisson",
    version="0.1",
    description="Slice up your images",
    author="Gustave Ronteix",
    author_email="gronteix@pasteur.fr",
    url="https://github.com/gronteix/saucisson",
    install_requires=[
        "numpy",
        "math"
    ],
    packages = ['saucisson']
)
