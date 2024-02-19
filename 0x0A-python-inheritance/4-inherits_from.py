#!/usr/bin/python3

"""Defines function that checks if an instance of a class is inherited."""


def inherits_from(obj, a_class):
    """Return True/False by check instance is inherited from a_class class."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
