"""
Source program for LAB Assignment 8 for CS 3A
Written by Andrew Tran, 03/02/2019
"""

import random

# global constants -------------------------------------------------
MIN_BET = 0
MAX_BET = 50


# helper class TripleString ----------------------------------------
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
    @classmethod
    def valid_string(cls, the_str):
        """ determine whether a given string length is legal """
        # True if len(the_str) is between MIN_LEN and MAX_LEN, otherwise False
        return cls.MIN_LEN <= len(the_str) <= cls.MAX_LEN


# global scope client functions ------------------------------------
def get_bet():
    while True:
        try:
            bet = int(input('How much would you like to bet '
                            '($1 - $50) or 0 to quit? $'))
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print('\nBet must be between $1 and $50.\n')
        except ValueError as e:
            print('\nIllegal value, enter an integer between 1 - 50.')
            print(e, end='\n\n')
    return bet


def pull():
    return TripleString(rand_string(), rand_string(), rand_string())


def rand_string():
    rand_num = random.randrange(100) + 1
    if 1 <= rand_num <= 40:
        return 'cherries'
    elif 40 < rand_num <= 78:
        return 'BAR'
    elif 78 < rand_num <= 93:
        return '7'
    else:
        return 'space'


def get_pay_multiplier(reels):
    icon1 = reels.get_string1()
    icon2 = reels.get_string2()
    icon3 = reels.get_string3()
    if icon1 == 'cherries' and icon2 != 'cherries':
        return 5
    elif icon1 == 'cherries' and icon2 == 'cherries' and icon3 != 'cherries':
        return 15
    elif icon1 == 'cherries' and icon2 == 'cherries' and icon3 == 'cherries':
        return 30
    elif icon1 == 'BAR' and icon2 == 'BAR' and icon3 == 'BAR':
        return 50
    elif icon1 == '7' and icon2 == '7' and icon3 == '7':
        return 100
    else:
        return 0


def display(reels, winnings):
    print('\n{} , {} , {}'.format(reels.get_string1(),
                                  reels.get_string2(),
                                  reels.get_string3()))
    if winnings > 0:
        print('Congratulations! You win: ${}\n'.format(winnings))
    else:
        print('Sorry, you lose.\n')


# main -------------------------------------------------------------
# set flags and initial bet amount
flag30Seen = False
flag50Seen = False
user_bet = get_bet()

while user_bet != 0:
    slots = pull()
    multiplier = get_pay_multiplier(slots)
    payout = user_bet * multiplier
    display(slots, payout)

    if multiplier == 30:  # cherries - cherries - cherries
        flag30Seen = True
    if multiplier == 50:  # BAR - BAR - BAR
        flag50Seen = True

    # if both flags are True, break out of while loop
    if flag30Seen and flag50Seen:
        break

    # ask for another bet amount to continue playing or quit (0)
    user_bet = get_bet()


# run over 100,000 times, betting $1 each time
user_bet = 1
user_winnings = 0
user_losses = 0
total_icons = 0
icons_count = {'cherries': 0,
               'BAR': 0,
               '7': 0,
               'space': 0}

for i in range(100001):
    slots = pull()
    multiplier = get_pay_multiplier(slots)

    user_winnings -= user_bet  # recall user_bet = 1 for these runs
    user_losses += user_bet  # casino always receives amount bet
    user_winnings += (user_bet * multiplier)  # payout

    icons = [slots.get_string1(), slots.get_string2(), slots.get_string3()]
    for icon in icons:
        total_icons += 1
        if icon == 'cherries':
            icons_count['cherries'] += 1
        elif icon == 'BAR':
            icons_count['BAR'] += 1
        elif icon == '7':
            icons_count['7'] += 1
        else:
            icons_count['space'] += 1

# calculate average frequencies of each icon
avg_cherries = '{}%'.format(round(100 * icons_count['cherries']
                                  / total_icons, 3))
avg_bar = '{}%'.format(round(100 * icons_count['BAR'] / total_icons, 3))
avg_7 = '{}%'.format(round(100 * icons_count['7'] / total_icons, 3))
avg_space = '{}%'.format(round(100 * icons_count['space'] / total_icons, 3))

# create dictionary illustrating the average distribution of icons
icons_avg = {'cherries': avg_cherries,
             'BAR': avg_bar,
             '7': avg_7,
             'space': avg_space}

# display count and frequencies of each icon
# as well as money won and lost over 100,001 runs
print('\n\nAFTER 100,001 RUNS ------------------------------------\n')
print('Count of each icon:\n {}\n'.format(icons_count))
print('Frequencies of each icon:\n {}\n'.format(icons_avg))
print('Money won: ${}\nMoney lost: ${}\n'.format(
    user_winnings, user_losses))

# report analysis
print('1. The symbols are very closely, but not exactly, following\n'
      '\tthe distribution in the program specifications.\n')
print('{:>15} {:5}'.format('cherries', '~ 40%'))
print('{:>15} {:5}'.format('BAR', '~ 38%'))
print('{:>15} {:5}'.format('7', '~ 15%'))
print('{:>15} {:5}'.format('space', '~ 7%'))
print('\n2. The count and frequencies of each icon (listed above) correctly\n'
      '\tresemble the program specifications, with less than a 1% error.\n')
print('3. The gambler is winning more money after 100,001 runs.\n')


""" ------------------- SAMPLE RUN -------------------

How much would you like to bet ($1 - $50) or 0 to quit? $asdf

Illegal value, enter an integer between 1 - 50.
invalid literal for int() with base 10: 'asdf'

How much would you like to bet ($1 - $50) or 0 to quit? $-1

Bet must be between $1 and $50.

How much would you like to bet ($1 - $50) or 0 to quit? $1

BAR , BAR , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $2

cherries , BAR , BAR
Congratulations! You win: $10

How much would you like to bet ($1 - $50) or 0 to quit? $3

7 , BAR , space
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $4

cherries , 7 , BAR
Congratulations! You win: $20

How much would you like to bet ($1 - $50) or 0 to quit? $5

BAR , BAR , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $6

cherries , cherries , space
Congratulations! You win: $90

How much would you like to bet ($1 - $50) or 0 to quit? $7

BAR , BAR , 7
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $8

BAR , BAR , BAR
Congratulations! You win: $400

How much would you like to bet ($1 - $50) or 0 to quit? $9

cherries , BAR , BAR
Congratulations! You win: $45

How much would you like to bet ($1 - $50) or 0 to quit? $10

7 , cherries , space
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $11

cherries , BAR , BAR
Congratulations! You win: $55

How much would you like to bet ($1 - $50) or 0 to quit? $12

BAR , BAR , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $13

BAR , cherries , BAR
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $14

cherries , 7 , 7
Congratulations! You win: $70

How much would you like to bet ($1 - $50) or 0 to quit? $15

cherries , cherries , space
Congratulations! You win: $225

How much would you like to bet ($1 - $50) or 0 to quit? $16

7 , cherries , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $17

cherries , cherries , BAR
Congratulations! You win: $255

How much would you like to bet ($1 - $50) or 0 to quit? $18

BAR , cherries , 7
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $19

cherries , cherries , 7
Congratulations! You win: $285

How much would you like to bet ($1 - $50) or 0 to quit? $20

cherries , BAR , 7
Congratulations! You win: $100

How much would you like to bet ($1 - $50) or 0 to quit? $21

BAR , cherries , 7
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $22

7 , 7 , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $23

cherries , space , cherries
Congratulations! You win: $115

How much would you like to bet ($1 - $50) or 0 to quit? $24

cherries , BAR , 7
Congratulations! You win: $120

How much would you like to bet ($1 - $50) or 0 to quit? $25

7 , 7 , BAR
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $26

7 , 7 , 7
Congratulations! You win: $2600

How much would you like to bet ($1 - $50) or 0 to quit? $27

cherries , BAR , BAR
Congratulations! You win: $135

How much would you like to bet ($1 - $50) or 0 to quit? $28

space , BAR , BAR
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $29

space , cherries , BAR
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $30

BAR , cherries , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $31

7 , 7 , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $32

BAR , cherries , BAR
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $33

cherries , BAR , cherries
Congratulations! You win: $165

How much would you like to bet ($1 - $50) or 0 to quit? $34

cherries , cherries , 7
Congratulations! You win: $510

How much would you like to bet ($1 - $50) or 0 to quit? $35

BAR , cherries , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $36

BAR , cherries , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $37

7 , BAR , cherries
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $38

7 , cherries , 7
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $39

cherries , 7 , space
Congratulations! You win: $195

How much would you like to bet ($1 - $50) or 0 to quit? $40

BAR , cherries , 7
Sorry, you lose.

How much would you like to bet ($1 - $50) or 0 to quit? $41

cherries , cherries , cherries
Congratulations! You win: $1230



AFTER 100,001 RUNS ------------------------------------

Count of each icon:
 {'cherries': 120306, 'BAR': 113743, '7': 44776, 'space': 21178}

Frequencies of each icon:
 {'cherries': '40.102%', 'BAR': '37.914%', '7': '14.925%', 'space': '7.059%'}

Money won: $667854
Money lost: $100001

1. The symbols are very closely, but not exactly, following
    the distribution in the program specifications.

       cherries ~ 40%
            BAR ~ 38%
              7 ~ 15%
          space ~ 7% 

2. The count and frequencies of each icon (listed above) correctly
    resemble the program specifications, with less than a 1% error.

3. The gambler is winning more money after 100,001 runs.


---------------------- END SAMPLE RUN ---------------- """
