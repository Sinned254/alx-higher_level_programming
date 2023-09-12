#!/usr/bin/python3
"""Module conatins funtion add_attribute
"""


def add_attribute(obj, attr_name, attr_value):
    """adds attribute to object if it's posssible"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
