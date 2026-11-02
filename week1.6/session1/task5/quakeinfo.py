# Week 1.6, Session 1: Task 5
from feed import QuakeFeed
from dataset import QuakeDataset

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like

# significance_level = input("Enter significance level: ")
# time_period = input("Enter time period: ")

myquakefeed = QuakeFeed("4.5", "week")

dataset = QuakeDataset(myquakefeed)

print(dataset)




