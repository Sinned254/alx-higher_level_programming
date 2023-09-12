#!/usr/bin/python3
"""Module contains class ``Student`` that define student
"""


class Student:
    """Studen class
    """
    def __init__(self, first_name, last_name, age):
        """initialize class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a representation of a dictionary to sa student
        """
        if attrs is None:
            student_json = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
            return student_json
        else:
            student_json = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_json[attr] = getattr(self, attr)
            return student_json

    def reload_from_json(self, json_data):
        """Replaces all attribute of the studen instance
        """
        for key, value in json_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
