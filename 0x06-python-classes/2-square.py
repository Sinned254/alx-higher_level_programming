#!/usr/bin/python3
"""Module containing the ``Square`` class with a private instance attribute
``size``.
"""


class Square:
    """``Square`` class.
    """

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
            raise ValueError("size must be >= 0")
        self.__size = size
