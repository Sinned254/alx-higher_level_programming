#!/usr/bin/python3
"""Module contains funtion ``save_to_json_file``
"""
import json


def save_to_json_file(my_obj, filename):
    """Funtion writes an object to text file using JSON representation
    Args:
        my_obj: object to write
        filename: file name to write text 
    Returns: nothing
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
