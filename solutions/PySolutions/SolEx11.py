# sum all numbers in lista until the first even (included)
lista=[1, 5, -2, 'Hey', 4, 3, 7]

summa = 0
for elem in lista:
    if type(elem) is int:
        summa += elem
        if elem % 2 == 0:
            break

print('The sum until the first even included is:', summa)
