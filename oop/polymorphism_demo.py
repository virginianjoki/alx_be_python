class Shape:
    def area(self): 
        # Method to be overridden by derived classes
        raise NotImplementedError("Subclass must implement abstract method")
    
    def description(self):
        # Method to return a basic description of a shape
        return "This is a shape"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        # Corrected the constructor call to super().__init__()
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
        # Returns the area of the rectangle (length * width)
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        # Correctly initializing the Circle's radius
        super().__init__()  # Optional if Shape class has an __init__, here for consistency
        self.radius = radius
        
    def area(self):
        # Returns the area of the circle (π * radius²)
        import math
        return math.pi * self.radius ** 2
