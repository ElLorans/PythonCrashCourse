##The Fibonacci Sequence is computed based on the following formula:
##f(n)=0 if n=0
##f(n)=1 if n=1
##f(n)=f(n-1)+f(n-2) if n>1
##
##Please write a function returning the Fibonacci
##Sequence in comma separated form

##Example:
##fibonacci(7)
##The output of the program should be:
##0,1,1,2,3,5,8,13



def fibonacci(num):
    if num < 0:
        return 'Only positive integers are allowed'
    elif num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    
    else:
        fib_seq = [0, 1]
        count = 2
        while count <= num:
            last = fib_seq[count - 1] + fib_seq[count - 2]
            fib_seq.append(last)
            count += 1
        return fib_seq
        

inp = input('Insert a number')
print('\nThe first', inp, 'numbers of the Fibonacci Sequence are:\n')
print(fibonacci(int(inp)))
