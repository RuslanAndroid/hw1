from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, width, height):
        super().__init__(area=width * height, name=name, angles=4, perimeter=(width + height) * 2)
