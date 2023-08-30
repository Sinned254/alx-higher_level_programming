#!/usr/bin/python3
"""Module contains the ``Square`` class with a private instance
attribute 'size'
"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """ method for class square

        Args:
            size (int): size of Square.

        Raises:
            TypeError: if `size` is not an integer.
            ValueError: if `size` is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
