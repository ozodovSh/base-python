import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__("Rectangle")
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle")
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

t = Triangle(3, 4, 5)
r = Rectangle(4, 6)
c = Circle(5)

print("Triangle:", t.area(), t.perimeter())
print("Rectangle:", r.area(), r.perimeter())
print("Circle:", c.area(), c.perimeter())