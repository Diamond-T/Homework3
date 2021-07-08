class house():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length*self.width

house_w_h = house(12, 10)
print(house_w_h.area())
