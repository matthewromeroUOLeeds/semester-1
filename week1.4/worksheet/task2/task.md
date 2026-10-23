Task 2 – Portfolio task
Create a function named currency_converter that converts between four different currencies. The
function should accept three arguments:
1. amount: A number representing the monetary value to be converted. It can be an integer or a
floating-point number, and it must always be non-negative.
2. from_currency: A string representing the currency code of the original currency. The supported
currency codes are:
• 'GBP' (British Pound)
• 'CNY' (Chinese Yuan)
• 'PHP' (Philippine Peso)
• 'INR' (Indian Rupee)
3. to_currency: A string representing the currency code to which the amount should be converted.
The possible values for this argument are the same as for from_currency.
Expected Behavior:
• The function should return the converted amount as a floating-point number, rounded to two
decimal point precision using Python's round() function.
• If the input amount is negative, the function should return 0.0.
• You do not need to handle cases where non-numeric values are passed in.
• You do not need to handle cases for undefined currency codes.
The conversion rates are stored in the following dictionary structure:
conversion_rate = {
'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
}
The numbers in the inner dictionary are the conversion rates. For example, the conversion rate from
GBP to CNY is 9.24. Therefore, 101 GBP will be converted to 933.24 CNY.
A template file currency_converter.py is provided and you are to write your function in this file.
Please do not change the file name. When submitting your file, make sure there are no additional
function calls to test the function, or code to get user input. Only a file with the function definition
is required. The autograder on Gradescope will run tests and provide feedback on passed and failed
tests.
You must pass all tests on Gradescope to complete the task.