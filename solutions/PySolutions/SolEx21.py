##write a function that takes 2 arguments, a list and a number,
##and returns a tuple with all the possible combination of
##len == number in ascending order.

## Example:
## lista = [1, 2, 3]
## all_rng(lista, 2) 
## should give as output:
## ([1, 2], [2, 3], [1, 3])


#SOLUTION
import itertools                

def all_rng(lista, num):
    res = list()
    for elem in itertools.combinations(lista, num):
        # itertools.combinations is a generator (like range) with all
        # combinations
        res.append(list(elem))
    return tuple(res)

listb = [1, 2, 3, 4, 5, 6]

print(all_rng(listb, 3))
