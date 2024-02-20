#!/usr/bin/python3

"""Defines a function that print the reads from the read file to stdout."""


def read_file(filename=""):
    """Print the reads of a txt file to stdout."""
    with open(filename, encoding="utf-8") as text:
        text.seek(0)
        print("{:s}".format(text.read()), end="")
