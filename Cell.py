import datetime


Color = {0: 'white', 1: 'red', 2: 'green', 3: 'blue'}


class Cell:
    def __init__(self, value="", color=0):
        self.value = value
        self.color = Color.get(color)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = Color.get(color)

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
        self.color = Color.get(0)
