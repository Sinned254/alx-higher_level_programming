#!/usr/bin/python3
"""Modules contains class ``Rectangle`` which is a subclass of ``Base``
"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle defination
    Attributes
    ---------
    width: int
        width of a rectangle
    height: int
        Height of a Rectngle
    x: (int) x cordinate
    y: (int) y cordinate
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Innitialize ``rectangle``"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width property def"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property def"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property def"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter'"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property def"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """finds teh are of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """rints a rectangle of # characters by iterating over
        the height of the rectangle and printing a line of #
        characters with a length equal to the width."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        return f"[Rectangle]({self.id}) {self.__x}/{self.__y}" + \
                f"- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """It checks the length of the args tuple to
        determine how many arguments were provided.
        It assigns each argument to the corresponding
        attribute if that argument is provided.
        The order of assignment matches the order
        specified (id, width, height, x, y).
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        if not args or not kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary containing the id, width, height, x,
        and y attributes of the Rectangle instance. This method
        allows you to easily convert
        a Rectangle object into a dictionary representation.
        """
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
