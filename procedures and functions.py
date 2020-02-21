# Procedures are abstractions. We can create a blueprint of steps
# for common actions that we can reference and use as often
# as we wish.

# Step 1: Create the blueprint / define the procedure
def speak():
    print("Hello user!")
    print("From your PC")

# Step 2: Use the blueprint / call the procedure
speak()
speak()
speak()
speak()
speak()
speak()
speak()


def check_if_even(number):
    if number % 2 == 0:
        print("{} is even".format(number))
    else:
        print("{} is NOT even".format(number))


check_if_even(12)
check_if_even(3)


def multiply_together(num1, num2):
    answer = num1 * num2
    print("{} x {} = {}".format(num1, num2, answer))

multiply_together(5, 9)
multiply_together(1, 1)
multiply_together(-3, 7)
multiply_together(.5, 16)


def add_together(num1, num2, num3):
    total = num1 + num2 + num3
    print("{} + {} + {} = {}".format(num1, num2, num3, total))


add_together(2, 7, 4)
add_together(8, 6, 13)
add_together("a", "b", "c")


# Procedures are self-contained. They do not change the rest of the
# code AT ALL.
# Functions return data to the rest of the code.


def subtract(num1, num2):
    difference = num1 - num2
    return difference


answer = subtract(2, 4)
print(answer)
my_other_answer = subtract(answer, 9)
print(my_other_answer)
my_final_answer = subtract(my_other_answer, 21)
print(my_final_answer)



def give_me_five(number):
    result = number + 5
    return result


cash = give_me_five(0)
print(cash)
cash = give_me_five(cash)
print(cash)
cash = give_me_five(cash)
print(cash)

# print() is a procedure
# input() is a function

def find_volume_prism(length, width, height):
    volume = length * width * height
    if volume >= 0:
        return volume
    else:
        return 0
    print("No code is run after a return statement")

print(find_volume_prism(1, 1, 1))







