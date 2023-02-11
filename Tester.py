import Cell
import Spreadsheet
import datetime


class Tester:
    def test_cell_get_set_value(self):
        c = Cell.Cell()
        c.set_value('lala')
        if c.get_value() == 'lala':
            print("c.get_set_value() passed")
        else:
            print("c.get_set_value() failed")

    def test_cell_get_set_color(self):
        c = Cell.Cell()
        c.set_color(2)
        if c.get_color() == 'green':
            print("c.get_color() passed")
        else:
            print("c.get_color() failed")

    def test_cell_to_int(self):
        c = Cell.Cell(value='1')
        c.to_int()
        if type(c.get_value()) == int:
            print("to_int() passed")
        else:
            print("to_int() failed")

    def test_cell_to_float(self):
        c = Cell.Cell(value='1')
        c.to_float()
        if type(c.get_value()) == float:
            print("to_float() passed")
        else:
            print("to_float() failed")

    def test_cell_to_date(self):
        c = Cell.Cell(value="12/12/2013")
        c.to_date()
        if c.get_value() == datetime.datetime.strptime("12/12/2013", "%d/%m/%Y").date():
            print("to_date() passed")
        else:
            print("to_date() failed")

    def test_cell_reset(self):
        c = Cell.Cell()
        c.set_value = 'hurray'
        c.reset()
        if c.get_value() == '':
            print("reset() passed")
        else:
            print("reset() failed")

    def test_sp_get_cell_at(self):
        sp = Spreadsheet.Spreadsheet(rows=3, cols=3)
        c = sp.get_cell_at(row=1, col=1)
        if isinstance(c, Cell.Cell):
            print("test_sp_get_cell_at() passed")
        else:
            print("test_sp_get_cell_at() failed")

    def test_sp_set_cell_at(self):
        sp = Spreadsheet.Spreadsheet(rows=3, cols=3)
        c = Cell.Cell()
        sp.set_cell_at(1, 1, c)
        if sp.get_cell_at(1, 1) == c:
            print("test_sp_set_cell_at() passed")
        else:
            print("test_sp_set_cell_at() failed")

    def test_sp_add_row(self):
        sp = Spreadsheet.Spreadsheet(rows=3, cols=3)
        sp.add_row(1)
        if len(sp.mCells) == 4:
            print("add_row() passed")
        else:
            print("add_row() failed")

    def test_sp_remove_row(self):
        sp = Spreadsheet.Spreadsheet(3, 3)
        sp.remove_row(1)
        if len(sp.mCells) == 2:
            print("remove_row() passed")
        else:
            print("remove_row() failed")

    def test_sp_add_col(self):
        sp = Spreadsheet.Spreadsheet(2, 2)
        sp.add_col(1)
        if len(sp.mCells[0]) == 3:
            print("add_col() passed")
        else:
            print("add_col() failed")

    def test_sp_remove_col(self):
        sp = Spreadsheet.Spreadsheet(3, 3)
        sp.remove_col(1)
        if len(sp.mCells[0]) == 2:
            print("remove_col() passed")
        else:
            print("remove_col() failed")

    def test_sp_swap_cols(self):
        sp = Spreadsheet.Spreadsheet(2, 2)
        sp.set_cell_at(1, 1, 'col1')
        sp.set_cell_at(1, 0, 'col2')
        sp.swap_cols(0, 1)
        if sp.get_cell_at(1, 1) == 'col2' and sp.get_cell_at(1, 0) == 'col1':
            print("swap_cols() passed")
        else:
            print("swap_cols() failed")

    def test_sp_swap_rows(self):
        sp = Spreadsheet.Spreadsheet(3, 3)
        c1 = Cell.Cell(value='row1')
        c2 = Cell.Cell(value='row2')
        sp.set_cell_at(0, 0, c1)
        sp.set_cell_at(1, 0, c2)
        sp.swap_rows(0, 1)
        if sp.get_cell_at(0, 0).get_value() == "row2" and sp.get_cell_at(1, 0).get_value() == "row1":
            print("test_sp_swap_rows() passed")
        else:
            print("test_sp_swap_rows() failed")


t = Tester()
t.test_cell_get_set_value()
t.test_cell_get_set_color()
t.test_cell_to_int()
t.test_cell_to_float()
t.test_cell_to_date()
t.test_cell_reset()
t.test_sp_get_cell_at()
t.test_sp_set_cell_at()
t.test_sp_add_row()
t.test_sp_remove_row()
t.test_sp_add_col()
t.test_sp_remove_col()
t.test_sp_swap_cols()
t.test_sp_swap_rows()
