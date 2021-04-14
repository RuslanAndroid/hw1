import pytest

from src.Triangle import Triangle

triangle_name = "Обычный треугольник"
triangle_perimeter = 79
triangle_area = 85.6281933711088


@pytest.fixture
def default_triangle():
    triangle = Triangle(name=triangle_name, side1=23, side2=17, side3=39)
    yield triangle
    del triangle


@pytest.fixture
def second_triangle():
    triangle = Triangle(name=triangle_name+"2", side1=55, side2=21, side3=38)
    yield triangle
    del triangle


def test_triangle_name(default_triangle):
    assert default_triangle.name == triangle_name


def test_triangle_perimeter(default_triangle):
    assert default_triangle.perimeter == triangle_perimeter


def test_triangle_area(default_triangle):
    assert default_triangle.area == triangle_area


def test_triangle_angles(default_triangle):
    assert default_triangle.angles == 3


def test_triangle_add_area(default_triangle, second_triangle):
    assert default_triangle.add_area(second_triangle) == default_triangle.perimeter + second_triangle.perimeter


def test_triangle_not_add_area(default_triangle):
    try:
        default_triangle.add_area(1)
        assert False
    except Exception:
        assert True
