#!/usr/bin/python3
"""Defines a locked class"""

class LockedClass:
    """
    Only allows the first name attribute
    """

    __slots__ = ["first_name"]
