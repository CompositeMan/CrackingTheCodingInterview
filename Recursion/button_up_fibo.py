def nth_fibonacci(n):

	f_1 = 0
	f_2 =1
	
	for i in range(2, n):
		f_3 = f_1 + f_2
		f_1 = f_2
		f_2 = f_3

	return f_1 + f_2

def test(n):
	f = nth_fibonacci(n)
	return f


for i in range(2,15):
	print(test(i), end=" ")

print()
