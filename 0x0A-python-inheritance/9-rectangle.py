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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the Ractangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() & str() repre of the Rectangle."""
        rect = "[" + str(self.__class__.__name__) + "]"
        rect += str(self.__width) + "/" + str(self.__height)
        return (rect)
