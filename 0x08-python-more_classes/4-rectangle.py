#!/usr/bin/python3
"""Define a class Rectangle"""

class Rectangle:
    """Represent a Rectangle"""

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
        """Get/Set the width of the Rectangle"""
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
        """Get/Set the height of a Rectangle"""
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
        """Return the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the length right round the Rectangle"""
        perr = 0
        if self.__width != 0 or self.__height != 0:
            perr = (self.__width + self.__height) * 2
        return (perr)

    def __str__(self):
        """Return the prentable rep of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        new = []
        for i in range(self.__height):
            [new.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                new.append("\n")
        return ("".join(new))

    def __repr__(self):
        """Return the string rep of a Rectangle"""
        new = "Rectangle(" + str(self.__width)
        new += ", " + str(self.__height) + ")"
        return (new)
