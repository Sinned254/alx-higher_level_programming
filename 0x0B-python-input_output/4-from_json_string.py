#!/usr/bin/python3
"""Module contains from_json_string funtion
"""
import json


def from_json_string(my_str):
    """ Funtion returns an object represented by JSON string
    Args:
        my_str: JSON string to be deserialized
    Returns: deserialzed string in pythod data structure
    """
    new_obj = json.loads(my_str)
    return new_obj
