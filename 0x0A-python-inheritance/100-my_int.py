#!/usr/bin/python3

"""Defines a class MyInt that takes from int."""


class MyInt(int):
    """Inverts == and !=."""

    def __eq__(self, value):
        """Makes == become !=."""
        return (self.real != value)

    def __ne__(self, value):
        """makes != become ==."""
        return (self.real == value)
