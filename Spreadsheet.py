import Cell


class Spreadsheet:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        c = Cell.Cell()
        self.mCells = [[c for _ in range(cols)] for _ in range(rows)]

    def get_cell_at(self, row, col):
        return self.mCells[row][col]

    def set_cell_at(self, row, col, value):
        self.mCells[row][col] = value

    def add_row(self, row):
        c = Cell.Cell()
        added_row = self.cols * [c]
        self.mCells.insert(row, added_row)
        return self.mCells

    def remove_row(self, row):
        del self.mCells[row]
        return self.mCells

    def add_col(self, column):
        c = Cell.Cell()
        for i in range(self.rows):
            self.mCells[i].insert(column, c)
        return self.mCells

    def remove_col(self, col):
        for i in range(self.rows):
            del self.mCells[i][col]
        return self.mCells

    def swap_rows(self, row, other_row):
        self.mCells[row], self.mCells[other_row] = self.mCells[other_row], self.mCells[row]
        return self.mCells

    def swap_cols(self, col, other_col):
        for i in range(self.rows):
            self.mCells[i][col], self.mCells[i][other_col] = self.mCells[i][other_col], self.mCells[i][col]
        return self.mCells
