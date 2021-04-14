import pytest

from src.Square import Square

square_name = "Обычный квадрат"
square_perimeter = 200
square_area = 2500


@pytest.fixture
def default_square():
    square = Square(name=square_name, width=50)
    yield square
    del square


@pytest.fixture
def second_square():
    square = Square(name=square_name+"2", width=120)
    yield square
    del square


def test_square_name(default_square):
    assert default_square.name == square_name


def test_square_perimeter(default_square):
    assert default_square.perimeter == square_perimeter


def test_square_area(default_square):
    assert default_square.area == square_area


def test_square_angles(default_square):
    assert default_square.angles == 4


def test_square_add_area(default_square, second_square):
    assert default_square.add_area(second_square) == default_square.perimeter + second_square.perimeter


def test_square_not_add_area(default_square):
    try:
        default_square.add_area(1)
        assert False
    except Exception:
        assert True
