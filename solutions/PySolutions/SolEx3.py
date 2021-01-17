# generate a number from 1 to 10 (bonus point if the number is random)
# ask the user to guess a number from 1 to 10
# if the number is wrong, ask again
# if the input is not a number, ask again for an input
# if the input is correct, show "YOU W0N AFTER x ATTEMPTS", where x
# is the number of guesses


import random
ans = random.randint(1,10)              # we create a random number from 1 to 10
count = 1                               # auxiliary variable to count # attempts

while True:
    inp = input('Guess a number from 1 to 10')
    if inp.isdigit():
        if int(inp) == ans:
            print('YOU WON AFTER', count, 'ATTEMPTS')
            break
        else:
            print('The right answer is another one...\nTry again\n')
            count += 1
    else:
        ('Only integers are accepted, try again')
    
    
