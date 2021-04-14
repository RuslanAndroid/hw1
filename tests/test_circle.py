import pytest

from src.Circle import Circle

circle_name = "Обычный круг"
circle_perimeter = 188.49555921538757
circle_area = 2827.4333882308138


@pytest.fixture
def default_circle():
    hero = Circle(name=circle_name, radius=30)
    yield hero
    del hero


@pytest.fixture
def second_circle():
    hero = Circle(name=circle_name+"2", radius=60)
    yield hero
    del hero


def test_circle_name(default_circle):
    assert default_circle.name == circle_name


def test_circle_perimeter(default_circle):
    assert default_circle.perimeter == circle_perimeter


def test_circle_area(default_circle):
    assert default_circle.area == circle_area


def test_circle_angles(default_circle):
    assert default_circle.angles == 0


def test_circle_add_area(default_circle, second_circle):
    assert default_circle.add_area(second_circle) == default_circle.perimeter + second_circle.perimeter


def test_circle_not_add_area(default_circle):
    try:
        default_circle.add_area(1)
        assert False
    except Exception:
        assert True
