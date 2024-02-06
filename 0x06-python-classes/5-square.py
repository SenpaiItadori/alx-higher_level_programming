#!/usr/bin/python3

"""Define a class square"""

class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of a square"""
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
        """Return the current area of a Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the currebnt square with #"""
        side = self.__size
        if side == 0:
            print("")
        for i in range(side):
            for j in range(side):
                print("#",end="")
            print("")
