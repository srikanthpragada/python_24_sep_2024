import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


c1 = Circle(10)  # c1.__init__(10)
c2 = Circle(10)
c3 = Circle(20)

print(c1)
print(c1 == c2)
print(c3 > c1)


