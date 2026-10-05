# Week 1.2, Session 1: Task 5
rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Budapest"] = "Danube"
rivers["Cairo"] = "Nile"
print(rivers)
# Display all the keys
cities = rivers.keys()
print(cities)
# Display all the values
values = rivers.values()
print(values)
# Display all the key:value pairs, as tuples
pairs = rivers.items()
print(pairs)
# Delete an entry from the rivers database
rivers.pop("Liverpool")
print(rivers)