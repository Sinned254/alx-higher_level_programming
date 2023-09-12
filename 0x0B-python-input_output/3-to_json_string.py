#!/usr/bin/python3
"""Module contains funtion to_json_string funtion
"""
import json


def to_json_string(my_obj):
    """Funtion returns the JSON representaion of an object
    Args: 
        my_obj: object
    Returns: JSON representation of an object
    """
    json_s = json.dumps(my_obj)
    return json_s
