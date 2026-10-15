"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Matthew Romero
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"



# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14
red_count = 0
red_amber_count = 0
green_count = 0
amber_count = 0


for systime in range(0, maxtime + 1):
    

    if state == "red" and red_count < 4:
        amber_count = 0
        print(f"Time {systime:03} State {state}")
        red_count += 1
        if red_count == 4:
            state = "red_amber"
            

    elif state == "red_amber" and red_amber_count < 3:
        red_count = 0
        print(f"Time {systime:03} State {state}")
        red_amber_count += 1
        if red_amber_count == 3:
            state = "green"

    elif state == "green" and green_count < 5:
        red_amber_count = 0
        print(f"Time {systime:03} State {state}")
        green_count += 1
        if green_count == 5:
            state = "amber"

    elif state == "amber" and amber_count < 3:
        green_count = 0
        print(f"Time {systime:03} State {state}")
        amber_count += 1
        if amber_count == 3:
            state = "red"






