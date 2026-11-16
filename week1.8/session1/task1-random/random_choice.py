import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

number = input("Enter a number:")
int_number = int(number)

if int_number > 1000:
    raise ValueError("There are only 1000 unique names in the list")
chosen = random.sample(names, k=int_number)
# Display the chosen names, one per line

for i in chosen:
    print(i)