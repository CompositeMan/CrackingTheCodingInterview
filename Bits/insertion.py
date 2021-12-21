from bit_ops import *

from math import log2

def insert(m,n,i,j):
	#I assume that len(bin(m)) = j-i+1
	gap = j-i+1
	l = int(log2(m)) + 1
	if l != gap:
		raise ValueError(f" LOG:{l} The gap {gap} btw. {j} and {i} is too big for {m} ")

	for k in range(gap):
		n = update_bit(n, i+k, get_bit(m,k))
	return n 



#N 1 000 000 000 0, M 10011, i 2, j 6

def test():
	n = (1 << 10)
	m = (1 << 4) + 3

	i,j = 2,6

	try:
		rep = insert(m,n,i,j)
		r_b = bin(rep)[2:]
		assert r_b == "10001001100"

	except Exception as e:
		print(e)

def test_(n,m,i,j):
	r = insert(m,n,i,j)
	
	n = bin(n)[2:]
	m = bin(m)[2:]
	
	n = list(n)
	for k, ch in enumerate(m):
		n[-i-k] = ch

	n = ''.join(n)
	r = bin(r)[2:]

	#print(f" r : {r} and n : {n} ")
	assert r == n

if __name__ == "__main__":
	test()
	test_(127, 8, 2, 5)
