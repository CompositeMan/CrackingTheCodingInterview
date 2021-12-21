#Write a function to determine the number of bits you would need to flip to convert integer A to integer B.


#Input: 29 (or: 11101), 15 (or: 01111)
#Output: 2

# basically it is the number of different bits, XOR is the way to go


def num_of_bits_to_convert(a, b):
	if type(a) != type(b):
		a,b = normalize(a,b)
		return bin_repr(a,b)	
	if isinstance(a, str) and isinstance(b, str):
		return bin_repr(a,b)
	diff = a^b
	diff = bin(diff)[2:]
	c = 0
	for ch in diff:
		if ch == "1":
			c += 1
	return c
def normalize(a,b):
	if isinstance(a, int):
		return bin(a)[2:], b
	elif isinstance(b, int):
		return a, bin(b)[2:]
	else:
		return a,b	

def bin_repr(a,b):
	l = len(a)
	if l != len(b):
		raise ValueError(f" {a}  and {b} are not of same length")

	c = 0
	for i in range(l):
		if a[i] != b[i]:
			c += 1

	return c

def test(a=29,b=15, ans=2):
	r = num_of_bits_to_convert(a, b)
	assert r == ans



if __name__ == "__main__":	
	test()
	test(29, "01111")
	test("11101", 16, 3)
	test(10, 10, 0)
	test(10, 11, 1)
