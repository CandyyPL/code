n = int(input('Enter how many fibonacci numbers: '))

last = 0
curr = 1
new = 1

for x in range(n):
    print(f'{x+1}. {new}')
    new = curr + last
    last = curr
    curr = new