#!/usr/bin/python3
"""Defines a rectangle class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeomtry """

    def __init__(self, width, height):
        """Initializes a rectangle
        Args:
            width (int): The width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of a Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string represention of Rectangle object """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
