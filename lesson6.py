#Task1
grade = int(input("Enter your grade from 1 to 10: "))

if 1 <= grade <= 3:
    print("Poor")
elif 4 <= grade <= 6:
    print("Satisfactory")
elif 7 <= grade <= 9:
    print("Good")
elif grade == 10:
    print("Excellent")
else:
    print("Incorrect grade. Please enter a number from 1 to 10.")

#Task2
time = int(input("Enter the current time in hours (from 0 to 23): "))

if 6 <= time < 12:
    print("Good morning!")
elif 12 <= time < 18:
    print("Good afternoon!")
elif 18 <= time < 24:
    print("Good evening!")
elif 0 <= time < 6:
    print("Good night!")
else:
    print("Incorrect time. Please enter a number from 0 to 23.")

#Task3
user_input = 10
divisible_by_three = [number for number in range(1, user_input + 1) if number % 3 == 0]
print(divisible_by_three)

#Task4
numbers_list = [4, -3, 7, -1, 9, -6]
positive_numbers = [number for number in numbers_list if number > 0]
average = sum(positive_numbers) / len(positive_numbers) if positive_numbers else 0
print(average)

#Task5
def print_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
print_christmas_tree(5)

#Task6
def print_butterfly(wings_size):
    for i in range(wings_size):
        print('*' * (i + 1) + ' ' * (2 * (wings_size - i) - 1) + '*' * (i + 1))
    for i in range(wings_size - 1, -1, -1):
        print('*' * (i + 1) + ' ' * (2 * (wings_size - i) - 1) + '*' * (i + 1))
print_butterfly(4)

#Task7
def print_chessboard(size):
    empty = '□'
    filled = '■'
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print(filled, end=' ')
            else:
                print(empty, end=' ')
        print()
print_chessboard(8)

#task8
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
bubble_sort([64, 34, 25, 12, 22, 11, 90])
