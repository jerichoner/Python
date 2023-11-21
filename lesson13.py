# Task 1: Create a Car class with attributes brand, model, and year. Add a method description() to print information about the car.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def description(self):
        return f"{self.year} {self.brand} {self.model}"

# Task 2: Create a Person class with attributes name and age. Create a subclass Employee inheriting from Person with an added salary attribute. Implement a method get_info() to print information about the employee.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

# Task 3: Create an Animal class with a speak() method. Create two subclasses: Dog and Cat, which override speak() to return "Woof!" and "Meow!", respectively.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Develop a BankAccount class with attributes balance and account_number. 
# Create a deposit() method that allows funds to be deposited into the account, 
# and a withdraw() method that allows funds to be withdrawn. 
# Create a SavingsAccount subclass that has an interest_rate attribute and an add_interest() method that adds interest to the balance.

class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount
        return self.balance

    def display_account_info(self):
        super().display_account_info()
        print(f"Interest Rate: {self.interest_rate}%")

# Example usage:

# Car
my_car = Car("Toyota", "Corolla", 2021)
print(my_car.description())

# Employee
employee = Employee("Alice", 30, 70000)
print(employee.get_info())

# Animals
dog = Dog()
cat = Cat()
print(dog.speak())  # Outputs: Woof!
print(cat.speak())  # Outputs: Meow!

# BankAccount
savings_account = SavingsAccount(1000, '87654321', 1.5)
savings_account.display_account_info()