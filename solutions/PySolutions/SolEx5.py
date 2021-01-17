# constantly ask the user "what's your favourite TV show"
# every time he answers, show him every previous answer in a different row
# if he gives the same answer more than once, print "Don't repeat answers"
# if he gives the same answer but changing case, warn him with "DON'T TRY TO TRICK ME!"

ans = list()        # we create a list
#ans = []           # another way to create a list
while True:
    inp = input('What is your favourite TV show?')

    for elem in ans:
        print(elem)

    if inp in ans:


movies = list()     # we create a list
#movies = []        # another way to create a list
while True:
    ans = input("What's your favourite TV show?")
    for elem in movies:
        print(elem)

    if ans in movies:
        print("Don't repeat answers")
    elif ans.lower() in movies:
        print("DON'T TRY TO TRICK ME!")
    else:
        movies.append(ans.lower())          # WATCH OUT! WE NEED TO APPEND ans.lower()
                                            # otherwise program will be case sensitive
