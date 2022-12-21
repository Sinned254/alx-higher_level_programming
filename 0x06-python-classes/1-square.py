#!/usr/bin/python3
"""Module containing the ``Square`` class with a private instance attribute
``size``.
"""

class Square:
    """Square class."""

    def __init__(self, size):
        """__init__method for Square.


        Args:
            size (int): size of Square.

        """
        self.__size = size
