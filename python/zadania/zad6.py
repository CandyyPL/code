# Zadanie 10.1 a, b

list = []

p = 1

while p <= 10000:
    n = int(input('Podaj liczbe != 0: '))

    if n != 0:
        list.append(n)

    p *= n

print(f'Ilosc liczb: {len(list)}')
print(f'Wartosc iloczynu: {str(p)}')