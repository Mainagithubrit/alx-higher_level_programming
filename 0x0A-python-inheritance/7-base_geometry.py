#!/usr/bin/python3

"""Defines a class BaseGeometry"""


class BaseGeometry:
    """a class that raises an exception error"""

    def area(self):
        """A function that raises an Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates a parameter as an integer.

        Args:
            name (str): name of parameter
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
