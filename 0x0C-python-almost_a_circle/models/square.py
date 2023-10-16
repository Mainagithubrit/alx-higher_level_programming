#!/usr/bin/python3
"""Defines a Square that inherits from a Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a square

        Args:
            size (int): size of the square
            x (int): The x coordinate of the square
            y (int): The y coordinate of the square
            id (int): The identity of the of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square"""
        return self.width

    @size.setter
    def size(self):
        self.width = value
        self.height = value
