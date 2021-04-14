import pytest

from src.Rectangle import Rectangle

rectangle_name = "Обычный прямоугольник"
rectangle_perimeter = 240
rectangle_area = 3500


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(name=rectangle_name, width=50, height=70)
    yield rectangle
    del rectangle


@pytest.fixture
def second_rectangle():
    rectangle = Rectangle(name=rectangle_name+"2", width=120, height=300)
    yield rectangle
    del rectangle


def test_rectangle_name(default_rectangle):
    assert default_rectangle.name == rectangle_name


def test_rectangle_perimeter(default_rectangle):
    assert default_rectangle.perimeter == rectangle_perimeter


def test_rectangle_area(default_rectangle):
    assert default_rectangle.area == rectangle_area


def test_rectangle_angles(default_rectangle):
    assert default_rectangle.angles == 4


def test_rectangle_add_area(default_rectangle, second_rectangle):
    assert default_rectangle.add_area(second_rectangle) == default_rectangle.perimeter + second_rectangle.perimeter


def test_rectangle_not_add_area(default_rectangle):
    try:
        default_rectangle.add_area(1)
        assert False
    except Exception:
        assert True
