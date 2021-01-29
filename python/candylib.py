def isPrime(n):
	n = int(n)

	if n <= 1:
		return False
	else:
		for m in range(2, n):
			if n % m == 0:
				return False
		return True

def primeFrom(lst):
	ret = []

	for element in lst:
		if isPrime(element) == True:
			ret.append(element)

	return ret

def nwd(a, b):
	while True:
		if a % b == 0:
			return b
		else:
			c = a % b
			a = b
			b = c

def nww(a, b):
	return (a*b) / nwd(a, b)

def root(s, p):
	return p ** (1.0/s)

def addAll(*args):
	r = 0

	for x in args:
		r += x

	return r

def multiplyAll(*args):
	r = 1

	for x in args:
		r *= x

	return r

def isLeap(y):
	if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
		print(True)
	else:
		print(False)