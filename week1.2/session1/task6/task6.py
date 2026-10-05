# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music = {
    "ed sheeran" : [
        {
            "name" : "plus", 
            "date" : 2017
        }, 
        {
            "name" : "multiply", 
            "date" : 2019
        }, 
        {
            "name" : "divide", 
            "date" : 2021
        }
    ],
    "bad bunny" : [
        {
            "name" : "Un verano sin ti", 
            "date" : 2023
        }, 
        {
            "name" : "YHLQMDLG", 
            "date" : 2020
        }, 
        {
            "name" : "Debi tirar mas fotos",
            "date" : 2025
        }
    ]
}
# Pretty-print the data structure




# Display details of one album recorded by a specific artist

album_count = 0
for albums in music.values():
    album_count+=len(albums)

print(album_count)






