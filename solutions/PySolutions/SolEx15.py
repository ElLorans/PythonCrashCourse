##Write a function which can compute the factorial of a given numbers.
##Suppose the following input is supplied to the program:
##8
##Then, the output should be:
##40320

def my_factorial(number):
    if number < 0:
        return 'factorial is defined only for non-negative integer numbers'
    
    res = 1
    while number > 0:
        res *= number
        number -= 1

    return res

inp = input('Insert a number')
print('The factorial of', inp, 'is:', my_factorial(int(inp)))

