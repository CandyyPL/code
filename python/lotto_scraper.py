import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print('version error: use python 3.0 or higher')

from bs4 import BeautifulSoup
from requests import get

url = 'https://megalotto.pl/wyniki/lotto/losowania-od-1-Stycznia-1957-do-12-Stycznia-2021'

site = get(url)
bsed = BeautifulSoup(site.content)

main_list = bsed.find('div', class_='lista_ostatnich_losowan')

i = 0
s = ''
for roll in main_list:
    ns = ((roll.get_text()[16:])[:-8]).rstrip()
    s += ns + ' '

lst = s.split(' ')
del lst[-1]

l = []

for x in range(1, 50):
    c = lst.count(str(x))
    t = (str(x), c)
    l.append(t)

ls = sorted(l, key=lambda tup:(-tup[1], tup[0]))

cn = 1
for x in ls:
    print(f'{cn}. {x[0]}\t:\t{x[1]}')
    cn += 1