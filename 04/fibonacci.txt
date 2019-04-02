nterms = int(input("kolikrat?"))

n1 = 0
n2 = 1
count = 0

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return (fibonacci(n-1) + fibonacci(n-2))