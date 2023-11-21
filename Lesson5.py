#Task 1
for i in range(int(input("Enter the number: "))+1):
     if i % 2 == 0:
         print(i)

#Task 2
sum_of_numbers = sum(range(int(input("Enter the number: "))+1))
print("Sum of numbers up to", i+1, "inclusive", sum_of_numbers)


#Task 3
for i in range(20+1):
     if i % 2 == 0:
         print(i)


#Task 4 
number = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Task 5
for letter in "Python":
    print(letter)

#Task 6
num = 1
sum = 0
while num <= 100:
    if num % 2 != 0:
        sum += num
    num += 1
print(sum)

#Task 7
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print()

#Task 8    
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')
    print()

#task 9
for i in range(2, int(input("Enter the number: ")) + 1):
    prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(f"{i} is prime number.")
    else:
        print(f"{i} isn`t prime number.")
