# count how many even numbers in lista
# bonus point: ask the user to insert the lista he wants
lista = [1, 0, 5, 'a']

inp = input('Insert a list of elem separated by "|" WITHOUT space')

liste = inp.split('|')              # .split('x') creates a list separating
                                    # every time it finds 'x'

evens = 0
for elem in liste:
    try:
        num = int(elem)             # inputs are strings, so check if it is a
                                    # number
        if num % 2 == 0:
            evens += 1
    except:
        pass                        # pass does nothing, but prevents error
                                    # because Python expects something after
                                    # except


print('You inserted', evens, 'even numbers')
