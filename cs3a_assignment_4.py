"""
Source program for LAB Assignment 4 for CS 3A
Written by Andrew Tran 01/29/2019
"""

# part one
# initialize specific range of years
years = range(1987, 2012)

# iterate through each individual year in years
for year in years:
    curr_year = str(year)  # convert year to string to iterate through digits
    digitCount = [0] * 10

    # iterate through each individual digit in curr_year
    for digit in curr_year:
        curr_digit = int(digit)  # convert digit to int to use as an index
        digitCount[curr_digit] += 1

    duplicates = False
    output_string = ''
    possible_comma = ''

    # iterate through each index of digitCount list to check for duplicates
    for index in range(len(digitCount)):
        if digitCount[index] > 1:
            duplicates = True  # found a duplicate in curr_year
            output_string += '{}{}'.format(possible_comma, index)
            possible_comma = ', '

    # modify output_string based on the discovery of duplicates
    if duplicates:
        output_string = '{} has duplicates: {}'.format(year, output_string)
    else:
        output_string = '{} has no duplicates.'.format(year)

    print(output_string)

print('\n')

""" -------------- SAMPLE RUN PART ONE ---------------

1987 has no duplicates.
1988 has duplicates: 8
1989 has duplicates: 9
1990 has duplicates: 9
1991 has duplicates: 1, 9
1992 has duplicates: 9
1993 has duplicates: 9
1994 has duplicates: 9
1995 has duplicates: 9
1996 has duplicates: 9
1997 has duplicates: 9
1998 has duplicates: 9
1999 has duplicates: 9
2000 has duplicates: 0
2001 has duplicates: 0
2002 has duplicates: 0, 2
2003 has duplicates: 0
2004 has duplicates: 0
2005 has duplicates: 0
2006 has duplicates: 0
2007 has duplicates: 0
2008 has duplicates: 0
2009 has duplicates: 0
2010 has duplicates: 0
2011 has duplicates: 1


---------------------- END SAMPLE RUN ---------------- """

# part two
# use symbolic constants to represent the number of rows and columns
NUM_ROWS = 6
NUM_COLS = 6

# print all values in a field of fixed length 7
print('{:7}'.format(0.0), end='')
for k in range(5, NUM_COLS * 10, 10):
    print('{:7}'.format(k / 10.0), end=' ')  # print top row labels
print('\n')

for i in range(5, NUM_ROWS * 10, 10):
    print('{:7}'.format(i / 10.0), end=' ')  # print left column labels
    for j in range(5, NUM_COLS * 10, 10):
        product = (i / 10.0) * (j / 10.0)
        print('{:7.2f}'.format(product), end=' ')  # print products
    print('\n')

""" -------------- SAMPLE RUN PART TWO ---------------

    0.0    0.5     1.5     2.5     3.5     4.5     5.5 

    0.5    0.25    0.75    1.25    1.75    2.25    2.75 

    1.5    0.75    2.25    3.75    5.25    6.75    8.25 

    2.5    1.25    3.75    6.25    8.75   11.25   13.75 

    3.5    1.75    5.25    8.75   12.25   15.75   19.25 

    4.5    2.25    6.75   11.25   15.75   20.25   24.75 

    5.5    2.75    8.25   13.75   19.25   24.75   30.25 

  
---------------------- END SAMPLE RUN ---------------- """
