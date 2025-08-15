import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area(self) method")
    
class Rectangle(Shape):
    def __init__(self, area, length, width):
        super().__init__(area)        
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, area, radius):
        super().__init__(area)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius **2)
