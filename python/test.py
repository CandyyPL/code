data = ['aa123', 'bb22', 'cc123']

# Take from 'data' list all values that have '123' and create list 'new' with them
new = [x for x in data if '123' in x]

print(new)