# -*- coding: utf-8 -*-


"""{{cookiecutter.package_name}}.{{cookiecutter.package_name}}: provides entry point main()."""


__version__ = "0.2.0"


import sys
from .stuff import Stuff


def main():
    print("Executing {{cookiecutter.package_name}} version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))


class Boo(Stuff):
    pass