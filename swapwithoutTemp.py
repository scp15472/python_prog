def swap (a,b):
	a = a + b
	b = a - b
	a = a - b
	print"Values of first and second number after swapping"
	return a,b

print swap(5,10)
