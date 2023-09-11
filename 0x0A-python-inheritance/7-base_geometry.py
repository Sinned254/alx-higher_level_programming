#!/usr/bin/python3
"""Contains ``BaseGeometry`` with method area
"""
class BaseGeometry:
    def area(self):
        """raise exception are not implemeted
        """
        raise Exception("area() is not implemeted")

    def integer_validator(self, name, value):
        """Validates value if int
        Args: 
            value: value to validtae
            Name: name of the Value
        Raises:
            Typerror: if value not int
            ValueError: if value less than 1
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
