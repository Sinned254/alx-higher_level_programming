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

    def to_json(self):
        """ Returns a representation of a dictionary to sa student
        """
        student_json = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return student_json
