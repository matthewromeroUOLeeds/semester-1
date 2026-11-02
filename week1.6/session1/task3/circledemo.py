# Week 1.6, Session 1: Task 3
from shapes import Circle
from point import Point
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

circle = Circle(5, Point(0,0))

print(circle.area())
print(circle.perimeter())

circle.set_radius(10)
print(circle.area())

print(circle)


