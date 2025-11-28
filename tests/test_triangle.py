import pytest

from triangle.triangle import classify_triangle


def test_equilateral():
    assert classify_triangle(3, 3, 3) == "equilateral"


def test_isosceles():
    assert classify_triangle(5, 5, 3) == "isosceles"
    assert classify_triangle(5, 3, 5) == "isosceles"
    assert classify_triangle(3, 5, 5) == "isosceles"


def test_scalene():
    assert classify_triangle(4, 5, 6) == "scalene"


def test_non_positive():
    with pytest.raises(ValueError):
        classify_triangle(0, 1, 1)
    with pytest.raises(ValueError):
        classify_triangle(-1, 2, 3)


def test_non_number():
    with pytest.raises(ValueError):
        classify_triangle("a", 1, 1)


def test_not_triangle():
    with pytest.raises(ValueError):
        classify_triangle(1, 2, 3)
    with pytest.raises(ValueError):
        classify_triangle(1, 1, 3)
