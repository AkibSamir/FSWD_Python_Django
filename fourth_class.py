# Nested Function

def outer_function():
    def inner_function():
        print("This is inner function")
    print("This is outer function")
    return inner_function()

outer_function()

def first_function(name):
    def second_function():
        print("Welcome ", name)
    second_function()

first_function("Sam")


# Write a factorial function
def factorial(number):
    try:
        if number < 0:
            raise ValueError("Your value have to be grater than 0")
        if not isinstance(number, int):
            raise TypeError("Input value must be a number.")
        if number == 0:
            return 1
        return number * factorial(number - 1)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

print(factorial(5))

# Lambda function
print("*" * 5, "Lambda Function", "*" * 5)
addition = lambda x, y: x + y
print(addition(10, 5))

subtraction = lambda x, y: x - y
print(subtraction(10, 5))

multiplication = lambda x, y: x * y
print(multiplication(10, 5))

division = lambda x, y: x / y
print(division(10, 5))

modulus = lambda x, y: x % y
print(modulus(11, 5))


# Iterator
for i in range(10):
    print(i, end=" ")
print()
print(range(10))

# Generator
def my_range(limit):
    for i in range(limit):
        yield i

for i in my_range(10):
    print(i, end=" ")

print("\nGenerator with start end and step")
def my_range2(start=1, end=0, step=1):
    for i in range(start, end, step):
        yield i

for i in my_range2(1, 20, 2):
    print(i, end=" ")

# map()
print("Mapping: ")
numbers = [10, 20, 30, 40, 50]
number_map = map(lambda x:x, numbers)
print(number_map)
for i in number_map:
    print(i, end=" ")

# reduce()
print("\nReduce: ")
from functools import reduce
reduce_num = reduce(lambda x, y: x + y, numbers)
print(reduce_num)

print(reduce(lambda x, y: x if x < y else y, [10, 20, 30]))

# filter()
def even_number(number):
    if number % 2 == 0:
        return True

result = filter(even_number, [1, 3, 4, 5, 7, 8])
print(list(result))



