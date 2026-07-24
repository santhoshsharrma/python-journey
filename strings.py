# Strings
'''
Text is a string data type. we can know if a text is a string when the text is in between single,double or triple quotes.
to check the length of string -> len()
'''
letter = 'p'
print(letter)
# length 
print(len(letter))

greetings = "Namaste People, This is my journey!"
print(greetings)
print(len(greetings))

# Multiline Strings:
''' The multiline strings works just as multiline comments in python. we either use single/double quotes'''
random_var = '''Hello people
Today, the weather is beautiful.'''
print(random_var)

# String concatenation
'''
String concatenation means we merge/connect two string variables into a single string
'''
ex1 = "hello"
ex2 = "world"
space = ' '
final = ex1 + space + ex2
print(final)

firstName = "Max"
lastName = "Verstappen"
fullName = firstName + space + lastName
print(fullName)

# Escape Sequences
'''
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
'''


print("One of my favourite philosophies include \"Buddhism\"")

print("Buddhism is one of the major religions on Earth.\nDid you know about this?")
print('Days\tTopics\tExercises')
print('Day 1\t3\t2')
print('Day 2\t1\t4')
print('Day 3\t6\t5')
print('Day 4\t2\t9')

# String formatting

first_name = 'Ahura'
last_name = 'Mazda'
countryOrigin = 'Persia'

about = '{} {} was the first Monotheistic God who was worshipped in Ancient {}'.format(first_name,last_name,countryOrigin)
print(about)

'''
We can even Perform Arithmetic Operators
'''
a, b = 10,12

print('{} + {} = {}'.format(a,b, a + b))
print('{} - {} = {}'.format(a,b, a - b))
print('{} * {} = {}'.format(a,b, a * b))
print('{} / {} = {}'.format(a,b, a / b))
print('{} % {} = {}'.format(a,b, a % b))


'''
fstrings are used in modern way because we dont have to rely on old ways such as .format or Concatenation
String interpolation (like Python f-strings) is needed because it makes embedding variables directly inside strings.
This makes it clean, readable, and efficient.

Concatenation: "Hello, " + name + "!"
.format()    : "Hello, {}!".format(name) (less readable for complex expressions)
% formatting : "Hello, %s!" % name (outdated, error-prone)
f-strings    : print(f"Hello {name}!")
'''
num1 = 12
num2 = 22

print(f'{num1} + {num2} = {num1+num2}')
print(f"{num1} - {num2} = {num1 + num2}")

name = 'Alice'
age = 18

print(f"{name} is {age} years old.")
# old way
print(name + " is " + str(age) + " years old.")

# Python Strings as Sequences of Characters

# Character unpacking
country = 'Argentina'
a,b,c,d,e,f,g,h,i = country
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

'''if you want them as A r g e n t i n a -> use end = ' '  '''

# Accessing Characters in Strings by Index
# In programming, counting begins from 0. for ex: in the word Python, the first 0th index is P.

example = 'LangChain'
index1 = example[0]
index2 = example[1]
index3 = example[-1] # first index from right side
print(index1)
print(index2)
print(index3)

# Slicing Python Strings

'''
# Suppose we need to print first 3 alphabets or last three or all.
The Logic: [start:stop:step]

'''
language = 'Rust Programming'
print(language[0:3]) # first three
print(language[0:]) # all
print(language[-3:]) # last three

# Reversing a String

print(language[::-1])
'''
Here, start works in such a way when step is postive, it starts from beginning. else if negative, starts from the end.
1: move forward one by one
-1: move from backward one by one
'''
print(language[::1])
print(language[0:5:2])
print(language[0::2]) # Rs rgamn
