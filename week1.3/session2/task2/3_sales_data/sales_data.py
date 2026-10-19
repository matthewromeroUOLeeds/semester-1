# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

with open("sales.csv", "r") as infile:
    
    data = infile.readlines()
    lines = [line.strip().split(",") for line in data[1:]]

    largest_sale = 0
    largest_sale_day = []
    sale_sum = 0
    widget_sales = {
        "A":0,
        "B":0,
        "C":0,
        "D":0
    }

    for sale in lines:
        sale_amount = int(sale[2]) 
        sale_widget = sale[1]
        sale_sum+=sale_amount
        if sale_amount > largest_sale:
            largest_sale = sale_amount
            largest_sale_day = sale

        widget_sales[sale_widget[len(sale_widget) - 1]] += int(sale[3])
        
    average_sale = sale_sum / len(lines)

    print(largest_sale)
    print(largest_sale_day)
    print(average_sale)

    print(widget_sales)






# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows