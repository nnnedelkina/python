class Cell:

    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        sub = self.nucleus - other.nucleus
        if sub > 0:
            return Cell(sub)
        else:
            print('В первой клетке недостаточно ячеек')
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def make_order(self, num):
        self.num = num
        return ('*' * num + '\n') * (self.nucleus // num) + '*' * (self.nucleus % num)


cell_1 = Cell(12)
cell_2 = Cell(18)
cell_3 = cell_1 + cell_2
print(cell_3.nucleus)

cell_4 = cell_1 - cell_2
print(cell_4.nucleus)

cell_5 = cell_1 * cell_2
print(cell_5.nucleus)

cell_6 = cell_1 / cell_2
print(cell_6.nucleus)

print(cell_1.make_order(4))
