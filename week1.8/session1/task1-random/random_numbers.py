import random

# Get user to input how many random numbers they want
amount = int(input("Enter how many numbers you want: "))

# Generate this many random numbers

random_numbers = [f"{str(random.randint(0,100))}\n" for i in range(amount)]

# Write the random numbers to a file named random.txt, one number per line

with open ("random.txt", "w") as infile:
    infile.writelines(random_numbers)

