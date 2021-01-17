# sum all the negative numbers in lista
lista = [-1, 0, 5, 'a', -7, -2]


summa = 0
for elem in lista:
    if type(elem) is int and elem < 0:
        summa += elem

print('the sum of negative numbers is:', summa)
        
