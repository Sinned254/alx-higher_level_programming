#!/usr/bin/python3
""" Module containing the ``lookup`` funtion defination
"""


def lookup(obj):
    """Returns the list of availabe attributes and methods of an object
    Args:
        obj(object): object
    """
    return dir(obj)
