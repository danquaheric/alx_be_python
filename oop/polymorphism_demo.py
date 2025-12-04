import math


class Shape:
    """
    Base class for different shapes.
    The area method is meant to be overridden by subclasses.
    """

    def area(self):
        """
        Calculate the area of the shape.
        This base implementation forces subclasses to override it.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """
    Rectangle shape with length and width.
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        Formula: length × width
        """
        return self.length * self.width


class Circle(Shape):
    """
    Circle shape with a given radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)