# Worksheet 1.2: Task 2 Solution

from util import read_numbers
import sys

numbers = read_numbers()

print(numbers)

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

else:
    minimum = min(numbers)
    maximum = max(numbers)

    mean = sum(numbers) / len(numbers)

    median_index = len(numbers) // 2
    numbers.sort()
    if len(numbers) % 2:
        median = numbers[median_index]
    else:
        median = (numbers[median_index] + numbers[median_index - 1]) / 2


    print(f"Minimum = {minimum}")
    print(f"Maximum = {maximum}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")



