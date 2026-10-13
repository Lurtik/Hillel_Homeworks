class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area == other.area


    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.area + other.area
        new_height = total_area / self.width
        return Rectangle(new_height, self.width)


    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        return Rectangle(self.width * n, self.height)

    def __str__(self):
        return f'Прямокутник: {self.width} x {self.height}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
