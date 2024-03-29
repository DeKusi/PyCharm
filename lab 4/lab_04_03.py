# 10
class Geometric:
    def calculateArea(self):
        print("Calculating area")


class Squar(Geometric):
    def __init__(self, a):
        self.side = a

    def _perimeter(self):
        print("Perimeter of Square {} : {}\n".format(self.side, self.side * 4))

    def calculateArea(self):
        print("Area of Square {} : {}\n".format(self.side, pow(self.side, 2)))


geom = Geometric()
geom.calculateArea()
sq = Squar(5)
sq.calculateArea()
sq._perimeter()
print("Check subclass: ", issubclass(Squar, Geometric))
print("Check instance sq -> Square: ", isinstance(sq, Squar))
print("Check instance sq -> Geometric:", isinstance(sq, Geometric))
print("Check instance sq -> dict: ", isinstance(sq, dict))
print("Geometric.__bases__: ", Geometric.__bases__)
print("Square.__bases: ", Squar.__bases__)

# 11
import math


class Circle(Geometric):

    def __init__(self, radius):
        Geometric.__init__(self)
        self.__reduce = radius

    def calculateArea(self):
        print("Area of Circle : {}\n".format(pi * pow(self.side, 2)))
