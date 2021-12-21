def is_pow_2(num):
	if num == 0:
		return False
	return ( num & (num-1) ) == 0


def test():
	assert is_pow_2(2 ** 8) == True
	assert is_pow_2(2 ** 9) == True
	assert is_pow_2( (2 ** 9) - 1) == False
	assert is_pow_2( 1 ) == True
	assert is_pow_2( 20 ) == False
	assert is_pow_2( 0 ) == False



test()
