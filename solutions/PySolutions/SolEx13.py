# constantly ask the user for new names and phone numbers
# to add to the phone book, then save them

phone_book = {}

while True:
    name = input('Add Contact Name')
    num = input('Insert Contact Number')

    phone_book[name] = num
