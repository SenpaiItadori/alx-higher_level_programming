#!/usr/bin/python3

"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represent a base geometry."""

    def area(self):
        """Raises an exception with error message."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.
        Args:
            name (string): Name of value.
            value (int): The size of the name specified.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
