# Translating the tasks from the image, they are as follows:
# 1. Create a program that prompts the user to input two numbers and tries to perform arithmetic division of one number by the other. 
#    Handle ZeroDivisionError and present an informative error message.
# 2. Create a custom exception called ValidationError, which can occur when validating user data. Then create a program that 
#    checks whether the entered name is composed only of letters. If the entered name contains numbers or symbols, raise 
#    the ValidationError with an appropriate message.
# 3. Create a context manager that measures the time taken to execute a block of code. Then use it to measure the time taken 
#    for input operations and output the time in milliseconds.

import time
from contextlib import contextmanager

# Task 1: Division program with error handling
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Task 2: Custom exception and validation program
class ValidationError(Exception):
    pass

def validate_name():
    name = input("Enter your name: ")
    if not name.isalpha():
        raise ValidationError("Name can only contain letters.")
    return "Name is valid."

# Task 3: Context manager for measuring execution time
@contextmanager
def time_execution():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")

# Using the context manager to measure the time of an input operation
with time_execution():
    name = input("Enter your name to measure the input time: ")

validation_error_message = ""

try:
    validate_name()
except ValidationError as e:
    validation_error_message = str(e)

result = divide_numbers()
print(result)

valid_name = validate_name()
print(valid_name)

print(validation_error_message)
