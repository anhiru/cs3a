"""
Source program for LAB Assignment 7 for CS 3A
Written by Andrew Tran, 02/24/2019
"""


class TripleString:
    """ encapsulates a 3-string object """

    # class constants ----------------------------------------------
    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = '(undefined)'

    # constructor method -------------------------------------------
    def __init__(self,
                 string1=DEFAULT_STRING, string2=DEFAULT_STRING,
                 string3=DEFAULT_STRING):

        # instance attributes
        if not self.set_string1(string1):
            self.string1 = TripleString.DEFAULT_STRING

        if not self.set_string2(string2):
            self.string2 = TripleString.DEFAULT_STRING

        if not self.set_string3(string3):
            self.string3 = TripleString.DEFAULT_STRING

    # mutator ('set') methods --------------------------------------
    def set_string1(self, str1):
        """ modify string1 """
        if not self.valid_string(str1):
            return False
        # else
        self.string1 = str1
        return True

    def set_string2(self, str2):
        """ modify string2 """
        if not self.valid_string(str2):
            return False
        # else
        self.string2 = str2
        return True

    def set_string3(self, str3):
        """ modify string3 """
        if not self.valid_string(str3):
            return False
        # else
        self.string3 = str3
        return True

    # accessor ('get') methods -------------------------------------
    def get_string1(self):
        """ hand back string1 """
        return self.string1

    def get_string2(self):
        """ hand back string2 """
        return self.string2

    def get_string3(self):
        """ hand back string3 """
        return self.string3

    def to_string(self):
        """ return a string containing all the info of TripleString object """
        output = 'strings are:\n\t{}\n\t{}\n\t{}\n'.format(
            self.get_string1(), self.get_string2(), self.get_string3())
        return output

    # helper methods for entire class -----------------------------
    def valid_string(self, the_str):
        """ determine whether a given string length is legal """
        # True if len(the_str) is between MIN_LEN and MAX_LEN, otherwise False
        return TripleString.MIN_LEN <= len(the_str) <= TripleString.MAX_LEN


# ---------------------- CLIENT ------------------------------------

# create 4 TripleString objects
triple_string_num_1 = TripleString()
triple_string_num_2 = TripleString('Hello', 'world!',
                                   'Hope you\'re listening.')
triple_string_num_3 = TripleString('Just', 'two')
triple_string_num_4 = TripleString('1.', '..4..', '...3')

# display all 4 TripleString objects
print('Before mutators -------------------:')
print(triple_string_num_1.to_string())
print(triple_string_num_2.to_string())
print(triple_string_num_3.to_string())
print(triple_string_num_4.to_string())

# mutate 1 or more attribute(s) of every object
triple_string_num_1.set_string1('beginning')
triple_string_num_1.set_string2('middle')
triple_string_num_1.set_string3('end')

triple_string_num_2.set_string1('Bye')

triple_string_num_3.set_string3('...nevermind!')

triple_string_num_4.set_string2('h89h171xh812')

# display all 4 TripleString objects again
print('After mutators -------------------:')
print(triple_string_num_1.to_string())
print(triple_string_num_2.to_string())
print(triple_string_num_3.to_string())
print(triple_string_num_4.to_string())

# explicit mutator tests
print('\nExplicit mutator tests:')
if triple_string_num_1.set_string1(''):
    print('Call successful: string1 changed to \'\'')
else:
    print('Call failed: length of string \'\' was invalid')

if triple_string_num_1.set_string1('start'):
    print('Call successful: string1 changed to \'start\'')
else:
    print('Call failed: length of string \'start\' was invalid')

# accessor calls
print('\nAccessor calls:')
temp = triple_string_num_3.get_string2()
print('The second string of triple_string_num_3 is {}'.format(temp))
temp = triple_string_num_4.get_string2()
print('The second string of triple_string_num_4 is {}'.format(temp))


""" ------------------- SAMPLE RUN -------------------

Before mutators -------------------:
strings are:
    (undefined)
    (undefined)
    (undefined)

strings are:
    Hello
    world!
    Hope you're listening.

strings are:
    Just
    two
    (undefined)

strings are:
    1.
    ..4..
    ...3

After mutators -------------------:
strings are:
    beginning
    middle
    end

strings are:
    Bye
    world!
    Hope you're listening.

strings are:
    Just
    two
    ...nevermind!

strings are:
    1.
    h89h171xh812
    ...3


Explicit mutator tests:
Call failed: length of string '' was invalid
Call successful: string1 changed to 'start'

Accessor calls:
The second string of triple_string_num_3 is two
The second string of triple_string_num_4 is h89h171xh812


---------------------- END SAMPLE RUN ---------------- """
