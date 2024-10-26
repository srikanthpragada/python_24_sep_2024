from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side


s = Square(10, 20, 40)
print(s.area())
