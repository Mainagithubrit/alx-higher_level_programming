#!/usr/bin/python3

"""Defines a class Base"""


class Base:
    """This is a representation of  the Base for all other classes in 0x0C.

    Private attributes:
        __nb__object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects