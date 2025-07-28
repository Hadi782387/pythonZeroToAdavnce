class Shape:
    def __init__(self, color, isFilled):
        self.color = color
        self.isFilled = isFilled

class Circle(Shape):
    def __init__(self, color, isFilled, radius):
        super().__init__(color, isFilled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, isFilled, side):
        super().__init__(color, isFilled)
        self.side = side

class Triangle(Shape):
    def __init__(self, color, isFilled, width):
        super().__init__(color, isFilled)
        self.width = width

# Circle object create
circle = Circle(color="green", isFilled=True, radius=5)

# Output
print(circle.color)
print(circle.isFilled)
print(circle.radius)
