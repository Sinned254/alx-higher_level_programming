#!/usr/bin/python3
""" Module has definatinion of class Rectangle
"""


class Rectangle:
    """Class Rectangle
    Attributes:
        number_of_instances (int)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width(int):
            height(int):
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width: returns width of rectangele

        Args:
            width (int): width in int
        Returns:
            wiidth
        Raises:
            TypeError: if width is not an ant int
            Valueerror: if width is less than o
        """
        return self.__width

    @property
    def height(self):
        """height: returns height
        Args:
            heigth (int): integer height of rectangle
        Returns:
            height of rectanle
        raises:
            TypeError: of height is not int
            valueError: of heigt is less than 0
        """
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """string rep # of rectangle.
        Returns:
            string rep of rectangle
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        for r in range(self.height - 1):
            for c in range(self.width):
                string += '#'
            string += '\n'
        string += '#' * self.width
        return string

    def __repr__(self):
        """String rep of rectangle object"""
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """Delete Method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Returns the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the pwerimeter of arectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
