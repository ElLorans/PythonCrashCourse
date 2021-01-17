# Readability and efficiency will be evaluated

# Realize a PhoneBook Programs that:
# Allows the user to insert new contacts and their numbers   (1 point)
# Allows the user to see all the contacts and their numbers (1 point)
# Allows the user to insert a contact and see the corresponding number (1 point)
# Allows the user to delete contacts                        (1 point)
# Warns the user if she is using the same number for a new contact (1 point)
# Warns the user if she is creating a new contact with the same name (1 point)
# the display phonebook functions shows the contacts by alphabetical order (1 point)
# the user can save the phonebook on a file (1 point)
# the user can load the phonebook from a file (1 point)

## Bonus:
# write the program using (almost) only using functions (2 points)
# write the program by creating a class PhoneBook


import json             # library that allows to load and save phonebook
# json allows to save and load objects from '.json' files


class PhoneBook:
    '''Provide basic PhoneBook functionalities.'''
    def __init__(self):             # __init__ function is run every time a new
        self.book = dict()          # instance of the class is created

    def add(self, name, num):
        '''Class method to save new contact.'''
        if name not in self.book:
            if num not in self.book.values():
                self.book[name] = num
            else:
                print('You already used this number')
                inp = input('Are you sure you want to use it again?')
                if 'y' in inp.lower():
                    self.book[name] = num
                else:
                    print('Contact has not been added')
        else:
            print("You can't have 2 contacts with the same name")
            inp = input("Do you want to overwrite old contact?")
            if 'y' in inp.lower():
                self.book[name] = num
            else:
                  print('Contact has not been added')
                  
    def show(self):
        '''Method to pretty print phonebook.'''
        print('\nYour PhoneBook:\n')
        print('-' * 20)
        for elem in sorted(self.book.items()):
            print(elem[0], ':', elem[1])
        print('-' * 20, '\n')

    def find(self, name):
        '''Method to provide contact number of input name.'''
        print(name, ':', self.book.get(name))

    def delete(self, name):
        del self.book[name]
        print(name, 'has been deleted')

    def save(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.book, file)
        print('\nYour phone book has been saved as a json file\n')

    def load(self, file_name):
        with open(file_name, 'r') as tool:
            self.book = json.load(tool)
        print('\nPhone book has been loaded\n')


def console(pb_class):
    '''Interact with PhoneBook class.'''
    
    inp = input('List of commands:\n \
[A]dd new Contact\n \
[D]elete Contact\n \
[F]ind Contact \n \
[P]rint PhoneBook\n \
[L]oad PhoneBook \n \
[Q]uit PhoneBook App\n \
[S]ave PhoneBook\n')
    
    inp = inp.lower()
    if 'a' in inp:
        name = input('Insert Contact Name')
        number = input('Insert Contact Number')
        pb_class.add(name, number)
        
    elif 'p' in inp:
        pb_class.show()
        
    elif 'f' in inp:
        look = input('What Contact are you looking for?')
        pb_class.find(look)
        
    elif 'd' in inp:
        erase = input('What contact do you want to eliminate?')
        pb_class.delete(erase)

    elif 'q' in inp:
        quit()

    elif 'l' in inp:
        file_name = input('Insert file name or file path')
        if '.json' not in file_name:
            file_name += '.json'
        pb_class.load(file_name)

    elif 's' in inp:
        file_name = input('Insert file name or file path')
        if '.json' not in file_name:
            file_name += '.json'
        pb_class.save(file_name)
        

phone = PhoneBook()                 # creates instance of PhoneBook class
print('Welcome to PhoneBook App!!\n\n')
while True:
    console(phone)                  # constantly calls console function
