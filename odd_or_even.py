# Odd Or Even
# Input if types of int equality comparison numbers mod

# Modular arithmetic (the modulus operator)
# Conditionals (if statements)
# Checking equality

# Get user input

a = raw_input('What number do you wish to evaluate: ')

# convert a into an integer

a1 = int(a)

# do the arithmatic

a2 = a1 % 2

# check the condition of even or odd

if a2 == 1:
	print("The number you entered is odd.")
elif a2 == 0:
	print("The number you entered is even.")
else:
	print("Please enter a whole number.")

# do more arithmatic

a2 = a1 % 4

# check another conditional

if a2 == 0:
	print("It is a multiple of the number four.")
else:
	print("")

# get user input for another number

b = raw_input('Please enter a number that is not zero: ')

# convert raw input to an integer

b1 = int(b)

# yet another conditional

if a1 % b1 == 0:
	print('This number divides evently into the first number.')
else:
	print('These two numbers do not divide equally into eachother.')