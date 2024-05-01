#1

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет"
    
person1 = Person("Python", 32)
person2 = Person("Ira", 25)

greet1 = person1.introduce()
greet2 = person2.introduce()
print(greet1)
print(greet2)


#2

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def display_info(self):
        print(f"{self.name} - {self.description}. {self.price} тенге")
    
product1 = Product("Iphone15", "Black, 128gb, IOS-17", 600000)
product2 = Product("Рюкзак", "Черный, объем 40л, производитель Nike", 10000)

product1.set_name("Iphone15pro")
product1.set_price(800000)

product1.display_info()
product2.display_info()

