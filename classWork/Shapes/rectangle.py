import math
from shape import Shape


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
