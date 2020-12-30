# Your Boss wants an analysis of a large and complex dataset, but you have so
# many columns and rows that Excel is slow and crashes every 5 minutes.
# Since you know a little bit of Python, you copy the dataset on a .py file (this file)
# and you write "file =" on the first line.
# Now you need to assign to each column heading its own values.


# You have a multiple lines string. The first line is the heading.
# create a dictionary whith each heading as a key
# and a list with the corresponding column as a value
# The result you should obtain is:
# {'Stock': ['Apple', 'Tesla'], 'Close': ['188.72', '278.62'], 'Beta': ['0.2', '0.5'], 'Cap': ['895.667B', '48.338B']}
# {'Employee': ['Linda', 'Bob', 'Joshua'], 'Wage':  [3000, 2000, 800], Hired: ['2017', '2016', '2019'], Promotion: ['Yes', 'No', 'Yes']}

# your code should work for both the examples provided and for any other multilines
# strings, disregarding their length.

file = """Stock Close Beta Cap
Apple 188.72 0.2 895.667B
Tesla 278.62 0.5 48.338B"""


file_2 = """Employee Wage Hired Promotion
Linda 3000 2017 Yes
Bob 2000 2016 No
Joshua 800 2019 Yes"""
