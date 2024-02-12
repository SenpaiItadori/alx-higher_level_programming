#!/usr/bin/python3
"""Define a class Rectangle"""

class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the rectangle"""
        return (self.__width)
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/Set the height of a rectangle"""
        return (self.__height)
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Find the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the length right round the shape"""
        perr = 0
        if self.__width != 0 or self.__height != 0:
            perr = (self.__width + self.__height) * 2
        return (perr)
