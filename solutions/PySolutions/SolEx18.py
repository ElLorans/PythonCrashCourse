##write a function that takes a nested list as an argument
##and returns a normal list
##show that the result is equal to flattened_list

nested_list = ['a', [2, 3], [4, 'b', [0, -2, ['c', 'e', '0f']]]]


flattened_list = ['a', 2, 3, 4, 'b', 0, -2, 'c', 'e', '0f']

def flat_list(nest_list):
    flat = list()
    for elem in nest_list:
        if type(elem) is list:              # we check if elem is a list
            
            flat += flat_list(elem)         # recursive function!
                                            # this is a function that calls
                                            # itself in a loop, until a case is
                                            # simple enough to be processed
                                            # directly!
        else:
            # if elem is not a list, we append it to 'flat'
            flat.append(elem)
            
    return flat

res = flat_list(nested_list)
print(res==flattened_list)
