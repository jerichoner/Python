# We will solve each task from the image with English variable names and descriptions.

# Task 1: Create a list of numbers and find the sum and average value.
numbers_list = [10, 20, 30, 40, 50]  # Example list of numbers
total_sum = sum(numbers_list)
average_value = total_sum / len(numbers_list)

# Task 2: Create a tuple with information about employees and display this information.
employees_info = (("John", "Manager"), ("Susan", "Accountant"), ("Mike", "Engineer"))  # Example employee info
for employee in employees_info:
    print(f"Name: {employee[0]}, Position: {employee[1]}")

# Task 3: Remove elements from a list by condition (e.g., remove all numbers greater than 20).
filtered_numbers = [number for number in numbers_list if number <= 20]

# Task 4: Create a list of fruits with several different fruits. Write a loop that removes all fruits from the list with a length of less than 5 characters.
fruits = ["apple", "pear", "banana", "kiwi", "mango", "plum"]
fruits = [fruit for fruit in fruits if len(fruit) >= 5]

# The results will be displayed.
print(total_sum, average_value, filtered_numbers, fruits)

# Continuing with the solutions for the tasks using English variables and descriptions.

# Task 5: Create a list of tuples 'students', where each tuple contains the name of a student and their grade.
students_list = [('Alice', 88), ('Bob', 92), ('Charlie', 90)]

# Task 6: Create a list 'numbers' from 1 to 20, but only with even numbers.
even_numbers_list = [num for num in range(1, 21) if num % 2 == 0]

# Task 7: Find the sum of the squares of all numbers from a new list.
sum_of_squares = sum(num ** 2 for num in even_numbers_list)

# Task 8: Create a two-dimensional list 'matrix', representing a 10x10 matrix. Imagine and perform some manipulation with it.
# Creating a 10x10 matrix
matrix_10x10 = [[i * 10 + j for j in range(10)] for i in range(10)]

# Example manipulation: Increasing each element by 1
manipulated_matrix = [[element + 1 for element in row] for row in matrix_10x10]

(students_list, even_numbers_list, sum_of_squares, manipulated_matrix)
