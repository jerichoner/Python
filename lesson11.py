import math
from datetime import datetime, timedelta

# Task 1: Write a program that calculates the area of a circle with a given radius using the formula πr².
def calculate_circle_area(radius):
    return math.pi * radius**2

# Task 2: Write a program that determines if a given number is prime (has no divisors other than 1 and itself).
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Task 3: Create a function that takes two arguments: the length of the base and the height of a triangle, and calculates its area.
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Task 4: Write a program that outputs the date 7 days from the current date.
def date_in_seven_days():
    return datetime.now() + timedelta(days=7)

# Task 5: Create a function that takes two dates and calculates the number of days between them.
def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

# Examples of using the functions
circle_area = calculate_circle_area(5)
prime_check = is_prime(29)
triangle_area = calculate_triangle_area(10, 5)
future_date = date_in_seven_days()
days_difference = days_between_dates(datetime(2023, 1, 1), datetime(2023, 1, 31))

print(circle_area, prime_check, triangle_area, future_date, days_difference)

import random
import string
import time

# Task 1: Write a program that outputs the day of the week for a given date.
def get_weekday(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.strftime('%A')

# Task 2: Create a function that generates a random name consisting of letters and digits.
def generate_random_name(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length - 1)) + str(random.randint(0, 9))

# Task 3: Write a program that randomly selects a winner from a list of participants by index.
def select_random_winner(participants):
    winner_index = random.randint(0, len(participants) - 1)
    return participants[winner_index]

# Task 4: Write a program that generates a random number from 1 to 6 and congratulates the user if a specified number is rolled.
def roll_dice_and_congratulate(rolled_number):
    result = random.randint(1, 6)
    return f"Rolled a {result}, {'Congratulations!' if result == rolled_number else 'Try again.'}"

# Task 5: Write a program that outputs the current time every second for a minute.
def display_time_each_second():
    start_time = time.time()
    while time.time() - start_time < 60:
        print(datetime.now().strftime('%H:%M:%S'))
        time.sleep(1)

# Demonstrate the usage of these functions and display the results.

# Get the day of the week for a given date
weekday = get_weekday('2023-12-25')  # Christmas Day 2023

# Generate a random name
random_name = generate_random_name(8)

# Select a random winner from a list of names
participants = ['Alice', 'Bob', 'Charlie', 'David']
winner = select_random_winner(participants)

# Roll a dice and check for a specified number (4 in this case)
dice_roll_result = roll_dice_and_congratulate(4)

# Display the current time every second for a minute (this will print a lot, so we'll comment it out)
# display_time_each_second()

print(weekday, random_name, winner, dice_roll_result)

# Task 1: Create a function that outputs the current time in "HH:MM:SS AM/PM" format and in 24-hour format.
def get_current_time():
    current_time_12h = datetime.now().strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    current_time_24h = datetime.now().strftime('%H:%M:%S')     # 24-hour format
    return current_time_12h, current_time_24h

# Task 2: Write a program that generates a random time (hours, minutes, seconds) and outputs it in a user-friendly format.
def generate_random_time():
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    random_time = datetime.now().replace(hour=random_hour, minute=random_minute, second=random_second)
    return random_time.strftime('%I:%M:%S %p'), random_time.strftime('%H:%M:%S')

# Execute the functions and display the results.
current_time_formats = get_current_time()
random_time_formats = generate_random_time()

print(current_time_formats, random_time_formats)
