 #Код 2 - Класс InventoryItem

class InventoryItem():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def display_info(self):
        print(f"Название товара {self.name}; Количество товара {self.quantity} мешков; Цена товара {self.price} тенге")

    def uvl(self):
        u = self.quantity + 80
        print(f"Завтра придет новая партия {self.name} и общее количество будет {u}")
    
    def umen(self):
        um = self.quantity - 30
        print(f"Сегодня продали {um} мешков {self.name}")

    def obsh_st(self):
        st = self.quantity * self.price
        print(f"Общая стоимость товара {st}")

tovar = InventoryItem("Мука", 50, 7000)
tovar.display_info()
tovar.uvl()
tovar.umen()
tovar.obsh_st()

#Код 3 - Класс Student

class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def print_info(self):
        print(f"Студент: {self.name} Оценки: {self.grades}")
    
    def average(self):
        aver = sum(self.grades) / len(self.grades)
        print(f"Успеваемость студента {self.name}: {aver}")

student1 = Student("Иван", [4, 5, 4, 3, 5, 2, 2, 2, 3])
student1.print_info()
student1.average()

