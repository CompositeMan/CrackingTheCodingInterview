from bit_ops import get_bit, set_bit, clear_bit, clear_bits_MS_through, clear_bits_0_through,update_bit
def get_bin(num, l):
	f_str = "{0:0"+str(l)+"b}"
	return f_str.format(num)
 

def test_get_bit(a, i):
	pos = i+1
	s = int(get_bit(a,i))
	a = get_bin(a, pos)	
	comp = int(a[-pos])
	assert s == comp 

def test_set_bit(a, i):
	n = set_bit(a, i)
	pos = i+1
	a = get_bin(a, pos)
	a = list(a)
	a[-pos] = '1'
	a = ''.join(a)
	assert a == get_bin(n, pos)

def test_clear(a, ith):
	n = clear_bit(a, ith)
	pos = ith+1
	a = get_bin(a, pos)
	a = list(a)
	a [-pos] = "0"
	a = ''.join(a)
	assert a == get_bin(n, pos)	

def test_clear_MS_through(a, i):
	#print(f"{a} {i} bits  ", end="")
	n = clear_bits_MS_through(a, i)
	pos = i + 1
	a = get_bin(a,pos)
	a = "0" + a[len(a) -i:]
	n = get_bin(n, pos)

	#print(f"n:{n} , a: {a}")
	assert n == a

def test_clear_0_through(a,i):
	n = clear_bits_0_through(a, i)
	from math import log2
	pos = int(log2(a))
	if pos == i or a == 1:
		assert 0 == n
		return
	a = get_bin(a, pos)
	zs = "0" * (i+1)
	a = a[:-i-1] + zs
	if "1" not in a:
		a = "0"
	n = get_bin(n, pos)

	assert a == n 	

def test_update(a, i, to):
	n = update_bit(a,i,to)
	s = set_bit(a,i) if to == 1 else clear_bit(a, i)
	assert n == s

def tests_of_get():
	test_get_bit(4, 2)
	test_get_bit(1, 1)
	test_get_bit(1, 0)
	test_get_bit(0, 0)
	test_get_bit(2, 0)
	test_get_bit(2, 1)
	test_get_bit(2, 2)

def tests_of_set():
	test_set_bit(0,0)
	test_set_bit(4,0)
	test_set_bit(4,1)
	test_set_bit(4,2)
	test_set_bit(0,1)
	test_set_bit(0,2)
	test_set_bit(4,3)

def tests_of_clear():
	test_clear(4,2)
	test_clear(0,2)
	test_clear(4,1)
	test_clear(1,2)
	test_clear(1,1)
	test_clear(4,8)
	test_clear(8,7)

def tests_of_clear_bits():
	test_clear_MS_through(12, 2)
	test_clear_MS_through(4, 2)
	test_clear_MS_through(63, 2)
	test_clear_MS_through(1, 1)
	test_clear_MS_through(2, 2)

	test_clear_0_through(8,2)
	test_clear_0_through(4,2)
	test_clear_0_through(63, 2)
	test_clear_0_through(1, 1)
	test_clear_0_through(2, 2)

def tests_of_update():
	test_update(4, 2, 0)
	test_update(4, 1, 1)
	test_update(3, 2, 1)
	test_update(12, 3, 0)
	test_update(6, 2, 0)
	test_update(4, 3, 1)


if __name__ == "__main__":

	#tests_of_get()
	#tests_of_set()
	#tests_of_clear()
	#tests_of_clear_bits()
	tests_of_update()
	

