"""
Source program for LAB Assignment 11 for CS 3A
Written by Andrew Tran, 03/24/2019
application of Student and StudentArrayUtilities classes
"""


# beginning of class Student definition ----------------------------
class Student:
    # class ('static') members and intended constants
    DEFAULT_NAME = 'zz-error'
    DEFAULT_POINTS = 0
    MAX_POINTS = 30
    SORT_BY_FIRST = 88
    SORT_BY_LAST = 98
    SORT_BY_POINTS = 108

    # class ('static') int
    sort_key = SORT_BY_LAST

    # initializer ('constructor') method -------------
    def __init__(self,
                 last=DEFAULT_NAME,
                 first=DEFAULT_NAME,
                 points=DEFAULT_POINTS):
        # instance attributes
        if not self.set_last_name(last):
            self.last_name = Student.DEFAULT_NAME
        if not self.set_first_name(first):
            self.first_name = Student.DEFAULT_NAME
        if not self.set_points(points):
            self.total_points = Student.DEFAULT_POINTS

    # mutator ('set') methods ------------------------
    def set_last_name(self, last):
        if not self.valid_string(last):
            return False
        # else
        self.last_name = last
        return True

    def set_first_name(self, first):
        if not self.valid_string(first):
            return False
        # else
        self.first_name = first
        return True

    def set_points(self, points):
        if not self.valid_points(points):
            return False
        # else
        self.total_points = points
        return True

    # accessor ('get') methods -----------------------
    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_total_points(self):
        return self.total_points

    # output method  ---------------------------------
    def display(self, client_intro_str='--- STUDENT DATA ---'):
        print(self.to_string(client_intro_str))

    # instance helpers -------------------------------
    def to_string(self, optional_title=' ---------- '):
        ret_str = ((optional_title
                    + '\n    name: {}, {}'
                    + '\n    total points: {}.').
                   format(self.last_name, self.first_name,
                          self.total_points))
        return ret_str

    # static/class methods ---------------------------
    @staticmethod
    def valid_string(test_str):
        return len(test_str) > 0 and test_str[0].isalpha()

    @classmethod
    def valid_points(cls, test_points):
        if 0 <= test_points <= cls.MAX_POINTS:
            return False
        return True

    @classmethod
    def compare_two_students(cls, first_stud, second_stud):
        if cls.sort_key == cls.SORT_BY_FIRST:
            return cls.compare_strings_ignore_case(
                first_stud.get_first_name(), second_stud.get_first_name())
        elif cls.sort_key == cls.SORT_BY_LAST:
            return cls.compare_strings_ignore_case(
                first_stud.get_last_name(), second_stud.get_last_name())
        else:
            return (first_stud.get_total_points()
                    - second_stud.get_total_points())

    # helper method for compare_two_students()
    @staticmethod
    def compare_strings_ignore_case(first_string, second_string):
        """ returns -1 if first < second, lexicographically,
           +1 if first > second, and 0 if same
           this particular version based on last name only
           (case insensitive) """

        first_upper = first_string.upper()
        second_upper = second_string.upper()
        if first_upper < second_upper:
            return -1
        # else if
        if first_upper > second_upper:
            return 1
        # else
        return 0

    @classmethod
    def set_sort_key(cls, key):
        """ mutator for the member sortKey """
        cls.sort_key = key

    @classmethod
    def get_sort_key(cls):
        """ accessor for the member sortKey """
        return cls.sort_key


# beginning of class StudentArrayUtilities definition --------------
class StudentArrayUtilities:
    # static constant best defined at top of class
    NOT_FOUND = -1

    @staticmethod
    def to_string(stud_array,
                  optional_title='--- The Students -----------:\n'):

        ret_str = optional_title
        for student in stud_array:
            ret_str += ('\n' + student.to_string())

        return ret_str

    @classmethod
    def array_sort(cls, data, array_size):
        for k in range(array_size):
            if not cls.float_largest_to_top(data, array_size - k):
                return

    @staticmethod
    def float_largest_to_top(data, array_size):

        changed = False

        # notice we stop at array_size - 2 because of expr. k + 1 in loop
        for k in range(array_size - 1):
            if Student.compare_two_students(data[k], data[k + 1]) > 0:
                data[k], data[k + 1] = data[k + 1], data[k]
                changed = True
        return changed

    @classmethod
    def array_search(cls, data, array_size, key_first, key_last):
        for k in range(array_size):
            if (data[k].get_last_name() == key_last
                    and data[k].get_first_name() == key_first):
                return k  # found match, return index
        return cls.NOT_FOUND

    @classmethod
    def binary_search_for_last_name(cls, data, key_last_nm,
                                    first_index, last_index):
        # exhausted search
        if first_index > last_index:
            return cls.NOT_FOUND

        middle_index = int((first_index + last_index) / 2)

        result = Student.compare_strings_ignore_case(
            key_last_nm,
            data[middle_index].get_last_name()
        )

        # < 0 means key before middle index
        if result < 0:
            return cls.binary_search_for_last_name(
                data, key_last_nm, first_index, middle_index - 1)

        # > 0 means key after middle index
        if result > 0:
            return cls.binary_search_for_last_name(
                data, key_last_nm, middle_index + 1, last_index)

        # else key IS in middle index position, i.e., found him
        return middle_index

    @classmethod
    def get_median_destructive(cls, array, array_size):
        median = 0
        if array_size < 1:
            return median

        saved_sort_key = Student.get_sort_key()
        Student.set_sort_key(Student.SORT_BY_POINTS)

        cls.array_sort(array, array_size)
        # cast (array_size / 2) to int because indexes cannot be floats
        if array_size % 2 == 0:
            median = (array[int(array_size / 2)].get_total_points() +
                      array[int(array_size / 2) - 1].get_total_points()) / 2
        else:
            median = array[int(array_size / 2)].get_total_points()

        Student.set_sort_key(saved_sort_key)
        return median


# client -----------------------------------------------------------

# instantiate three student arrays, two with an illegal name ...
student_arr1 = \
    [
        Student('smith', 'fred', 95),
        Student('bauer', 'jack', 123),
        Student('jacobs', 'carrie', 195),
        Student('renquist', 'abe', 148),
        Student('3ackson', 'trevor', 108),
        Student('perry', 'fred', 225),
        Student('lewis', 'frank', 44),
        Student('stollings', 'pamela', 452),
        Student('shetty', 'namrata', 100),
        Student('desai', 'shrina', 145),
        Student('chen', 'aileen', 282),
        Student('bui', 'william', 459),
        Student('lieu', 'spencer', 198),
        Student('nguyen', 'trucdan', 71),
        Student('chiang', 'nicholas', 55),
    ]
student_arr2 = \
    [
        Student('smith', 'fred', 95),
        Student('bauer', 'jack', 123),
        Student('jacobs', 'carrie', 195),
        Student('renquist', 'abe', 148),
        Student('3ackson', 'trevor', 108),
        Student('perry', 'fred', 225),
        Student('lewis', 'frank', 44),
        Student('stollings', 'pamela', 452),
        Student('shetty', 'namrata', 100),
        Student('desai', 'shrina', 145),
        Student('chen', 'aileen', 282),
        Student('bui', 'william', 459),
        Student('lieu', 'spencer', 198),
        Student('nguyen', 'trucdan', 71),
        Student('chang', 'nicholas', 55),
        Student('cui', 'carissa', 83)
    ]
student_arr3 = [Student('fuller', 'buckminster', 72)]

# assign size variables for each array
arr_size1 = len(student_arr1)
arr_size2 = len(student_arr2)
arr_size3 = len(student_arr3)

# tests using largest, even numbered array -----------
# display student_arr2 before calling sort method
print(StudentArrayUtilities.to_string(
    student_arr2, 'Before default sort (even):'))

# sort student_arr2 using initial sort key and display
StudentArrayUtilities.array_sort(student_arr2, arr_size2)
print(StudentArrayUtilities.to_string(
    student_arr2, '\n\nAfter default sort (even):'))

# change the sort key to first name, sort and display
Student.set_sort_key(Student.SORT_BY_FIRST)
StudentArrayUtilities.array_sort(student_arr2, arr_size2)
print(StudentArrayUtilities.to_string(
    student_arr2, '\n\nAfter sort BY FIRST:'))

# change the sort key to total score, sort and display
Student.set_sort_key(Student.SORT_BY_POINTS)
StudentArrayUtilities.array_sort(student_arr2, arr_size2)
print(StudentArrayUtilities.to_string(
    student_arr2, '\n\nAfter sort BY POINTS:'))

# change the sort key to first name and display median score
Student.set_sort_key(Student.SORT_BY_FIRST)
print('\n\nMedian of even class = {}'.format(
    StudentArrayUtilities.get_median_destructive(student_arr2, arr_size2)
))
if Student.get_sort_key() == Student.SORT_BY_FIRST:
    print('Failed to preserve sort key.')
else:
    print('Successfully preserved sort key.')

# calculate the median of the odd numbered array
print('Median of odd class = {}'.format(
    StudentArrayUtilities.get_median_destructive(student_arr1, arr_size1)
))

# calculate the median of the smallest array
print('Median of small class = {}'.format(
    StudentArrayUtilities.get_median_destructive(student_arr3, arr_size3)
))


""" ------------------- SAMPLE RUN -------------------

Before default sort (even):
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: zz-error, trevor
    total points: 108.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: shetty, namrata
    total points: 100.
 ---------- 
    name: desai, shrina
    total points: 145.
 ---------- 
    name: chen, aileen
    total points: 282.
 ---------- 
    name: bui, william
    total points: 459.
 ---------- 
    name: lieu, spencer
    total points: 198.
 ---------- 
    name: nguyen, trucdan
    total points: 71.
 ---------- 
    name: chang, nicholas
    total points: 55.
 ---------- 
    name: cui, carissa
    total points: 83.


After default sort (even):
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: bui, william
    total points: 459.
 ---------- 
    name: chang, nicholas
    total points: 55.
 ---------- 
    name: chen, aileen
    total points: 282.
 ---------- 
    name: cui, carissa
    total points: 83.
 ---------- 
    name: desai, shrina
    total points: 145.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: lieu, spencer
    total points: 198.
 ---------- 
    name: nguyen, trucdan
    total points: 71.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: shetty, namrata
    total points: 100.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: zz-error, trevor
    total points: 108.


After sort BY FIRST:
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: chen, aileen
    total points: 282.
 ---------- 
    name: cui, carissa
    total points: 83.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: shetty, namrata
    total points: 100.
 ---------- 
    name: chang, nicholas
    total points: 55.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: desai, shrina
    total points: 145.
 ---------- 
    name: lieu, spencer
    total points: 198.
 ---------- 
    name: zz-error, trevor
    total points: 108.
 ---------- 
    name: nguyen, trucdan
    total points: 71.
 ---------- 
    name: bui, william
    total points: 459.


After sort BY POINTS:
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: chang, nicholas
    total points: 55.
 ---------- 
    name: nguyen, trucdan
    total points: 71.
 ---------- 
    name: cui, carissa
    total points: 83.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: shetty, namrata
    total points: 100.
 ---------- 
    name: zz-error, trevor
    total points: 108.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: desai, shrina
    total points: 145.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: lieu, spencer
    total points: 198.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: chen, aileen
    total points: 282.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: bui, william
    total points: 459.


Median of even class = 134.0
Failed to preserve sort key.
Median of odd class = 145
Median of small class = 72

---------------------- END SAMPLE RUN ---------------- """
