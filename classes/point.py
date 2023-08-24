class Point:
    default_color = "red"
    default_color1 = "ye"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"draw ({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


Point.default_color1 = "yellow"
point = Point(1, 2)
other = Point(1, 2)
print(type(point))
# check instance
print(isinstance(point, Point))

print(point.x)
point.draw()

print(point.default_color)
print(point.default_color1)
print(point == other)
combined = point + other
print(combined.x)
