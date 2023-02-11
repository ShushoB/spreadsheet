import datetime
import Colors

class Cell:
    def __init__(self, value="", color_nb=0):
        self.value = value
        self.color = Colors.Colors(color_nb).name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_color(self):
        return self.color

    def set_color(self, color_nb):
        self.color = Colors.Colors(color_nb).name

    def to_int(self):
        try:
            self.value = int(self.value)
        except ValueError:
            print("Cannot convert to int")

    def to_float(self):
        try:
            self.value = float(self.value)
        except ValueError:
            print("Cannot convert to float")

    def to_date(self):
        try:
            self.value = datetime.datetime.strptime(self.value, "%d/%m/%Y").date()
        except ValueError:
            print("Cannot convert to date")

    def reset(self):
        self.value = ''
        self.color = Colors.Colors(0).name



