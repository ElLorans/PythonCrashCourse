##write a function that takes a string and a name as arguments
##and creates a file name.txt with the given string

def write(string, name):
    with open(name, 'w') as file:   # ALWAYS use the with method to open a file

                  # 'w' stands for 'writing mode'
        file.write(string)
    # here we used a VOID function (no return)

fl = input('Insert file name or file path + name')
text = input('Insert text you want to write')

if '.' not in fl:      # it's better to have a file extension
                       # so we check if it is present. If not, we add it
    fl += '.txt'          

write(text, fl)

# for instance, if user insert 'a' and 'Hello world' this program will create a
# file named 'a.txt' in the same folder with written 'Hello world'
