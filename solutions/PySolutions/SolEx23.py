##write a function that takes the filepath of a .txt as an argument
##and returns a dictionary with each word as keys and the number of times
##they are repeated as values.
##the dictionary must be sorted by value in descending order.
##the function MUST NOT be case sensitive.
##you can use harrypotter.txt for testing

def parse(filepath):
    with open(filepath) as file:
##    with open(filepath, 'r') as file:             # another way to write it
                        # 'r' stands for 'read mode'
        text = file.read()

    text = text.lower()                 # now everything is lowercase
                                        # so case unsensitive

    words = text.split()                # now words is a list of words
    occurrences = dict()
    for word in words:
        if word not in occurrences:
            occurrences[word] = 1
        else:
            occurrences[word] += 1

    srt = dict()                        # this will become the sorted version
                                        # of the occurrences dictionary

    # we sort occurrences dictionary
    for elem in sorted(occurrences, key=occurrences.get, reverse=True):
                       # 'key =' allows us to choose the sorting criteria
                       # 'dictionary.get' is the value
                       # 'reverse=True' allows to sort in descending order
                       # sorted(...) is a list of keys

        # assign each key to its corresponding value
        srt[elem] = occurrences[elem]
    return srt
        


FILE = 'harrypotter.txt'   # constants should be written LIKE_THIS
print(parse(FILE))         # works only if 'harrypotter.txt' is in same folder
