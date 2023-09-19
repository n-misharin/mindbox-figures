import math

import pytest

from figures.circle import Circle, CircleCreateException
from tests.utils import EPS


class TestCircle:
    @pytest.mark.parametrize(
        "radius, expected",
        [
            (5, math.pi * 5 * 5),
            (0, 0),
            (0.001, math.pi * 0.001 * 0.001),
            (0.00000002, math.pi * 0.00000002 * 0.00000002),
            (1, math.pi * 1 * 1)
        ]
    )
    def test_calc_area(self, radius: float, expected: float):
        circle = Circle(radius)
        assert abs(circle.area() - expected) < EPS

    @pytest.mark.parametrize(
        "radius", [-5, -1, -0.001]
    )
    def test_negative_circle(self, radius):
        with pytest.raises(CircleCreateException):
            Circle(radius)
