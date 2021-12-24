EMPTY = 0
def nth_fibonacci(n, mem):
	if n < 2: # 1st and 2nd are 0, 1 respectively
		return n
	m = mem[n]
	if m != EMPTY:
		return m
	else:
		m = nth_fibonacci(n-1, mem) + nth_fibonacci(n-2,mem)
		mem[n] = m
		return m

def fibonacci(n):
	memo = [EMPTY] * (n+1)
	return nth_fibonacci(n, memo)



def test(n):
	f = fibonacci(n)
	return f


for i in range(2,15):
	print(test(i), end=" ")

print()
	
