# Zadanie 10.1 b)

n = int(input('Podaj ile wyrazow: '))
a = 0.3
r = 1

for x in range(n):
    r *= a
    a *= 2

print(r)