
def get_bit(num, ith):
	return ( (1 << ith) & num) != 0

def set_bit(num, ith):
	return (1 << ith) | num
def clear_bit(num, ith):
	mask = ~(1 << ith)
	return mask & num

def clear_bits_MS_through(n, i):
	mask = (1 << i) - 1
	return n & mask

def clear_bits_0_through(n,i):
	mask = (-1 << (i+1)) # since it is in 2s complement form it will be all ones in MS side
	return n & mask
def update_bit(n, i , to):
	mask = ~(1 << i)
	return (n & mask) | (to << i)




