import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print('version error: use python 3 or higher')

from datetime import date

curr = date.today()

a = input('Podaj swoje imie: ')
b = input('Podaj swoj rok urodzenia: ')

print(f'{a}, masz {curr.year - int(b)}')