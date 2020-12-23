class Cell:
    def __init__(self, amount_cell):
        self.amount_cell = amount_cell

    def __add__(self, other):
        return Cell(self.amount_cell + other.amount_cell)

    def __str__(self):
         return f'is: {self.amount_cell}'

    def __sub__(self, other):
        if int((self.amount_cell - other.amount_cell) < 0):
            print('Negative result !')
        else:
            return Cell(self.amount_cell - other.amount_cell)

    def __truediv__(self, other):

        Cell(self.amount_cell / other.amount_cell)
        return round((self.amount_cell / other.amount_cell), 0)

    def __mul__(self, other):
        return Cell(self.amount_cell * other.amount_cell)

    def make_order(self, cells_in_row):
        self.cells_in_row = cells_in_row
        return f'{self.amount_cell/cells_in_row}\n{self.amount_cell/cells_in_row}\n{self.amount_cell/cells_in_row}'




cell_one = Cell(int(input('Input cell amount of the first cell : ')))
cell_two = Cell(int(input('Input cell amount of the second cell : ')))
print(f'The sum of cells in the general cell {cell_one + cell_two}')
print(f'The difference of cells in the general cell  {cell_one - cell_two}')
print(f'The quotient of cells in the general cell  {cell_one / cell_two}')
print(f'The result of the multiplying of cells in the general cell  {cell_one * cell_two}')
print(cell_one.make_order(12))