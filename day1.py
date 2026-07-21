# python is a high-level programming language that is widely used for web development, data analysis, AIML etc
# It is known for its simplicity and readability, making it a great choice for beginners and experienced developers alike.
# It is an Open-source language, which means that it is free to use and distributed
print("hello world")

#variables
x = 6
print(x)

x = y = z = 100
print(x,y,z)

x, y, z = 1, 2.5, "matrix"
print(x,y,z)

#Operators

# Comparison Operators
a, b = 10, 20
print(a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)

# Logical Operators

a, b = True, False

print(a and b)
print(a or b)
print(not b)
print(not a)

# Bitwise Operators

a = 11
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#keywords

import keyword
print(" the predefined keywords that cannot be used are: ")
print(keyword.kwlist)

# for example, we cannot use a " for " variable because it is a keyword.

# type of a datatype

x, y, z = 1, 2.5, True

print(type(x))
print(type(y))
print(type(z))

# String 
var = " Python is slower than java "
print(var)
print(type(var))
# access a string via it's index
print(var[1])
print(var[8])
print(var[-3])


# LIST
# A List can store different data types in itself.
a = [1,2,3]
print(a)
b = ["luna",12,True]
print(b)
print(b[1])

# Tuple
# A tuple is an immutable collection to store multiple items but they cannot be modified.
t1 =(1,)
print(type(t1))

# truthy and falsy values
if 1:
    print("1 is truthy")
if not 0:
    print("0 is falsy")
    
# Conditional statements
# if, if else, if elseif else, nested if else

# If condition: 
age = 20
if age >= 18:
    print("Adult")

# If-else condition(+ Type conversion ):
age = 18
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

age= input("Enter your age: ")
age_int = int(age)
print(type(age_int))
print(age)
if age_int >= 18:
    print("Eligible to enter")
else:
    print("Sorry, you're not eligible")

# In this program, i understood how type conversion actually works.
# i struggled when i noticed my code wasn't executing due to " cannot use for str and int "
# i thought for a while and realised to check the type of the age variable
# Once i saw it displayed age as <class 'int'> i knew i should perform type conversion
# i basically created a new variable named age_int and i converted the previous age to integer.
# This is for runtime execution btw.

# If elif-else statement

# An example to check the marital status of a user alongside if he is a teen or adult 
# In this code i made a mistake and i had to solve it. here is my mistake
"""
age = input("What is your age?")
ask = input("What is your status?: (single/married)")
age_integer = int(age)
if age_integer <= 20:
    print("Teen")
if ask.lower() == "single":
      print("Single Adult")
else:
    print("Married Adult")
   """
# The fix:
age = input("What is your age?: ")
ask= input("Are you single or married?: ").lower()
age_tc = int(age)
if age_tc < 19: print("Teen")
elif age_tc >=20 and ask == "single":
    print("Single Adult")
else:
    print("Married Adult")

