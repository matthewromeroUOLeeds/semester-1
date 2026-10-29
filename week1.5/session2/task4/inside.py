# Week 1.5, Session 2: Task 4
from geometry import Point, Circle
# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class


point = Point(0, 3)

circle = Circle(3)

if point in circle:
    print("point is inside circle")
else:
    print("point is outside circle")