# ask the user for an input
# if the input is a number, show on the screen if it is odd or even
# if the input is not a number, ask again for an input

while True:                         # indented block is executed infinite times
    inp = input('Insert a number')
    try:
        num = int(inp)              # inputs are strings, we need to convert!

        if num % 2 == 0:            # we check the remainder of num/2.
            print(inp, 'is even')   # If it is =0, it's an even number!
        elif num % 2 != 0:
            print(inp, 'is odd')
        break                       # we break the loop (will work only if inp
                                    # is an integer)
    except ValueError:
        print('Only integers are accepted, try again')


# we could also use .isdigit() rather than try except,
# because we are looking only for integers.


# here's the code with .isdigit():

print('\nHere is the code with .isdigit() in place of try except:\n')

while True:                         # indented block is executed infinite times
    inp = input('Insert a number')

    if inp.isdigit():               # we check if input is only made of digits
        
        num = int(inp)              # inputs are strings, we need to convert!

        if num % 2 == 0:            # we check the remainder of num/2.
            print(inp, 'is even')   # If it is =0, it's an even number!
        elif num % 2 != 0:
            print(inp, 'is odd')
        break                       # we break the loop (will work only if inp
                                    # is an integer)
    else:
        print('Only integers are accepted, try again')
