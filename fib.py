n = 0
m = 1

def fib(n, m):
	if n > 1000:
		return 0
	print(m)
	return fib(m, n + m)


fib(n, m)