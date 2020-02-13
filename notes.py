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

# Typecasting
# means turning data into different types
# like strings or integers
# Note: we can only + the same data types together

value = int(input("Enter a number: "))  # int casts the input into an integer data type
cost = 12
print(value+cost)

print("7" + "5")  # If you + strings, you write them next to each other, as in 75
print(str(7) + str(6))  # str() means cast into a string data type
                        # This yields 76, because we are adding strings
print(7+5)  # If you + integers, we add them together to get 12


# Escape Characters
# Change Automatic Formatting

sent = "This is my sentence."
print(sent)
sent = "This \nis my sentence."
print(sent)
sent = "This \tis my sentence."
print(sent)
mysentence = "She said \"yes!\""
print(mysentence)
mysentence = 'She said \'yes!\''
print(mysentence)
sent3 = "Jack's dog"
sent4 = 'my "dog"'


# Making Decisions
grade = int(input("Enter your percentage: "))
if grade > 70:
    print("You passed!")

grade = int(input("Enter your percentage: "))
if grade >= 70:
    print("You passed!")
else:
    print("you failed oh no!")

grade = int(input("Enter your percentage: "))
if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
else:
    print("you failed oh no!")


# For Loops

for i in range(3):
    print("hello!")

for i in range(100):
    print("bruh")

for i in range(1000):
    print(12)

for i in range(10):
    print("hello")
    print(6)

for i in range(10):
    print(i)

for j in range(2, 10):
    print(j)

for count in range(13, 25):
    print(count)

for value in range(17, 50):
    print(value)

for i in range(1, 11, 2):
    print(i)

for item in range(4, 20, 3):
    print(item)

for i in range(50, 10, -1):
    print(i)



# Advanced For Loops
counter = 0
for i in range(1, 101):
    counter = counter + i
print(counter)

# Factorial
factorial = 1
for i in range(1, 21):
    factorial = factorial * i
    print(factorial)

# Checking Divisibility
for i in range(100):
    if i % 2 == 0:
        print(i)

for i in range(100):
    if i % 3 == 0:
        print(i)

for i in range(1800, 1901):
    if i % 5 == 0:
        print(i)

# Counting Instances
count = 0
for i in range(100):
    if i % 2 == 0:
        print(i)
        count = count + 1
print(count)

count2 = 0
count3 = 0
for i in range(100):
    if i % 2 == 0:
        print("{} is divisible by 2".format(i))
        count2 = count2 + 1
    if i % 3 == 0:
        print("{} is divisible by 3".format(i))
        count3 = count3 + 1
    if i % 6 == 0:
        print("{} is divisible by 6".format(i))
    print("-----------------------------------------")
print("{} numbers were divisible by 2".format(count2))
print("{} numbers were divisible by 3".format(count3))
"""

# While Loops

value = 0
while value != 10:
    print("value is currently {}".format(value))
    value = value + 1
    print("The new value is {}".format(value))

count = 201
while count > 0:
    print("count is currently {}".format(count))
    count = count - 1
    print("The new count is {}".format(count))

name = input("Enter your name: ")
print(len(name))
while len(name) < 2:
    print("Your full name")
    name = input("Enter your name: ")
print("Welcome {}!".format(name))

sport = input("Guess my favorite sport")
while sport != "wrestling":
    if sport == "basketball":
        print("We don't play with a ball.")
    elif sport == "soccer":
        print("Indoors")
    elif sport == "baseball":
        print("We don't use a bat.")
    else:
        print("Try again")
    sport = input("Guess my favorite sport")
print("Yay, you got it!")

# Change this code to be YOUR game rather than mine.
# Change the answer to be YOUR fav sport, and add in 3 more
# special hints


