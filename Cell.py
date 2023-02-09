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
        return self.color

    def to_int(self):
        self.value = int(self.value)
        return self.value

    def to_float(self):
        self.value = float(self.value)
        return float(self.value)

    def to_date(self):
        self.value = datetime.datetime.strptime(self.value, "%d/%m/%Y").date()
        return self.value

    def reset(self):
        self.value = ''
        self.color = 'white'


