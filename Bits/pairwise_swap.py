from math import log2, ceil
from bit_ops import clear_bit
def pairwise_swap(num):
	l = num >> 1
	r = num << 1

	
	length = ceil(log2(num))		
	#mask = ~(1 << length)
	#r &= mask
	r = clear_bit(r, length)	
	
	#print(f"length: {length}")
	#print(f"l: {bin(l)[2:]}")
	#print(f"r: {bin(r)[2:]}")
	
	return l|r

def test(num=11):
	bar = "*" * 100
	print(bar)
	b = bin(num)[2:]
	print(b)

	s = pairwise_swap(num)

	b_s = bin(s)[2:]
	print(b_s)
	print(bar)


if __name__ == "__main__":
	test()
	for i in range(1,10):
		test(i)
		
