# The tasks from the image translate to the following requirements:
# 1. Create a base class named Vehicle that represents a transportation device with attributes model and year. 
#    Then create a subclass named Car that inherits from Vehicle and adds an additional attribute fuel_type.
# 2. Create classes Animal and Flyable (with abstract methods) and a subclass Bird, which inherits from both 
#    classes. Implement methods of the abstract class Flyable in the subclass Bird.
# 3. Expand the Car class from the previous practice (creation of the base class Vehicle) by adding new 
#    attributes and methods, presenting various models of cars, such as Taxi, Ford, Tesla. Each of these classes 
#    should have additional attributes such as model_name and fuel_efficiency. Override methods of the base 
#    class and provide information about each car model.

from abc import ABC, abstractmethod

# Task 1: Vehicle and Car classes
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        return f"Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, model, year, fuel_type):
        super().__init__(model, year)
        self.fuel_type = fuel_type

# Task 2: Animal, Flyable, and Bird classes
class Animal(ABC):
    pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Animal, Flyable):
    def fly(self):
        return "This bird can fly."

# Task 3: Expand the Car class with specific models
class Taxi(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency
    
    def display_info(self):
        return (f"Taxi Model: {self.model_name}, Fuel Efficiency: {self.fuel_efficiency}, "
                f"{super().display_info()}")

class Ford(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency
    
    def display_info(self):
        return (f"Ford Model: {self.model_name}, Fuel Efficiency: {self.fuel_efficiency}, "
                f"{super().display_info()}")

class Tesla(Car):
    def __init__(self, model, year, fuel_type, model_name, fuel_efficiency):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name
        self.fuel_efficiency = fuel_efficiency
    
    def display_info(self):
        return (f"Tesla Model: {self.model_name}, Fuel Efficiency: {self.fuel_efficiency}, "
                f"{super().display_info()}")

# Create instances and test display_info method for each new Car subclass
taxi = Taxi("Generic", 2020, "Diesel", "Yellow Cab", 15)
ford = Ford("Generic", 2019, "Gasoline", "Focus", 30)
tesla = Tesla("Generic", 2021, "Electric", "Model S", 100)

print(taxi.display_info(), ford.display_info(), tesla.display_info(), Bird().fly())
