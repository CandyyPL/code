import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print('version error: use python 3 or higher')

import math

if sys.argv[1] == '-l':
    tm = int(sys.argv[2])

    last = 1
    curr = 1
    new = 0

    print('1. 1')
    print('2. 1')

    for x in range(tm-2):
        new = curr + last
        last = curr
        curr = new
        print(f'{x+3}. {new}')

elif sys.argv[1] == '-g':
    tm = int(sys.argv[2])

    last = 1
    curr = 1
    new = 0

    for x in range(tm-2):
        new = curr + last
        last = curr
        curr = new

    print(f'The most precise golden proportion = {curr / last}')