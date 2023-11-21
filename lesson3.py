#Task 1

name = input("Enter your name: ")
print ("Hello, ", name, "!")

#Task2 Task3

biology = int(input("Enter your grade on biology: "))
russian = int(input("Enter your grade on Russian: "))
geography = int(input("Enter your grade on Geography: "))
math = int(input("Enter your grade on Math: "))
average = (biology+russian+geography+math)//4
print ("Youre middle grade is: ", average)
print("And now we let`s count all your grade. Let's bring out the best and worst of them ")
if biology > geography and biology > russian and biology > math:
       print("The best grade on Biology!")
elif geography > biology and geography > math and geography > russian:
      print("The best grade on Geography!")
elif russian > biology and russian > geography and russian > math:
     print("The best grae on Russian!")
else:
     print("The best grade on Math!")
if biology < geography and biology < russian and biology < math:
       print("To bad grade on Biology!")
elif geography < biology and geography < math and geography < russian:
      print("To bad grade on Geography!")
elif russian < biology and russian < geography and russian < math:
     print("To bad grade on Russian!")
else:
     print("To bad grade on Math!")

#Task 4
print("And now we collect your personal data!")
second_name = input("Enter your Second Name: ")
age = int(input("Enter your Age: "))
phone = int(input("Enter your Phone number: "))
city = input("Enter your City: ")
email = input("Enter your E-mail: ")
print ('\n' "Personal card", '\n' "Name: ",name, second_name, '\n' "Age: ", age, '\n' "Phone number: ", phone, '\n' "City: ", city, '\n' "E-mail:", email)
