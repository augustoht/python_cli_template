# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('{{cookiecutter.package_name}}/{{cookiecutter.package_name}}.py').read(), re.M).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="cmdline-{{cookiecutter.package_name}}",
    packages=["{{cookiecutter.package_name}}"],
    entry_points={
        "console_scripts": ['{{cookiecutter.package_name}}={{cookiecutter.package_name}}.{{cookiecutter.package_name}}:main']
    },
    version=version,
    description="Python command line application bare bones template.",
    long_description=long_descr,
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="{{cookiecutter.package_url}}",
)
