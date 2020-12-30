##write a function that takes a nested list as an argument
##and returns a normal list
##show that the result is equal to flattened_list

nested_list = ['a', [2, 3], [4, 'b', [0, -2, ['c', 'e', '0f']]]]


flattened_list = ['a', 2, 3, 4, 'b', 0, -2, 'c', 'e', '0f']

def flat_list(nest_list):
