#!/usr/bin/python3
"""Defines a class that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): the size of the new square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ print self method """
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
