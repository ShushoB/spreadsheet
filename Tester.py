import Cell
import Spreadsheet

class Tester:
    def test_cell_get_set_value(self):
        c = Cell.Cell()
        c.set_value = 'lala'
        if c.get_value == 'lala':
            print("c.get_set_value() passed")
        else:
            print("c.get_set_value() failed")


    def test_cell_get_color(self):
        c = Cell.Cell()
        c.set_color = 'green'
        if c.get_color == 'green':
            print("c.get_color() passed")
        else:
            print("c.get_color() failed")

    def test_cell_set_color(self):
        c = Cell.Cell()
        c.set_color = 'red'
        if c.get_color == 'red':
            print("c.set_color() passed")
        else:
            print("c.set_color) failed")


    def test_cell_to_int(self):
        c = Cell.Cell()
        c.to_int()
        if type(c.get_value()) == int:
            print("to_int() passed")
        else:
            print("to_int() failed")


    def test_cell_to_float(self):
        c = Cell.Cell()
        c.to_float()
        if type(c.get_value()) == float:
            print("to_float() passed")
        else:
            print("to_float() failed")


    def test_cell_to_date(self):
        c = Cell.Cell()
        c.set_value("12/12/2013")
        c.to_date()
        if c.get_value() == "2013-12-12":
            print("to_date() passed")
        else:
            print("to_date() failed")

    def test_cell_reset(self):
        c = Cell.Cell()
        c.set_value = 'hurrray'
        c.reset()
        if c.get_value() == '':
            print("reset() passed")
        else:
            print("reset() failed")

    def test_sp_get_set_cell_at(self):
        sp = Spreadsheet.Spreadsheet(2,2)
        sp.set_cell_at(1,1,'badumtss')
        if sp.get_cell_at(1,1) == 'badumtss':
            print("get_set_cell_at() passed")
        else:
            print("get_set_cell_at() failed")

    def test_sp_add_row(self):
        sp = Spreadsheet.Spreadsheet(2, 2)
        sp.set_cell_at(1, 1, 'badumtss')
        sp.add_row(1)
        if sp.get_cell_at(2, 1) == 'badumtss':
            print("add_row() passed")
        else:
            print("add_row() failed")

    def test_sp_remove_row(self):
        sp = Spreadsheet.Spreadsheet(3, 2)
        sp.set_cell_at(1, 1, 'badumtss')
        sp.remove_row(1)
        if sp.get_cell_at(1, 1) != 'badumtss':
            print("remove_row() passed")
        else:
            print("remove_row() failed")

    def test_sp_add_col(self):
        sp = Spreadsheet.Spreadsheet(2, 2)
        sp.set_cell_at(1, 1, 'lalala')
        sp.add_col(1)
        if sp.get_cell_at(1, 2) == 'lalala':
            print("add_col() passed")
        else:
            print("add_col() failed")

    def test_sp_remove_col(self):
        sp = Spreadsheet.Spreadsheet(2, 3)
        sp.set_cell_at(1, 1, 'lalala')
        sp.remove_col(1)
        if sp.get_cell_at(1, 1) != 'lalala':
            print("remove_col() passed")
        else:
            print("remove_col() failed")

    def test_sp_swap_cols(self):
        sp = Spreadsheet.Spreadsheet(2, 2)
        sp.set_cell_at(1, 1, 'Sh')
        sp.set_cell_at(1, 0, 'B')
        sp.swap_cols(0,1)
        if sp.get_cell_at(1, 1) == 'B' and sp.get_cell_at(1, 0) == 'Sh':
            print("swap_cols() passed")
        else:
            print("swap_cols() failed")

    def test_sp_swap_rows(self):
        sp = Spreadsheet.Spreadsheet(2, 2)
        sp.set_cell_at(1, 1, 'Sh')
        sp.set_cell_at(0, 1, 'B')
        sp.swap_cols(0, 1)
        if sp.get_cell_at(1, 1) == 'B' and sp.get_cell_at(0, 1) == 'Sh':
            print("swap_rows() passed")
        else:
            print("swap_rows() failed")
