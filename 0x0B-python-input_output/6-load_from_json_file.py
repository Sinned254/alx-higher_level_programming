#!/usr/bin/python3
"""Module contains funtion ``load_from_json_file``
"""
import json


def load_from_json_file(filename):
    """Funtion creates an object from JSON file
    Args:
        filename: file anme fo tthe file used 
    Returns: nothing
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
