"""
1. Given two integer numbers return their product. If the product is greater than 1000, then return their sum.
"""
print("Assignment 1: ")
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

product = num1 * num2
print("Product =", product)

if product > 1000:
    sum = num1 + num2
    print("Sum =", sum)

"""
2. Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number
"""
print("Assignment 2: ")

i = 0
sum = 0
while i < 10:
    sum = sum + i
    i += 1
print(sum)

"""
3. Print First 10 natural numbers using while loop.
"""
print("Assignment 3: ")
i = 0
while i < 10:
    print(i)
    i += 1

"""
4. Accept number from user and calculate the sum of all number from 1 to a given number
"""
print("Assignment 4: ")
num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print(sum)

"""
5. Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.
"""
print("Assignment 5: ")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 200, 300, 100]

for i in numbers:
    if i % 5 == 0:
        if i > 150:
            break
        else:
            print(i)

"""
6. Reverse the following list using for loop
"""
print("Assignment 6: ")

reversed_list = []

for i in range(len(numbers)):
    reversed_list.append(numbers[len(numbers)-(i+1)])
    # print(numbers[i])
print(reversed_list)

"""
7. Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function
For example: print('My', 'Name', 'Is', 'Tamim') will display MyNameIsJames

So use one of the formatting argument of print() to turn the output into My**Name**Is**Tamim
"""
print("Assignment 7: ")

name = "My name is Akib Samir"
print(name.replace(" ", "*"))

"""
8. Concatenate two lists index-wise
"""
print("Assignment 8: ")

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
concatenated_list = []

for i in range(len(num1)):
    for j in range(len(num2)):
        concatenated_list.append(num1[i]+num2[j])
print(concatenated_list)

"""
9. Given a Python list of numbers. Turn every item of a list into its square
"""
print("Assignment 9: ")

numbers = [1, 2, 3, 4, 5]
after_square = []
for i in numbers:
    after_square.append(i * i)

print(after_square)

"""
10. Access value 20 from the following tuple -> aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
"""
print("Assignment 10: ")
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

