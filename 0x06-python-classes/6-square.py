#!/usr/bin/python3

"""Define a class Square"""

class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size: The size of the square
            position: The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the current square"""
        return (self.__size)
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Get/set the current position of the current square"""
        return (self.__position)

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Return area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # char"""
        side = self.__size
        space = self.__position[0]
        pace = self.__position[1]

        if side == 0:
            print("")

        for a in range(pace):
            print("")
        for i in range(side):
            for k in range(space):
                print(" ", end="")
            for j in range(side):
                print("#",end="")
            print("")
