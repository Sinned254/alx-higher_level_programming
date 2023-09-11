#!/usr/bin/python3
"""Module comatind ``is_same_class`` function
"""


def is_same_class(obj, a_class):
    """ Method checks if object is instances of a class

    Returns: True if is instance otherwise False

    Args:
        abj: object
        a_class: class name
    """
    if type(obj) == a_class:
        return True
    else:
        return False
