""" program to find whether a number 'n' is a power of 2 """

import math


def isPowerOfTwo(n):
    """ function to check if parameter 'n' is a power of 2 """
    # while n % 2 == 0 and n != 0:
    #     n /= 2
    #     if n == 1:
    #         return True
    # return False
    return n > 0 and math.log(n, 2).is_integer()


# main
print(isPowerOfTwo(-2))
print(isPowerOfTwo(0))
print(isPowerOfTwo(1))
print(isPowerOfTwo(1/2))
print(isPowerOfTwo(math.sqrt(2)))