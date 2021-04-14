from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    __COUNT = 0

    def __init__(self, name, side1, side2, side3):
        p = (side1 + side2 + side3) / 2
        area = sqrt(p * (p - side1) * (p - side2) * (p - side3))
        perimeter = side1 + side2 + side3
        super().__init__(area=area, name=name, angles=3, perimeter=perimeter)
