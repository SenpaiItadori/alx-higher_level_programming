#!/usr/bin/python3

"""Define a class Square"""

class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
        size (int): the size of a square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square current"""
        return (self.__size)
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the area of the current square"""
        return (self.__size * self.__size)
