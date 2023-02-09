import Cell


class Spreadsheet:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        c = Cell.Cell()
        self.mCells = [[c for i in range(row)] for j in range(col)]

    def get_cell_at(self, row, col):
        return self.mCells[row][col]

    def set_cell_at(self, row, col, value):
        self.mCells[row][col] = value

    def add_row(self, row):
        c = Cell.Cell()
        added_row = self.col * [c]
        self.mCells.insert(row, added_row)
        return self.mCells

    def remove_row(self, row):
        del self.mCells[row]
        return self.mCells

    def add_col(self, column):
        c = Cell.Cell()
        for i in range (self.row):
            self.mCells[i].insert(column, c)
        return self.mCells

    def remove_col(self, col):
        for i in range (self.row):
            del self.mCells[i][col]
        return self.mCells

    def swap_rows(self, row, other_row):
        self.mCells[row], self.mCells[other_row] = self.mCells[other_row], self.mCells[row]
        return self.mCells

    def swap_cols(self, col, other_col):
        self.mCells[col], self.mCells[other_col] = self.mCells[other_col], self.mCells[col]
        return self.mCells



