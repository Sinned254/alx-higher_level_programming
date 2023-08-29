#!/usr/bin/python3
"""Module that contains the ``Square`` class definition.
"""


class Square:
    """Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """__init__method that sets the size and position of square.

        Args:
            size (int): size of Square
            position (tuple): position of a square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method sets position of Square.
        Args:
            value (tuple): tuple of two positive integers coodinate
        Raises:
            TypeError: if `value` is not a tuple of two
            positive integer coordinates

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive ints")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("positio must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of two integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints a # repesantation of square based on size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
