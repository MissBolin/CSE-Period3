# Tax Calculator

cost = float(input("What is the cost of this item? "))
state = input("What state? ")

tax = 0

if state == "CA":
    tax = cost * .08

print("Your item costs ${:.2f}, with ${:.2f} in tax.".format(cost+tax, tax))
