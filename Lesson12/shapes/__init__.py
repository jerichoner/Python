from circle import Circle
from rectangle import Rectangle

# Create a circle with radius 5 and calculate its area and perimeter
circle = Circle(5)
circle_area = circle.area()
circle_perimeter = circle.perimeter()

# Create a rectangle with length 4 and width 3 and calculate its area and perimeter
rectangle = Rectangle(4, 3)
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()

print(f"Circle: Area = {circle_area}, Perimeter = {circle_perimeter}")
print(f"Rectangle: Area = {rectangle_area}, Perimeter = {rectangle_perimeter}")
