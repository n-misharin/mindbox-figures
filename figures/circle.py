import math

from figures.figure import Figure, CreateFigureException


class CircleCreateException(CreateFigureException):
    pass


class Circle(Figure):

    def __init__(self, radius: float):
        if radius < 0:
            raise CircleCreateException("Circle radius must be non negative.")
        self.radius = radius

    def length(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius
