"""
Source program for LAB Assignment 5 for CS 3A
Written by Andrew Tran, 02/09/2019
"""

# part one
# initialize list of values to test for primes
candidatePrimes = [2, 10, 12, 15, 17, 31, 89, 97, 7919, 982451653]

for num in candidatePrimes:
    prime = False

    if num > 1:
        # assume num is prime if it is greater than 1...until shown it is not
        prime = True

        # check for divisors between 2 and the (square root of num) + 1
        # the + 1 is added in case casting to an int from a float is too low
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False  # found a value i that divides evenly into num
                break

    if prime:
        print('{} is a prime number.'.format(num))
    else:
        print('{} is not a prime number.'.format(num))

# part two
# function definition ---------------------------


def isPrime(p):
    """ checks whether or not a given number 'p' is prime """
    # copy code from part one, replacing 'num' with 'p'
    # and returning p if prime, 0 if not prime
    prime = False

    if p > 1:
        prime = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                prime = False
                break

    if prime:
        return p
    else:
        return 0


# part three
# main ------------------------------------------

# initialize list of primes and upper/lower bounds for range
primes = []
LOWER_BOUND = 1000
UPPER_BOUND = 1500

for value in range(LOWER_BOUND, UPPER_BOUND):
    # use isPrime() method to determine if current value is a prime number
    possiblePrime = isPrime(value)

    if possiblePrime != 0:
        primes.append(possiblePrime)  # add to end of list of primes
    if len(primes) == 3:
        break  # already found 3 primes, so exit loop

print('\nThe first 3 prime numbers between ' \
      '{} and {} are {}'.format(LOWER_BOUND, UPPER_BOUND, primes))


""" ------------------- SAMPLE RUN -------------------

2 is a prime number.
10 is not a prime number.
12 is not a prime number.
15 is not a prime number.
17 is a prime number.
31 is a prime number.
89 is a prime number.
97 is a prime number.
7919 is a prime number.
982451653 is a prime number.

The first 3 prime numbers between 1000 and 1500 are [1009, 1013, 1019]

---------------------- END SAMPLE RUN ---------------- """
