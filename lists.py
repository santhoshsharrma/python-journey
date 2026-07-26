# Lists
# List is a collection that is ordered and changeable,  it allows duplicate members.
sea_countries = ['Malaysia','Singapore','Thailand','Vietnam','Indonesia']
countries_SA = ['India','Pakistan','Sri Lanka','Nepal']

asia = countries_SA + sea_countries
continent = ', '.join(asia)
 
print(f'Asia is the largest continent on Earth. \nThe countries such as - {continent} are part of Asia')
print('Number of countries i listed are: ',len(asia))

# List allows different data types

aboutMe = ['Max',20, {'country':'India'}]
print(aboutMe)

# Accessing List items using positive indexing
indexing = aboutMe[0]
print(indexing) #Max

# Accessing List items using negative indexing
neg_indexing = aboutMe[-2]
print(neg_indexing) #20

# Unpacking List Items
europe = ['Germany',250,'Poland',1.09,'Greece',True]

first_index, int_index, string_index, float_index, vacation, boolean_index = europe

print(first_index)
print(int_index)
print(string_index)
print(float_index)
print(vacation)
print(boolean_index)

# *rest prints all the rest items

exampler = ['Python','Java','Rust','Golang','Javascript','Ruby']
lang1,lang2,lang3,*rest = exampler
print(lang1)
print(lang2)
print(lang3)
print(', '.join(rest)) 

# Modifying Lists

exampler = ['Python','Java','Rust','Golang','Javascript','Ruby']
exampler[0] = 'C'
print(exampler)

exampler[-1] = 'C++'
print(exampler)

# Checking Items in List

fruits = ['Banana','Apple','Grapes']
check_fruits = 'Grapes' in fruits
print(check_fruits)

# Adding Items to list

fruits.append('Orange')
print(fruits)

# This adds the item to the end of the list. i.e; -1

# Inserting Items to list
fruits.insert(4, 'Blueberry')
print(fruits)

# Removing Items from a List
'''
There are two ways 
1) .remove()
2) .pop()
3) del var[index]
'''

fruits.remove('Blueberry')
print(fruits)

fruits.pop() # removes the last item in a list
print(fruits)

fruits = ['Banana','Apple','Grapes','Orange','Strawberry']
del fruits[0]
print(fruits)

# to remove all, just use del fruits

# Clearing List Items

blahblah = ['a','b','c']
blahblah.clear()
print(blahblah)

# Copying a List

blahblah = ['a','b','c']
copy = blahblah.copy()
print(copy)

# Joining Lists -> similar to string concatenation

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)

# Reversing a list
music = ['Pop','Bass','Jazz']
music.reverse()
print(music)

# Sorting List Items

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)          # Sorted in alphabetical order

# To print rever, just use fruits.reverse()

# to print without modifying the list

veg = ['Carrot','Beetroot','Chickpea']
print(sorted(veg))

# Practise Exercises from 30-days-of-python github repo
empty = []
print(empty)

# Declare a list with more than 5 items
empty = ['Banana',205,'Germany','France','New York','Python']
print(empty)

# Find the length of your list
print(len(empty))

# Get the first item, the middle item and the last item of the list
first_item = empty[0]
second_item = empty[1]
last_item = empty[-1]
print(first_item)
print(second_item)
print(last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Max',20,180,'single','Earth']
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company

print(it_companies[0],it_companies[1],it_companies[-1])

# Print the list after modifying one of the companies

it_companies[0] = 'Tesla'
print(it_companies)

# Add an IT company to it_companies

it_companies.append('Facebook')
print(it_companies)

# Insert an IT company in the middle of the companies list

it_companies.insert(4, 'Telegram')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[0] = "TESLA"
print(it_companies)

# Join the it_companies with a string '#;  '

print(' #'.join(it_companies))

# Check if a certain company exists in the it_companies list.

check_company = 'Google' in it_companies
print(check_company)

# Sort the list using sort() method

it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
it_companies.sort()
print(it_companies)
slice_comp = it_companies[:3]
print(slice_comp)

# Slice out the last 3 companies from the list
slice_comp = it_companies[-3:]
print(slice_comp)

# Remove the first IT company from the list

del it_companies[0]
print(it_companies)