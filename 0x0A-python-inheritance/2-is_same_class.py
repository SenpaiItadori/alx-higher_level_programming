#!/usr/bin/python3

"""Defines a function that sees if an object is an instnce of a class."""


def is_same_class(obj, a_class):
    """Return True is the objects is an exact instance of a_class."""

    if type(obj) == a_class:
        return (True)
    else:
        return (False)
