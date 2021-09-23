print("Hello World")

# varible
"""
variable is like a container.
we can store data in a variable
we can declare variavle name with Alphabetic letter(A-Z or a-z) and number
We can't use any symbles as a variable name
variable name should start with a letter
Variable name is case sensetive ex. a and A are two differents variavle
"""
name = "Akib Samir"
age = 26

# Data Types
# integer, float, string, list, tuple, dictionary, boolean
print(type(name))   # we can use type() to know the data type
print(type(age))


# Conditional Statement
# if else statement
"""
when is_present = True then print if statement
when is_present = False then print else statement
"""
is_present = True
if  is_present:
    print("Good Boy")
else:
    print("Bad Boy")

# if elif else statement
cgpa = float(input("Enter your CGPA(0-4): "))
"""
Remember python always get input as a string
if we use it as any other data type we need to convert it
and we convert our input data as floating value
It also known as type casting 
"""

if cgpa == 4.0:
    print("A+")
elif cgpa >= 3.75 and cgpa < 4.0:
    print("A")
elif cgpa >= 3.50 and cgpa < 3.75:
    print("A-")
elif cgpa >= 3.25 and cgpa < 3.50:
    print("B+")
elif cgpa >= 3.0 and cgpa < 3.25:
    print("B")
elif cgpa >= 2.75 and cgpa < 3.0:
    print("B-")
elif cgpa >= 2.50 and cgpa < 2.75:
    print("C+")
elif cgpa >= 2.25 and cgpa < 2.50:
    print("C")
elif cgpa >= 2.0 and cgpa < 2.25:
    print("D")
else:
    print("F")

# Nested if
age = int(input("Enter your age: "))
if age >= 18:
    print("Your age is okay. You need to bring your NID with you.")
    nid = input("Do you have NID? Y/N: ")
    if nid.upper() == "Y":
        print("Go and give a vote.")
    else:
        print("Sorry! Go back home and bring your NID.")
else:
    print("You are a teeneger. You are not elligible to giving the vote")


