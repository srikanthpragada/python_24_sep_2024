import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        return  f"Radius -> {self.radius}"

    def __eq__(self, other):
        return self.radius  == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __int__(self):
        return self.radius

c1 = Circle(10)  # c1.__init__(10)
c2 = Circle(10)
c3 = Circle(20)

print(c1) # str(c1) -> c1.__str__()
# print(str(c1))
# print(c1.__str__())

print(c1 == c2)   # c1.__eq__(c2)
print(c1 == c3)   # c1.__eq__(c3)
print(c3 > c1)
print(c1 < c3)
print(int(c1) + int(c2))



