from math_operations import MathOperations
from text_operations import TextOperations
from student import Student

# Example usage of the simulated modules/classes
# Math operations
math_ops = MathOperations()
addition_result = math_ops.add(10, 5)
subtraction_result = math_ops.subtract(10, 5)
multiplication_result = math_ops.multiply(10, 5)
division_result = math_ops.divide(10, 5)

# Text operations
text_ops = TextOperations()
word_count = text_ops.count_words("Hello world this is an example text")

# Student information
student = Student("Alice", 22)
student_info = student.display_info()

print(addition_result, subtraction_result, multiplication_result, division_result, word_count, student_info)