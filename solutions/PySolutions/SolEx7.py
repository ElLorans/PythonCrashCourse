# ask the user to insert a word and two numbers x and y
# print the sentence from its xth element to its yth one
# bonus point: if the numbers are outside the word,
# first show the result, then ask the user to input the numbers again 

# EXAMPLE: word = python, x = 2, y = 5
# tho


word = input('Insert a word')
x = int(input('Insert the first number'))
y = int(input('Insert the second number'))

while True:
    
    print(word[x:y])

    length = len(word)              # stores how long is the word
    
    if abs(x) > length:             # also negative numbers can be slices
                                    # word[-1] would give 'n'
                                    # so we must check if:
                                    # -len(word)<x<len(word)

        print('The first number is outside the word')
        x = int(input('Insert the first number'))

    if abs(y) > length:
        print('The second number is outside the word')
        y = int(input('Insert the second number'))

    else:
        break
