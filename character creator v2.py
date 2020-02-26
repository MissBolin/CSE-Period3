import random


def get_char_name():
    name = input("Enter your character name: ")
    return name

def get_char_age():
    age = int(input("Enter your character age: "))
    return age

def get_char_class():
    pass
    # on your own
    # return the class

# Generate 6 stats
def roll_a_d6():
    roll = random.randint(1, 6)
    print("You rolled a {}".format(roll))
    return roll

def roll_a_stat():
    roll1 = roll_a_d6()
    roll2 = roll_a_d6()
    roll3 = roll_a_d6()
    roll4 = roll_a_d6()
    stat_total = roll1 + roll2 + roll3 + roll4
    return stat_total

def display_character():
    pass


print(get_char_name())
print(get_char_age())
print(roll_a_d6())
print("strength = {}".format(roll_a_stat()))