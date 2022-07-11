class Rate:
    def __init__(self, datetime, curr1, curr2, rate, colour):
        self.datetime = datetime
        self.curr1 = curr1
        self.curr2 = curr2
        self.rate = rate
        self.colour = colour

    def attributes(self):
        return self.datetime, self.curr1, self.curr2, self.rate, self.colour
