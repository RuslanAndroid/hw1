class Figure:
    def __init__(self, name="", area=0, angles=0, perimeter=0):
        self.name = name
        self.area = area
        self.angles = angles
        self.perimeter = perimeter

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise Exception('Ошибка', "это не фигура " + str(figure))
        return figure.perimeter + self.perimeter
