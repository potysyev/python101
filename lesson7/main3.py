class Cell:
    def __init__(self, cells_number):
        if isinstance(cells_number, int):
            self.cells_number = cells_number
        else:
            raise ValueError("Cells size is not integer")

    def __str__(self):
        return str(f"Number of cells {self.cells_number}")

    def __add__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(self.cells_number + other.cells_number)
        else:
            raise ValueError("Both arguments must be Cell class")

    def __sub__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if self.cells_number - other.cells_number > 0:
                return Cell(self.cells_number - other.cells_number)
            else:
                raise ValueError("Difference between arguments must be greater zero")
        else:
            raise ValueError("Both arguments must be Cell class")

    def __mul__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(self.cells_number * other.cells_number)
        else:
            raise ValueError("Both arguments must be Cell class")

    def __truediv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(self.cells_number // other.cells_number)
        else:
            raise ValueError("Both arguments must be Cell class")

    def make_order(self, linelen):
        output = []
        for i in range(1, self.cells_number + 1):
            output.append("*")
            if i % linelen == 0:
                output.append('\n')
        return ''.join([s for s in output])


c1 = Cell(11)
c2 = Cell(4)

print(c1.make_order(3))
print(c1 - c2)
