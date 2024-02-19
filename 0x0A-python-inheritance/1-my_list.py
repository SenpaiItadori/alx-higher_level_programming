#!/usr/bin/python3

"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Inherites the sorted printing from the builtin list class."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
