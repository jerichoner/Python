# Translating the tasks from the image, they are as follows:
# 1. Create several functions that perform arithmetic operations (addition, subtraction, multiplication, division)
#    on various data types (integers, floats, strings). Use static typing polymorphism to handle different data types
#    with the same code.
# 2. Create a base class Shape with a method area() that calculates the area of the shape. Then create subclasses
#    representing different geometric shapes like Circle, Rectangle, and Triangle. Redefine the area() method in
#    each subclass to calculate the area of the corresponding shape.
# 3. Create an interface Drawable, representing objects that can be drawn. Then create classes Circle and Rectangle
#    that implement this interface. Each class should have a draw() method, which realizes different logic for
#    drawing a circle and a rectangle.

from abc import ABC, abstractmethod
from math import pi

# Task 1: Functions for arithmetic operations with static typing polymorphism
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")

# Task 2: Shape base class and its subclasses
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Task 3: Drawable interface and its implementations
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class DrawableCircle(Circle, Drawable):
    def draw(self):
        return f"Drawing a circle with radius {self.radius}."

class DrawableRectangle(Rectangle, Drawable):
    def draw(self):
        return f"Drawing a rectangle with width {self.width} and height {self.height}."

# Test the arithmetic functions
add_result = add(10, 5)          # Should work for integers
subtract_result = subtract(10.5, 5.2) # Should work for floats
multiply_result = multiply("a", 3)    # Should work for string and integer
divide_result = divide(10, 2)         # Should work for integers

# Test the area calculation for shapes
circle = Circle(3)
rectangle = Rectangle(4, 5)
triangle = Triangle(3, 4)

circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Test the draw method for drawable shapes
drawable_circle = DrawableCircle(3)
drawable_rectangle = DrawableRectangle(4, 5)

drawable_circle_draw = drawable_circle.draw()
drawable_rectangle_draw = drawable_rectangle.draw()

print(add_result, subtract_result, multiply_result, divide_result,
 circle_area, rectangle_area, triangle_area,
 drawable_circle_draw, drawable_rectangle_draw)
