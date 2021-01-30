# Zadanie 11. c)

n = int(input('Podaj ktory wyraz ciagu: '))
a = 0.2

for x in range(n-1):
    a *= -3

print(f'{n}. wyraz ciagu: {round(a, 2)}')