# List Less Than Ten
# list numbers elements if conditional

# Lists
# More conditionals (if statements)

# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that
# are less than 5.

# Extras:
# 1. Instead of printing the elements one by one, make a new list that
#    has all the elements less than 5 from this list in it and print
#    out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only 
#    elements from the original list a that are smaller than that
#    number given the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

print a[0:5]

for x in a:
	if x <= 5:
		b.append(x)

print b	

y = raw_input('Please enter a number: ')
y = int(y)

for z in a: 
	if z <= y: 
		c.append(z)

print c
