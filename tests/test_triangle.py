import itertools

import pytest

from figures.triangle import Triangle, CreateTriangleException, TriangleTypes


class TestTriangle:

    @pytest.mark.parametrize(
        "a, b, c, expected",
        [
            (1, 1, 1, (3 * 2 * 2 * 2) ** 0.5),
            (3, 4, 5, (12 * 9 * 8 * 7) ** 0.5),
            *[
                (a, b, c, ((15 * 11 * 10 * 9) ** 0.5))
                for a, b, c in itertools.permutations([4, 5, 6])
            ]
        ]
    )
    def test_calc_area(self, a: float, b: float, c: float, expected: float):
        assert Triangle(a, b, c).area() == expected

    @pytest.mark.parametrize(
        "a, b, c",
        [
            (0, 0, 0),
            (-1, 1, 1),
            (1, -1, 1),
            (1, 1, -1),
            *[
                combination for combination in itertools.permutations([1, 2, 3])
            ],
        ]
    )
    def test_create_exception(self, a: float, b: float, c: float):
        with pytest.raises(CreateTriangleException):
            Triangle(a, b, c)

    @pytest.mark.parametrize(
        "a, b, c, t_type",
        [
            (2, 2, 2, TriangleTypes.ACUTE),
            *[
                (a, b, c, TriangleTypes.ACUTE)
                for a, b, c in itertools.permutations([4, 4, 5])
            ],
            *[
                (a, b, c, TriangleTypes.OBTUSE)
                for a, b, c in itertools.permutations([3, 4, 6])
            ],
            *[
                (a, b, c, TriangleTypes.RECTANGULAR)
                for a, b, c in itertools.permutations([3, 4, 5])
            ]
        ]
    )
    def test_triangle_type(self, a: float, b: float, c: float, t_type: TriangleTypes):
        assert Triangle(a, b, c).get_type() == t_type

    @pytest.mark.parametrize(
        "a, b, c",
        [
            (a, b, c) for a, b, c in itertools.permutations([1, 2, 3])
        ]
    )
    def test_sides_property(self, a: float, b: float, c: float):
        triangle = Triangle(3, 3, 3)
        with pytest.raises(CreateTriangleException):
            triangle.a = a
            triangle.b = b
            triangle.c = c
        with pytest.raises(CreateTriangleException):
            triangle.sides = a, b, c
