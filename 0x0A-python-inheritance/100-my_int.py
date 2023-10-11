#!/usr/bin/python3

"""Defines a class MyInt that inherits from int"""



class MyInt(int):
    """Represents invert int operators == and !=."""

    def __eq__(self, value):
        """change == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """change != operator with == behavior"""
        return self.real == value
