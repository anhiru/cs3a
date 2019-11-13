""" translate the 1000 most common words in English, Spanish, Greek """

from timeit import default_timer as timer

# read eng/span/greek .txt files
with open('1kwords.en.txt', encoding='utf-8') as f:
    enl = f.read().splitlines()

with open('1kwords.sp.txt', encoding='utf-8') as f:
    spl = f.read().splitlines()

with open('1kwords.gr.txt', encoding='utf-8') as f:
    grl = f.read().splitlines()


def translate(fm, to, word):
    if fm == 'en': 
        d = den
    elif fm == 'sp': 
        d = dsp
    else: 
        d = dgr

    if to == 'en': 
        index = 0
    elif to == 'sp': 
        index = 1
    else: 
        index = 2
        
    try:
        translation = d[word][index]
    except KeyError:
        translation = ''   # '<no word>'
    return translation


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


wlist = list(zip(enl, spl, grl))

den = {}  # empty dict
dsp = {}  # empty dict
dgr = {}  # empty dict

#  first you look it up in English to get the key
#  once you have the key, look it up in the dict for that language

for t in wlist:
    den[t[0]] = ('', t[1], t[2])
    dsp[t[1]] = (t[0], '', t[2])
    dgr[t[2]] = (t[0], t[1], '')

print('starting timer')
start = timer()
for i in range(1000000):
    func_to_measure()
end = timer()

elapsed = end - start
print('10M words translated in', elapsed, 'secs')
# print('1000 words takes', elapsed/10000, 'secs')


""" ------------------- SAMPLE RUN -------------------

starting timer
10M words translated in 3.492795118 secs


---------------------- END SAMPLE RUN ---------------- """
