# Zadanie 11. c)

n = int(input('Podaj ktory wyraz ciagu: '))
a = -10
b = -5

for x in range(n-1):
    a -= b
    b = a/2

print(f'{n}. wyraz ciagu: {a}')