#!/usr/bin/python3

"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """Retutns true or false if an object is inherited from a class"""
    obj_class = obj.__class__

    if obj_class is a_class:
        return False
    return (issubclass(obj_class, a_class))
