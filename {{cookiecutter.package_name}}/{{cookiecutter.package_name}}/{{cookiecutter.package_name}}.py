# -*- coding: utf-8 -*-

"""{{cookiecutter.package_name}}.{{cookiecutter.package_name}}: provides entry point main()."""

import sys

__version__ = "0.2.0"


def main():
    """Docstring in public function."""
    print("Executing {{cookiecutter.package_name}} version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
