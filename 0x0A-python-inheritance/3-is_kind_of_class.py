#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Method checks if object insnance of class or subclass

    Returns: True if it is otherwise False

    Args:
        obj: object name
        class: class name
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
