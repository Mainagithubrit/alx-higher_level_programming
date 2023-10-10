#!/usr/bin/python3

"""Defines an inheritance from List class"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
