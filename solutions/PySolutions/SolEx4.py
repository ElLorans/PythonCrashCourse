# ask the user to insert a username and a password
# show ACCESS GRANTED if:
# the username is BOSS and the password is money
# the username is pythondeveloper (not case sensitive) and the password is Slave
# show ACCESS DENIED if one or both inputs are incorrect
# bonus point: after 3 errors the program stops


count = 0
while count < 3:
    user = input('Insert username:')
    password = input('Inser password')

    if user == 'BOSS' and password == 'money':
        print('Access granted')
        break
    elif user.lower() == 'pythondeveloper' and password == 'Slave':
        # user.lower() is not case sensitive! we changed the input to lowercase
        # and we compare it to a lowercase string
        
        print('Access granted')
        break
    else:
        print('ACCESS DENIED')
        count += 1

if count == 3:
    print('You failed to login too many times')
