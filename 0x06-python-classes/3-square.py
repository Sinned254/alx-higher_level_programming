#!/usr/bin/python3i
"""Module containing the ``Square`` class with a private instance attribute
``size``.
"""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """__init__method that sets the size of square.

        Args:
            size (int): size of Square

        Raises:
            TypeError: if `size` is not an integer.
            ValueError: if `size` is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Gets the are of a square.

        Returns:
            Area of a square

        """
        return self.__size * self.__size
