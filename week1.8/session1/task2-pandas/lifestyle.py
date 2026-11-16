import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
print(type(data))
#it is of type DataFrame

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.
# Find the total number of students
print(data["Study_Hours_Per_Day"].count())

# Find the mean average GPA of the students
print(data["GPA"].mean())

# Find the standard deviation of how much sleep students get per day
print(data["Sleep_Hours_Per_Day"].std())

# Find the maximum amount of study hours per day
print(data["Study_Hours_Per_Day"].max())

# Sort the students by social hours per day ascending (lowest -> highest)
data.sort_values("Social_Hours_Per_Day").to_csv("new_sorted_data.csv")


# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data["Total_hours"] = data["Study_Hours_Per_Day"] + data["Extracurricular_Hours_Per_Day"] + data["Sleep_Hours_Per_Day"] + data["Social_Hours_Per_Day"] + data["Physical_Activity_Hours_Per_Day"]


# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
import matplotlib.pyplot as plt




high_stress = data[data["Stress_Level"] == "High"]
low_stress = data[data["Stress_Level"] == "Low"]

mean_low_stress = low_stress["GPA"].mean()
mean_high_stress = high_stress["GPA"].mean()

print(mean_low_stress)
print(mean_high_stress)

plt.xlabel("Stress Level")
plt.ylabel("Mean GPA")
plt.title("Relationship between Stress Level and GPA")

plt.bar(["Low","High"], [mean_low_stress, mean_high_stress,])

plt.show()

print(high_stress)