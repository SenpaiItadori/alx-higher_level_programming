#!/usr/bin/python3

"""Defines a Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a new Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square
        Args:
            size (int): The size of the square
            x (int): The position to be printed on the x-axis
            y (int): The position to be printed on the y-axis
            id: the identity of the new square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str/Print format of the Square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
