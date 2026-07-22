# Loops
# Loops are used when we need to execute a block of code repeatedly until the conditions are met.

# For loop
num = 4
for i in range(0,num):
    print(i)

# While loop runs as long as condition is true. once failed, it exits the loop

num = 0
while (num<3):
    num += 1
    print("Welcome to my journey ")    
    
# Nested loops
# the end = ' ' is used when we need to print something on the same line and ' ' has a space.
# for example
print("A", end = ' ')
print("B")
# This prints A B. not AB or B in the next line under A.

for i in range(1,5):
    for j in range(i):
        print(i, end = ' ')
    print()
    
'''
suppose inner loop is 3 times. the inner loop runs 3 times and end = ' ' prevents to start a new line.
so 3 3 3 stay in a single line. once i = 3 is satisfied, it moves to print() which moves to new line. 
since outer loop still runs acc to range, it moves to i = 4 and prints 4 4 4 4.

Inner loop controls how many numbers appear in a row.
end controls whether they stay on that row.
print() creates the next row → outer loop starts the next iteration.

The output prints 
1
2 2 
3 3 3 
4 4 4 4

the process:
i = 1 -> inner loop → print -> new line
i = 2 -> inner loop → print -> new line
i = 3 -> inner loop → print -> new line
i = 4 -> inner loop → print -> new line -> end
'''

for i in range(1,5):
    for j in range(5):
        print(i, end = ' ')
    print()

# this prints each line 5 times.

for i in range(1,5):
    for j in range(5):
        print(j, end = ' ')
    print()
    
'''
We find something interesting here, because now i tried to print j.
Since we already defined the range of i, which is from 1 -> 4, there is no defined range for j.
So it begins from 0 and ends with 4, because we know the final range to be 5.
and since we didn't use range(i) inside the inner loop, it prints 5 times.

Output would be:
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
'''

for i in range(1,5):
    for j in range(i):
        print(j, end = ' ')
    print()
    
'''

If we had used range(i) inside the inner loop, it would print this:
0
0 1
0 1 2
0 1 2 3 

why? because inside the inner loop, when i = 1, range(i) becomes range(1) so j prints a digit before 1.
and when i = 4, j treats it as range(4) thus printing before 4.


Now, if we wanted to also print 4 without increasing the range to range(6), we just can do range(i + 1)
'''
for i in range(1,5):
    for j in range(i + 1):
        print(j, end = ' ')
    print()
    
'''
This prints:
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

'''

x = 0
while(x < 100):
    x += 2
print(x)

# since 0+2=2 and it always gives us an even number, the nearest even number to 100 is 98. 98+2 = 100.
# x = 100
