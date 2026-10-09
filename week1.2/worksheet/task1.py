# Worksheet 1.2: Task 1 Solution
import sys

grade = input("Enter integer grade from 0 to 100: ")

if grade.isdecimal() and int(grade) >= 0 and int(grade) <= 100:
    if int(grade) <= 100 and int(grade) >= 70:
        print(f"{grade} is a Distinction")
    elif int(grade) <= 69 and int(grade) >= 40:
            print(f"{grade} is a Pass")
    elif int(grade) <= 39 and int(grade) >= 0:
            print(f"{grade} is a Fail")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")

