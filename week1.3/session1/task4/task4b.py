# Week 1.3, Session 1: Task 4b



# create a for loop and use range to print the list of numbers 
# between 3 and 50 that are divisible by 3
list_of_multiples = []

for i in range(3,51):
    if i % 3 == 0:
        list_of_multiples.append(i)

print(list_of_multiples)