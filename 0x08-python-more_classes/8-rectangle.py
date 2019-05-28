#!/usr/bin/python3
class Rectangle:
    """Class with a instance private attributes, with optional value 0
        validate type and value > to 0, send a message Error using raised
        and define a method to asign values
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method init
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """Method for string representation
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            st = ""
            for i in range(self.__height):
                st = "{}{}\n".format(st, self.print_symbol * self.__width)
            return st[:-1]

    def __repr__(self):
        """Method for representation class
        """
        return "Rectangle("+str(self.__width)+","+str(self.__height)+")"

    def __del__(self):
        """Method that delete a object
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """Method that return the area of the rectangle
        Args:
            Takes a self parameters
        Return:
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method that return the perimeter of the rectangle
        Args:
            Takes a self parameters
        Return:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (2 * (self.__width + self.__height))
        return perimeter

    @property
    def width(self):
        """Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1
