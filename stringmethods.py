# String Methods
# String Methods are used to format strings.

# 1) capitalize() - This converts the first character of the string to capital letter
journey = "my journey will succeed"
print(journey.capitalize())

name = input("Enter your name: ")
print(f"Hello, {name.capitalize()}!")


# 2) .count() -> This method is used to return the count of the desired input

print(journey.count('c')) #2
print(journey.count('e')) #3
print(journey.count('e',4,10)) #1

# 3) .endswitch() -> checks if the string ends with a specified ending

print(journey.endswith('ed')) # True
print(journey.endswith('am')) # False

# 4) .find() -> retruns the index of the string in the specified input in it. if not, returns -1
print(journey.find('M')) #-1 because M does not exist
print(journey.find('y')) #1 because y exist on index 1

# 5) rfind() -> Returns the index of the last occurrence of a substring, if not found returns -1

print(journey.rfind('cc'))

# 6) index(): Returns the lowest index of a substring.
# additional arguments indicate starting and ending index (default 0 and string length - 1). 
# If the substring is not found it raises a valueError.

sub_string = 'll'
print(journey.index(sub_string))

sub_stringOne = 'ab'
# print(journey.index(sub_stringOne)) -> Value Error

# 7) isalnum() -> Checks alphanumeric character, does not count space

exampleOne = 'My name is Luna'

