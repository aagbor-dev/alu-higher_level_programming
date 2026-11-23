#!/usr/bin/python3
"""Defines the Rectangle class, which inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with a size and a position.

    The width, height, x and y attributes are private. Each one has a
    getter and a setter that validates the new value.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create a rectangle.

        Args:
            width (int): the width, greater than 0.
            height (int): the height, greater than 0.
            x (int): the horizontal position, 0 or more.
            y (int): the vertical position, 0 or more.
            id (int): the id of the instance, passed to the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_integer(name, value):
        """Raise TypeError if value is not an integer.

        Args:
            name (str): the name of the attribute, used in the message.
            value: the value to check.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the horizontal position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the vertical position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle with the character #.

        The y attribute gives the number of empty lines before the
        rectangle, and the x attribute gives the number of spaces
        before each row.
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign values to the attributes of the rectangle.

        Args:
            *args: the new values, in the order id, width, height, x, y.
            **kwargs: the new values by name. Ignored if args is not empty.
        """
        names = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)
