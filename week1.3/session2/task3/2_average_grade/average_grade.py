# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

with open("student_data.csv", "r") as infile:
    data = infile.readlines()


    data = [entry.strip().split(",") for entry in data[1:]]

    for entry in data:
        name = entry[1]
        grades = [int(entry[2]), int(entry[3]), int(entry[4])]
        average_grade = f"{sum(grades) / 3 :.2f}"

        with open(f"report{entry[0]}.txt", "w") as infile:
            infile.writelines([f"Name: {name} \n", f"Average Grade: {average_grade} \n"])



# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
