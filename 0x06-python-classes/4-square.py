#!/usr/bin/python3
"""Module containing the ``Square`` class with a private instance attribute
``size``.
"""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """__init__method that sets the size of square.

        Args:
            size (int): size of Square

        """
        self.size = size

    def area(self):
        """Gets the area of a square

        Returns:
            Area of a square

        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method taht set the size of a square.

        Args:
            value (int): size of square

        Raises:
            TypeError: if `value' is not an integer.
            ValueError: if `value' is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
