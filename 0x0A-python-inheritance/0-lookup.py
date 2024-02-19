#!/usr/bin/python3

"""Defines an object attributes lookup function."""


def lookup(obj):

    """Return the list of available attributes and methods."""
    return (dir(obj))
