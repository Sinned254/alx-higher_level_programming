#!/usr/bin/python3
"""Module contains the ``Square`` class with a private instance attribute 
'size'
"""


class Square:
    """class Square"""

    def __init__(self, size):
        """ method for class square

        Args:
            size (int): size of Square.

        """
        self.__size = size
