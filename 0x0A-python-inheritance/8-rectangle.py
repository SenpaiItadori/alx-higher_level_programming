#!/usr/bin/python3

"""Defines a class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle."""

    def __init__(self, width, height):
        """Initialize a class Rectangle.

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
