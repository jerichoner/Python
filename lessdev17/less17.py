# Первое задание: Функции для разных типов данных
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# Второе задание: Базовый класс Shape и его подклассы
class Shape:
    def area(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Третье задание: Интерфейс Drawable и классы, реализующие этот интерфейс
class Drawable:
    def draw(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

class DrawableCircle(Circle, Drawable):
    def draw(self):
        print(f"Рисуем круг с радиусом {self.radius}")

class DrawableRectangle(Rectangle, Drawable):
    def draw(self):
        print(f"Рисуем прямоугольник с длиной {self.length} и шириной {self.width}")

# Примеры использования
# Функции
print(add(10, 5))        # 15
print(subtract(10, 5))   # 5
print(multiply(10, 5))   # 50

# Фигуры и рисование
circle = DrawableCircle(5)
rectangle = DrawableRectangle(10, 5)

print(circle.area())     # 78.54 (округленно)
circle.draw()            # Рисуем круг с радиусом 5

print(rectangle.area())  # 50
rectangle.draw()         # Рисуем прямоугольник с длиной 10 и шириной 5
