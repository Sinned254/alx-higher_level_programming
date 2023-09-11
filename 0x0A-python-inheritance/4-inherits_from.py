#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ check if the object is an instance of a class that
    inherited from specified class 

    Returns: True if it does otherwise false

    Args:
        abj: object name
        class: class name
    """
    if obj.__class__ is not a_class:
        for cls in obj.__class__.mro():
            if cls == a_class:
                return True

    return False
