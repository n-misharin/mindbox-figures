from __future__ import annotations

import enum
from typing import Union

from figures.figure import Figure, CreateFigureException


class CreateTriangleException(CreateFigureException):
    pass


class TriangleTypes(enum.Enum):
    OBTUSE = "obtuse"
    RECTANGULAR = "rectangular"
    ACUTE = "acute"


class Triangle(Figure):

    def __init__(self, a: float, b: float, c: float):
        self.sides = a, b, c

    def __set_a(self, value: float) -> None:
        a, b, c = value, self.__b, self.__c
        if not Triangle.is_exist((a, b, c)):
            raise CreateTriangleException(f"Triangle with sides {a}, {b}, {c} does not exist.")
        self.__a = value

    def __set_b(self, value: float) -> None:
        a, b, c = self.__a, value, self.__c
        if not Triangle.is_exist((a, b, c)):
            raise CreateTriangleException(f"Triangle with sides {a}, {b}, {c} does not exist.")
        self.__b = value

    def __set_c(self, value: float) -> None:
        a, b, c = self.__a, self.__b, value
        if not Triangle.is_exist((a, b, c)):
            raise CreateTriangleException(f"Triangle with sides {a}, {b}, {c} does not exist.")
        self.__c = value

    def __set(self, sides: tuple[float, float, float]) -> None:
        a, b, c = sides
        if not Triangle.is_exist(sides):
            raise CreateTriangleException(f"Triangle with sides {a}, {b}, {c} does not exist.")
        self.__a, self.__b, self.__c = a, b, c

    def perimeter(self) -> float:
        return self.__c + self.__b + self.__a

    def get_type(self) -> TriangleTypes:
        return Triangle.type(self)

    def area(self) -> float:
        p = self.perimeter()
        return (p * (p - self.__c) * (p - self.__b) * (p - self.__a)) ** 0.5

    @staticmethod
    def is_exist(triangle: Union[Triangle, tuple[float, float, float]]) -> bool:
        a, b, c = triangle if isinstance(triangle, tuple) else triangle.sides
        return a + b > c > 0 and a + c > b > 0 and c + b > a > 0

    @staticmethod
    def type(triangle: Union[Triangle, tuple[float, float, float]]) -> TriangleTypes:
        a, b, c = sorted(triangle if isinstance(triangle, tuple) else triangle.sides)

        if not Triangle.is_exist(triangle.sides):
            raise CreateTriangleException(f"Triangle with sides {a}, {b}, {c} does not exist.")

        if c ** 2 == b ** 2 + a ** 2:
            return TriangleTypes.RECTANGULAR

        if c ** 2 > b ** 2 + a ** 2:
            return TriangleTypes.OBTUSE

        return TriangleTypes.ACUTE

    a = property(lambda self: self.__a, __set_a)

    b = property(lambda self: self.__b, __set_b)

    c = property(lambda self: self.__c, __set_c)

    sides = property(lambda self: (self.__a, self.__b, self.__c), __set)
