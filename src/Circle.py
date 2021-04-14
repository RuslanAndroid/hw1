from src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name=name, area=pi * radius ** 2, angles=0, perimeter=2*pi*radius)
