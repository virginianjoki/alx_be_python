
import math

# Base class
class Shape:
    def area(self):
        #Method that raises NotImplementedError, to be overridden by derived classes.
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        #Initialize a Rectangle instance with length and width.
        self.length = length
        self.width = width

    def area(self):
        #Calculate the area of the rectangle (length × width).
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        #Initialize a Circle instance with radius.
        self.radius = radius

    def area(self):
        #Calculate the area of the circle (π × radius²).
        return math.pi * ("self.radiu s** 2")
    

# Example usage:
rect = Rectangle(10, 5)  # Rectangle with area = 10 * 5 = 50
print(f"The area of the Rectangle is: {rect.area()}")  # Output: 50

circle = Circle(7)  # Circle with radius 7, area ≈ π * 7² ≈ 153.94
print(f"The area of the Circle is: {circle.area()}")  # Output: 153.93804002589985    