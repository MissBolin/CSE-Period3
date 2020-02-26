import random


def get_char_name():
    name = input("Enter your character name: ")
    return name


def get_char_age():
    age = int(input("Enter your character age: "))
    return age


def get_char_class():
    pass
    # Will do this later


def roll_d6():
    roll = random.randint(1, 6)
    print("You rolled a {}".format(roll))
    return roll



print(get_char_name())
print(get_char_age())







