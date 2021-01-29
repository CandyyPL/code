# Zadanie 10.1 a)

n = int(input('Podaj ile wyrazow: '))
a = -300
r = 0

for x in range(n):
    r += a
    a /= 10

print(r)