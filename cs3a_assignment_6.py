"""
Source program for LAB Assignment 6 for CS 3A
Written by Andrew Tran, 02/16/2019
"""


# part one
def isColliding(ball_one, ball_two):
    """determine if two balls are colliding given 3-tuples of floats
    which hold the (x,y) coordinates of their centers and respective radii"""
    # set (x, y) values of each ball
    x1 = ball_one[0]
    y1 = ball_one[1]
    x2 = ball_two[0]
    y2 = ball_two[1]

    # compute the distance between ball centers using distance formula
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

    # return True (balls are colliding) if the distance between their centers
    # is less than or equal to the sum of their respective radii
    return distance <= ball_one[2] + ball_two[2]


# part two
# code copy + pasted below from LAB Assignment 6 module
# 1: set up a list to iterate on
# 2: myCheeseList = ["Apple", "Asiago", "Brie", "Caerphilly",
# 3:                 "Emmental", "Gloucester", "Gouda"]
# 4:
# 5: for i in range(len(myCheeseList)):
# 6:
# 7:     if i == 2:
# 8:         del(myCheeseList[4])
# 9:
# 10:    print(i, myCheeseList[i])
print('An IndexError occurs at line 10 during the 7th (last) iteration.\n'
      'After del(myCheeseList[4]), the list elements shift left by one,\n'
      'so myCheeseList[6] no longer exists, and trying to print it\n'
      'will result in an IndexError: list index out of range.\n')
print('To fix this, we could use a while loop instead:\n'
      'while i < len(myCheeseList):\n\t# code in loop\n\tindex += 1\n'
      'with i initialized at 0 before the start of the while loop.\n\n'
      'This would work since len(myCheeseList) is recalculated each time\n'
      'around the loop, making it possible to delete items from the list.\n')

""" -------------- SAMPLE RUN PART TWO ---------------

An IndexError occurs at line 10 during the 7th (last) iteration.
After del(myCheeseList[4]), the list elements shift left by one,
so myCheeseList[6] no longer exists, and trying to print it
will result in an IndexError: list index out of range.

To fix this, we could use a while loop instead:
while i < len(myCheeseList):
    # code in loop
    index += 1
with i initialized at 0 before the start of the while loop.

This would work since len(myCheeseList) is recalculated each time
around the loop, making it possible to delete items from the list.


---------------------- END SAMPLE RUN ---------------- """

# part three
print('Chapter 7, Files:\n'
      '\t1) If the open is successful, the operating system\n'
      '\treturns us a file handle.\n'
      '\t2) If the file does not exist, open will fail with a traceback\n'
      '\tand you will not get a handle to access the contents of the file.\n')
print('Chapter 9, Dictionaries:\n'
      '\t1) The curly brackets, {}, represent an empty dictionary.\n'
      '\t2) The order of the key-value pairs is not the same.\n')
print('Chapter 10, Tuples:\n'
      '\t1) The values stored in a tuple can be any type,\n'
      '\tand they are indexed by integers.\n'
      '\t2) To create a tuple with a single element,\n'
      '\tyou have to include the final comma.\n')

""" ------------- SAMPLE RUN PART THREE --------------

Chapter 7, Files:
    1) If the open is successful, the operating system
    returns us a file handle.
    2) If the file does not exist, open will fail with a traceback
    and you will not get a handle to access the contents of the file.

Chapter 9, Dictionaries:
    1) The curly brackets, {}, represent an empty dictionary.
    2) The order of the key-value pairs is not the same.

Chapter 10, Tuples:
    1) The values stored in a tuple can be any type,
    and they are indexed by integers.
    2) To create a tuple with a single element,
    you have to include the final comma.


---------------------- END SAMPLE RUN ---------------- """


# part four
# translating 5 animal names from English to Spanish
def translate(word):
    """translate an inputted English word into its Spanish counterpart"""
    if word in eng_span_dict:
        return eng_span_dict[word]
    else:
        return ''


# create an English-to-Spanish dictionary
eng_span_dict = {'bee': 'abeja',
                 'iguana': 'iguana',
                 'scorpion': 'alacrán',
                 'giraffe': 'jirafa',
                 'spider': 'araña'}

# 4 test cases that show one of the 5 English words being translated
# to Spanish and a lookup on "flea" getting an empty string
test1 = translate('bee')
test2 = translate('iguana')
test3 = translate('scorpion')
test4 = translate('spider')
test5 = translate('flea')
print(test1, test2, test3, test4, test5, end='\n\n')


# translating English-Spanish-Greek
# create 5 more dictionaries, in addition to the English-to-Spanish dictionary

# Spanish-to-English dictionary
span_eng_dict = {'abeja': 'bee',
                 'iguana': 'iguana',
                 'alacrán': 'scorpion',
                 'jirafa': 'giraffe',
                 'araña': 'spider'}

# English-to-Greek dictionary
eng_greek_dict = {'bee': 'μέλισσα',
                  'iguana': 'ιγκουάνα',
                  'scorpion': 'σκορπιός',
                  'giraffe': 'καμηλοπάρδαλη',
                  'spider': 'αράχνη'}

# Greek-to-English dictionary
greek_eng_dict = {'μέλισσα': 'bee',
                  'ιγκουάνα': 'iguana',
                  'σκορπιός': 'scorpion',
                  'καμηλοπάρδαλη': 'giraffe',
                  'αράχνη': 'spider'}

# Spanish-to-Greek dictionary
span_greek_dict = {'abeja': 'μέλισσα',
                   'iguana': 'ιγκουάνα',
                   'alacrán': 'σκορπιός',
                   'jirafa': 'καμηλοπάρδαλη',
                   'araña': 'αράχνη'}

# Greek-to-Spanish dictionary
greek_span_dict = {'μέλισσα': 'abeja',
                   'ιγκουάνα': 'iguana',
                   'σκορπιός': 'alacrán',
                   'καμηλοπάρδαλη': 'jirafa',
                   'αράχνη': 'araña'}


def translate(fm, to, word):
    """translate an inputted word from English/Spanish/Greek
    to any of the three languages of choice"""
    try:
        if fm == 'en':
            if to == 'sp':
                return eng_span_dict[word]
            else:
                return eng_greek_dict[word]
        elif fm == 'sp':
            if to == 'en':
                return span_eng_dict[word]
            else:
                return span_greek_dict[word]
        else:
            if to == 'en':
                return greek_eng_dict[word]
            else:
                return greek_span_dict[word]
    except KeyError:
        pass


# 10 successful test cases and 1 failed due to KeyError
test1 = translate('en', 'en', 'spider')
test2 = translate('gr', 'sp', 'ιγκουάνα')
test3 = translate('en', 'gr', 'giraffe')
test4 = translate('sp', 'gr', 'abeja')
test5 = translate('sp', 'en', 'alacrán')
test6 = translate('gr', 'en', 'μέλισσα')
test7 = translate('en', 'gr', 'scorpion')
test8 = translate('sp', 'en', 'alacrán')
test9 = translate('en', 'sp', 'iguana')
test10 = translate('gr', 'sp', 'σκορπιός')
test11 = translate('en', 'sp', 'flea')
print(test1, test2, test3, test4, test5, test6,
      test7, test8, test9, test10, test11, sep='\n')

""" -------------- SAMPLE RUN PART FOUR --------------

abeja iguana alacrán araña 

αράχνη
iguana
καμηλοπάρδαλη
μέλισσα
scorpion
bee
σκορπιός
scorpion
iguana
alacrán
None


---------------------- END SAMPLE RUN ---------------- """
