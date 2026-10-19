# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
info = []
name = input("Enter Name: ")
info.append(name.lower())
age = int(input("Enter Age: "))
info.append(age)
colour = input("Enter Favourite Colour: ")
info.append(colour.lower())



print(info)

with open("user_info.txt", "a") as infile:
    for entry in info:
        infile.write(f"{entry} \n")



# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
