#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Method checks if object is instances of a class

    Returns: True if is instance otherwise False

    Args:
        abj: object
        a_class: class name
    """
    return type(obj) == a_class
