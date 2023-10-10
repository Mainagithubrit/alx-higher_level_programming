#!/usr/bin/python3

"""Defines a class and inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """Returns True or false if an object instance inherits from a class"""
    return (isinstance(obj, a_class))
