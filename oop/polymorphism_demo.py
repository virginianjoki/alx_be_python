
class Shape:
    def area(self): 
        raise NotImplementedError
    
    def description(self):
        return "This is a shape"
    
class Rectangle(Shape):
    def _init_(self, length ,width):
        super()._init_()
        self.width = width
        self.length  = length
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius
        
    def area(self):
        import math
        return math.pi * self.radius**2