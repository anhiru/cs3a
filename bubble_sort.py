""" example program demonstrating bubble sort """

import math as m

# MAX_SIZE = 20 is not used because we cannot easily predict size of array
ITEMS_PER_LINE = 5


def float_largest_to_top(data, array_size):
    changed = False

    # notice that we stop at (array_size - 2) because of (k + 1) in loop
    for k in range(array_size - 1):
        if data[k] > data[k + 1]:
            data[k], data[k + 1] = data[k + 1], data[k]
            changed = True

    return changed


def array_sort(data, arr_size):
    for k in range(arr_size):
        if not float_largest_to_top(data, arr_size - k):
            return


def print_array(data, arr_size, optional_title='--- The Array ----:\n'):
    print(optional_title)

    # new line every ITEMS_PER_LINE items, commas between
    for k in range(arr_size):
        if k % ITEMS_PER_LINE == 0:
            print()
        else:
            print('', '', end='')
        print(data[k], end='')


# client -----------------------------------------------------------
my_array = [10.2, 56.9, -33, 12, 0, 2, 4.8, 199.9, 73, -91.2]
array_size = len(my_array)

print_array(my_array, array_size, "Our array before the sort")
array_sort(my_array, array_size)
print('\n')
print_array(my_array, array_size, "And now after the sort")
print('\n')


# question 34
class Dog:
    def __init__(self, name):
        self.name = name

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name


my_dog = Dog('Fifi')
your_dog = my_dog
my_dog.set_name('Leon')
print(my_dog.get_name())
print(your_dog.get_name())
