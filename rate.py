class Rate:
    def __init__(self, date, curr1, curr2, rate, colour):
        self.date = date
        self.curr1 = curr1
        self.curr2 = curr2
        self.rate = rate
        self.colour = colour

    def attributes(self):
        return self.date, self.curr1, self.curr2, self.rate