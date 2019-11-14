"""
# My Class Notes

# Printing Strings
print("hello world")
print("This is a string")
print("123 abc .,")
print('check this')
# You can use apostrophes or quotes

# Printing Numbers
# Integers have no decimal place
print(7)
print(-10)
# floating point numbers HAVE a decimal place
print(3.14)
print(-10.)

# Printing Booleans
print(True)
print(False)

# This is a comment
"""
"""
This is a multi -
line comment and I 
can keep writing
on multiple lines
"""
"""

# Basic Math
print(8+3)
print(8-3)
print(8*3)  # shift + 8
print(8/3)

# Semi-advanced Math

# Exponents or Powers
print(2**3)  # 8
print(1**7)  # 1

# Floor Division
print(11//5)
print(51//10)

# Remainder After Division
# Also called 'MOD'
print(51 % 10)
print(77 % 25)

# Variables
# Store Data

my_number = 7
print(my_number)

name = "John Doe"
print("Welcome")
print(name)

food = False
print(food)

# Update variables
cost = 12
cost += 4  # Add 4
print(cost)


price = 10
price -= 3  # subtract 3
print(price)

price = 10
price *= 3  # Multiply 3
print(price)

price = 10
price /= 3  # Divide by 3. Return the float (decimal)
print(price)

# Writing a program
small = 12
middle = 15
large = 20
small = large - middle
large = large % small
middle = large + small
print(small)
print(middle)
print(large)

# Comparison Operators
# Result in a Boolean (T/F)

print(8 < 7)
print(8 < 8)
print(8 < 9)

print(8 <= 7)
print(8 <= 8)
print(9 >= 7)

print(8 == 8)  # Double equal signs means check if they are equal
print(8 != 9)  # != means not equal

# Manipulating String Cases
my_name = "sam"
my_name = my_name.upper()
color = "PURPLE"
color = color.lower()
state = "califORNIA"
state = state.title()
print(my_name, color, state)

# Concatenating (Joining) Strings
first = "Ms."
last = "Bolin"
full = first + last
sentence = "Welcome" + full + "to CSE!"
print(sentence)

# Taking User Input as a String
name = input("Enter your name: ")
print(type(name))
print(name)

age = input("Enter your age: ")
print(type(age))
age = int(age)
print(type(age))
print(age)

# String formatting
# places the values of the variables at the end into each curly bracket {} in order
print("Welcome {}!".format(name))
print("Welcome {}! You are {} years old!".format(name, age))
"""
# Typecasting
# means turning data into different types
# like strings or integers

value = int(input("Enter a number: "))
cost = 12
print(value+cost)

print("7" + "5")
print(str(7) + str(6))
print(7+5)
