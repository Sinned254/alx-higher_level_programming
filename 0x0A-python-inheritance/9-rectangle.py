#!/usr/bin/python3
"""Contains ``BaseGeometry`` with method area
"""


class BaseGeometry:
    """class ``BaseGeometry`` defination"""
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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class ``rectangle`` inherits from ``BaseGeometry
    """
    def __init__(self, width, height):
        """Innitialize class ``Recrtangl``"""
        self.__width = 0  # Initialize width as 0
        self.__height = 0  # Initialize height as 0
        self.integer_validator("width", width)  # Validate and set width
        self.integer_validator("height", height)  # Validate and set height
        self.__width = width
        self.__height = height

    def area(self):
        """Method finds the are of a rectrangele"""
        return self.__width * self.__height

    def __str__(self):
        """Prints rectangle string"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return self.__str__()
