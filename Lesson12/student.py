# Task 3: Creating a module student.py with a class Student that has attributes for name and age, and a method to display student information.

# Simulating the student module
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Student Name: {self.name}, Age: {self.age}"