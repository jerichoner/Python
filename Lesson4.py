#Task 1
a = int(input("Enter the number A: "))
b = int(input("Enter the number B: "))

if a > b: 
    print("A more that B")
else: 
    print("B more that A")

#Task 2
if a > 10 and a < 20:
    print("The number A is between 10 and 20")
else:
    print("The number A is not between 10 and 20")

#Task 3
age = int(input("Enter your Age: "))

if age >= 18:
    print("You can ride a car")
elif age < 18 and age > 0:
    print("You need to grow up")
else:
    print("You not a human")

#Task 3
if age <= 2:
      print("You are Baby" )
elif age > 2 and age <= 12:
      print("You are Child")
elif age > 12 and age <= 18:
      print("You are Teenager")
elif age > 18 and age <= 35:
      print("You are Youth")
elif age > 35 and age <= 60:
      print("You are Adult")
else:
      print("You are Elderly man")

#Task 4
grade = int(input("Enter your Grade: "))

if grade == 1:
        print("You are Dumb")
elif grade == 2:
       print("Unsatisfactory")
elif grade == 3:
       print("Satisfactory")
elif grade == 4:
       print("Okay")
elif grade == 5:
       print("Excellent")
else:
       print("Invalid evaluation value!")

#Task 5
x = int(input("Enter the x"))
y = int(input("Enter the y"))

if x > 0 and y > 0:
      print("The point is in the First coordinate quadrant")
elif x < 0 and y > 0:
      print("The point is in the Second coordinate quadrant")
elif x < 0 and y < 0:
      print("The point is in the Third coordinate quadrant")
else:
      print("The point is in the Fourth coordinate quadrant")

#Task 6
number = int(input("Enter the Number: "))

if number % 2 == 0:
    if number % 4 == 0:
        print("The number is even and divisible by 4")
    else:
        print("The number is even but not divisible by 4")
else:
      print("The number is not even")

#Task 7
grade2 = int(input("Enter your Grade: "))

if grade2 >= 1 and grade2 < 3:
        print("Unsatisfactory")
if grade2 >= 3 and grade2 < 5:
       print("Satisfactory")
if grade2 >= 5 and grade2 < 7:
       print("Okay")
if grade2 >= 7 and grade2 <=10:
       print("Excellent")
if grade2 < 4:
    extra = input("Enter Extra Work: ")
    if extra != "":
        print("You are have an Extra Work: ", extra)
    else:
        print("You are dumb")
else:
       print("Invalid evaluation value!")

#Task 8
if number % 2 == 0 and number > 0:
        print("The number is even and upper zero")

#Task 9
year = int(input("Enter the Year:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
      print("This is leap year")
else:
      print("This is not leap year")

#Task 10
medicine = input("Enter your serious medical contraindications if there are any: ")

if age >= 18 and age <=45 and medicine == "":
      print("Wellcome!")
else:
      print("You are not allowed to enter")