#!/usr/bin/python3
"""Defines a class rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The identity of the Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        sef.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the width"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the width"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__x = value

    @property
    def y(self):
        """set/get the width"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using the '#' character."""
