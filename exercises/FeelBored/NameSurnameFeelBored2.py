# You decided to create a web hosted dashboard with all the stocks bought every week.
# Each trader can access the dashboard through the web and insert his purchases
# You must transform their data into dictionaries.
# You learn the hard way that strings obtained through a form end with \r rather than with \n

# expected output:
# get_dict(data) = {'Apple': 10, 'Samsung': 20}



data = '''10 Apple\r
20 Samsung'''

# You learn the hard way that users never read the instructions, too.

data_2 = '''Apple 70
Ferrari 30
PetroBrazil 12
Super Stock 5'''

# And that some trader save their records separating them with a tab, so
# when they copy it on the dashboard, you get:

data_3 = '''Apple\t25
Tesla\t12
Ferrero\t50
No fantasy anymore\t20'''

data_4 = '''12\t I do not know
5 what to invent
7\t to make it harder'''


# Your code must never crash, take into account every possible scenario, and always work.
# If it really cannot work, it must warn the user and explain how to insert his data,
# clearly pointing out the error.

def get_dict(stringa):

