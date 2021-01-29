# Zadanie 10.1 c)

n = int(input('Podaj ile wyrazow: '))
a = 7
r = 7

for x in range(3, n+2):
    if x % 3 == 0:
        a += 2
    else:
        a += 1

    r += a

print(r)