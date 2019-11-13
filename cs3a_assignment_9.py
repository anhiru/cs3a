"""
Source program for LAB Assignment 9 for CS 3A
Written by Andrew Tran, 03/10/2019
program that translates 1,000 common words between
English, Spanish, and Greek
"""

from timeit import default_timer as timer


def make_dict(input_file_name):
    with open(input_file_name, 'r', encoding='utf-8') as f:
        dict_list = f.readlines()
        index = 0
        while index < len(dict_list):
            dict_list[index] = dict_list[index].rstrip('\n')
            index += 1
    keys = (x for x in range(1000))
    return dict(zip(keys, dict_list))


en_dict = make_dict('1kwords.en.txt')
sp_dict = make_dict('1kwords.sp.txt')
gr_dict = make_dict('1kwords.gr.txt')

dict_language = {'en': en_dict, 'sp': sp_dict, 'gr': gr_dict}


def translate(fm, to, word):
    if fm not in dict_language.keys():
        return 'from is not a valid language code.'
    elif to not in dict_language.keys():
        return 'to not a valid language code.'
    else:
        for i in range(1000):
            if fm == to:
                return word 
            if word not in dict_language[fm].values():
                return 'The word you want to look up ' \
                       'is not in the dictionary.'
            if dict_language[fm][i] == word:
                return dict_language[to][i]


def func_to_measure():
    spbee = translate('gr', 'sp', 'μέλισσα')
    translate('sp', 'en', spbee)
    translate('en', 'sp', 'heart')
    translate('en', 'gr', 'heart')
    translate('en', 'gr', 'diegetic')
    translate('gr', 'en', 'μέλισσα')
    spneck = translate('en', 'sp', 'neck')
    translate('en', 'gr', 'neck')
    translate('sp', 'gr', spneck)
    translate('en', 'sp', 'beauty')


# part one
print('Test run of Sample Answer 2 WITHOUT benchmark code:')
print(translate('en', 'gr', 'light'))
print(translate('en', 'sp', 'light'))
print(translate('sp', 'en', 'momento'))
print(translate('sp', 'gr', 'momento'))
print((translate('gr', 'en', 'πολλαπλασιάστε')))
print(translate('gr', 'sp', 'πολλαπλασιάστε'))
print(translate('en', 'gr', 'giraffe'))


""" -------------- SAMPLE RUN PART ONE ---------------

Test run of Sample Answer 2 WITHOUT benchmark code:
φως
luz
moment
στιγμή
multiply
multiplicar
The word you want to look up is not in the dictionary.


---------------------- END SAMPLE RUN ---------------- """

# part two
# test Sample Answer 2 with added benchmark code (import, func_to_measure())
print('\n\nTest run of Sample Answer 2 WITH benchmark code:')
print(translate('en', 'gr', 'river'))
print(translate('gr', 'en', 'πηγαίνω'))
print(translate('gr', 'en', 'γυναικών'))
print(translate('gr', 'sp', 'απασχολημένος'))
print(translate('sp', 'gr', 'jirafa'))
print('\nstarting timer')
start = timer()
func_to_measure()
end = timer()

elapsed = end - start
print('10 words translated in', elapsed, 'secs\n\n')


""" -------------- SAMPLE RUN PART TWO ---------------

Test run of Sample Answer 2 WITH benchmark code:
ποτάμι
go
women
ocupado
The word you want to look up is not in the dictionary.

starting timer
10 words translated in 0.095431397 secs


---------------------- END SAMPLE RUN ---------------- """

# part three
# benchmark Sample Answer 2 to find out
# how quickly it can process 10,000 translations
print('Test run of Sample Answer 2 WITH benchmark code and 10K translations:')
print('starting timer')
start = timer()
for k in range(1000):
    func_to_measure()
end = timer()

elapsed = end - start
print('10K words translated in', elapsed, 'secs\n\n')


""" ------------- SAMPLE RUN PART THREE --------------

Test run of Sample Answer 2 WITH benchmark code and 10K translations:
starting timer
10K words translated in 96.614978712 secs


---------------------- END SAMPLE RUN ---------------- """

# part four
# verify that Sample Answer 2 can translate
# 9 of the 10 words given in func_to_measure()

print('Translations in func_to_measure():')
spbee = translate('gr', 'sp', 'μέλισσα')
print(spbee)
print(translate('sp', 'en', spbee))
print(translate('en', 'sp', 'heart'))
print(translate('en', 'gr', 'heart'))
print(translate('en', 'gr', 'diegetic'))
print(translate('gr', 'en', 'μέλισσα'))
spneck = translate('en', 'sp', 'neck')
print(spneck)
print(translate('en', 'gr', 'neck'))
print(translate('sp', 'gr', spneck))
print(translate('en', 'sp', 'beauty'))


""" -------------- SAMPLE RUN PART FOUR --------------

Translations in func_to_measure():
abeja
bee
corazón
καρδιά
The word you want to look up is not in the dictionary.
bee
cuello
λαιμός
λαιμός
belleza


---------------------- END SAMPLE RUN ---------------- 

The processing from Sample Answer 4 appears to be significantly faster
than that of Sample Answer 2. When I ran both programs, I recorded a 
difference in time of over a minute and a half (~ 3.5 seconds for
Sample Answer 4, in comparison to the ~ 96.6 seconds for Sample Answer 2).
This is largely due to the different methods used to process information 
and search for words in all of the dictionaries. 

In Sample Answer 2, finding a translation for a parameterized word is done 
by iterating through every key of the 'fm' dictionary until a match is found.
The program then returns the value of the 'to' dictionary at the 
corresponding index for the match. The need to iterate through a loop
starting from the beginning makes searching for a translation a very slow
process--especially if it's run 100,000 times. 

In Sample Answer 4, finding a translation for a parameterized word is done
through simple assignment and return. There is no need to iterate through 
each dictionary from the beginning every time, because the dictionaries are
initially defined in such a way that every word is essentially a key to a 
3-string tuple of the corresponding translations. That way, all the program
has to do is find the parameterized word in the 'fm' dictionary and return 
its proper 'to' value translation.

In summary, Sample Answer 2 is a lot slower than Sample Answer 4, because 
Sample Answer 2 requires an iteration from the start of the dictionary until 
it finds a match, while Sample Answer 4 simply returns the value of the key
(the key is the word to be translated). Although it might not be as noticeable
with just one or two method calls of func_to_measure(), doing so 100,000 times
results in a significant time difference: over a minute and a half.

"""
