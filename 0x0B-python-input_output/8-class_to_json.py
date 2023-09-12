#!/usr/bin/python3
"""Module containin ''class_to_json`` funtion
"""


def class_to_json(obj):
    """Return sserialization of an object
    """
    if isinstance(obj, (str, int, bool, type(None))):
        return obj
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    if hasattr(obj, '__dict__'):
        return class_to_json(obj.__dict__)
    return None
