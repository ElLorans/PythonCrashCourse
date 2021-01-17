# ask the user for a base x and an exponent e
# (suppose only integers are provided)
# show on the screen the result

## SOLUTION:   (will crash if inputs are not provided correctly)
x = input('Insert a base x')
e = input('Insert an exponent e')
base = int(x)                       # inputs are string, so we need to convert
exponent = int(e)                   # them to int
print(base, '^', exponent, '=', base**exponent)



## SOLUTION BONUS (checks if inputs are provided correctly):

x = input('Insert a base x')
e = input('Insert an exponent e')
try:                                # we try to execute the indented block
    base = int(x)                   # if we have an error, we will execute                  
    exponent = int(e)               # the indented block AFTER 'except'               
    print(base, '^', exponent, '=', base**exponent)

##except:                           # NEVER USE 'BARE' except
except ValueError:                  # specify the error you are looking for
                                    # in this case, 'ValueError'
    print('Only integers are allowed')
