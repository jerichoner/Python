# Task 1: Creating a custom module math_operations.py which contains functions for addition, subtraction, multiplication, and division.

# Simulating the math_operations module
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y