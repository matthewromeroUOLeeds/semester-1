"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Matthew Romero
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
    amount = int(input("How much do you want to save every month?: "))
except: 
    print("Invalid Input type. Must be integer")



# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

yearly_amount = amount * 12
print("Amount saved yearly without interest: £", yearly_amount)

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

total_amount = yearly_amount * 1.008

#Taken from stack overflow: https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros
print("Amount saved yearly with interest: £", "%.2f" % round(total_amount, 2))