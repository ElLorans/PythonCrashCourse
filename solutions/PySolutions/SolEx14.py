# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hint: use range(#begin, #end) function


res = []
for elem in range(2000, 3201):      # last number is not included! So, 3201
    if elem % 7 == 0 and elem % 5 != 0:
        res.append(elem)

# let's print res in a comma separated sequence with no brackets

for elem in res:
    print(elem, end=',')
