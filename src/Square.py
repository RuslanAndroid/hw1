from src.Figure import Figure


class Square(Figure):
    def __init__(self, name, width):
        super().__init__(area=width ** 2, name=name, angles=4, perimeter=width * 4)
