#!/usr/bin/python3
"""Define a class Rectangle"""

class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set/Get the wiidth of a Rectangle"""
        return (self.__width)
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/Get the width of the Rectangle"""
        return (self.__height)
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
