# count how many words of 5 letters in lista
lista=['Hey','there','those','are','some','words']

words = 0
for elem in lista:
    if len(elem) == 5:
        words += 1

print('There are', words, 'words of 5 letters')
