class Cell:
    def __init__(self, cells_amount):
        self.cells_amount = cells_amount

    def __add__(self, other):
        return self.cells_amount + other.cells_amount

    def __sub__(self, other):
        return self.cells_amount - other.cells_amount if self.cells_amount - other.cells_amount > 0 \
            else 'Разность кол-ва ячеек <= 0'

    def __mul__(self, other):
        return self.cells_amount * other.cells_amount

    def __truediv__(self, other):
        return round(self.cells_amount / other.cells_amount)

    def make_order(self, cells_in_row):
        return '\n'.join([''.join(['*' * cells_in_row + '\n']) * (self.cells_amount // cells_in_row)]) + \
               str('*' * (self.cells_amount % cells_in_row))


cell = Cell(15)
print(cell.make_order(6))
print()
print(cell.make_order(5))

cell2 = Cell(14)
print(cell + cell2)
print(cell - cell2)
print(cell2 - cell)
print(cell * cell2)
print(cell / cell2)

