# Write a function to swap a number in place (that is, without temporary variables)
"""
a>b
a=-1  b=-9
a=-10 b=a-b=-1
a-=b=-9

a>b
a=100,b=10
a=110, b=110-10=100
a-=b=-1

a<b
a=-9, b=-1
b=-10, a=b-a=-1
b=-9

a<b
a=10, b=100
b=110, a=b-a=100
b-=a
"""

def swap(a, b):
	if a == b:
		return a,b
	if a < b:
		b += a
		a = b-a
		b -= a
	else:
		a += b
		b = a-b
		a -= b
	

	return a,b

def swap_w_xor(a, b):
	a = a^b
	b = a^b
	a = a^b
	return a,b

def test(a, b, f=swap): 
	p_a, p_b = a, b
	a,b = f(a,b)
	assert a == p_b
	assert b == p_a

if __name__ == "__main__":
	test(100,0)
	test(0,100)
	test(10,10)
	test(-1, -9)
	test(-9, -1)
	
	test(100,0,swap_w_xor)
	test(0,100, swap_w_xor)
	test(10,10, swap_w_xor)
	test(-1, -9, swap_w_xor)
	test(-9, -1, swap_w_xor)
		
