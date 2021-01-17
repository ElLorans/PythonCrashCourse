##write a function sum_dict() that takes a dictionary as an argument
##and returns the sum of the keys
##bonus point: sum only floats and ints, without errors for other data types

##write a function merge_dict() that merges two dicts

def sum_dict(dictionary):
    summa = 0
    for key in dictionary.keys():
        if type(key) is int or type(key) is float:
            summa += key

    return summa


def merge_dict(dict1, dict2):
    # if by merge we mean update:
    dict1.update(dict2)
    return dict1


# TEST:

diction = {1: 'a', 2: 'b', 'c': 3}
print(sum_dict(diction))

diction2 = {'c': 4, 'd': 5}
print(merge_dict(diction, diction2))
