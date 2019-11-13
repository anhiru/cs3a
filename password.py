"""
source program that gets a valid password from the user
"""

MIN_LEN = 6
MAX_LEN = 15

valid = False
while not valid:
    password = input('Create your password: ')
    length = len(password)

    # test for quit
    if length == 1 and password[0].casefold() == 'q':
        print('\nUser canceled session; no password defined.\n')
        break

    # test for proper length
    if not (MIN_LEN <= length <= MAX_LEN):
        print('Password length must be between {} and {} characters, '
              'inclusive.\n '.format(MIN_LEN, MAX_LEN))
        continue

    valid = True  # assume innocent entering loop
    # allow only letters and numbers
    for k in range(length):
        letter = password[k]  # store in local variable so we can reuse
        if 'a' <= letter <= 'z':
            continue  # the for loop, we have a good lower case letter
        elif 'A' <= letter <= 'Z':
            continue  # the for loop, we have a good upper case letter
        elif '0' <= letter <= '9':
            continue  # the for loop, we have a good numeral
        else:
            # this letter is not one of the three legal types
            print('Use only A-Z, a-z or 0-9, please.\n')
            valid = False
            break  # from the for loop leaving validated as false

    # if the above loop yielded an error, we try again
    if not valid:
        continue

    # if we made it here, it is the proper length and has legal chars
    # but is the first character a letter?
    letter = password[0]
    if letter >= '0' and letter <= '9':
        print('First character must be a letter (non-numeric).\n')
        valid = False
        continue
    else:
        # they passed the final test
        print('\nYour password ' + password + ' has been accepted.\n')
        # no need for break since good while() condition

print('Good bye.\n\n')
