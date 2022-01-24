# Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.

# Some information : 
# Think of Unicode as a massive version of the ASCII table—one that has 1,114,112 possible code points. That’s 0 through 1,114,111, or 0 through 17 * (2^16) - 1 
#, or 0x10ffff hexadecimal. In fact, ASCII is a perfect subset of Unicode. The first 128 characters in the Unicode table correspond precisely to the ASCII characters 
# that you’d reasonably expect them to.

# Assuming the strings we receive are UTF-8. If not, we should be given the formatting. s1 and s2 should be of same encoding.

def perm_check(s1, s2):
	if len(s1) != len(s2):
		return False

	xor_1 = 0
	xor_2 = 0
	for i in range(len(s1)):
		xor_1 ^= ord(s1[i])
		xor_2 ^= ord(s2[i])

	return xor_1 == xor_2

def test(a,b, s=True):
	r = perm_check(a,b)
	assert s == r

if __name__ == "__main__":
	a = "aeᮈ"
	b = "ᮈea"
	test(a,b)
	
	a = "記者鄭啟源羅智堅"
	b = "源羅智堅記者鄭啟"
	test(a,b)

	a = "smiley😧"
	b = "sm😧iley"
	test(a,b)

	a = "open mouth"
	b = "😧"
	test(a,b,False)
	
	a = "記者鄭啟源羅智"
	b = "源羅智堅記者鄭"
	test(a,b, False)
	
	a = "記者啟源羅智堅"
	b = "源羅a堅記者啟"
	test(a,b,False)
	
	a = "記者啟羅智堅"
	b = "源羅智堅記者啟"
	test(a,b,False)

	a = 'αβγδεζηθικλμνξοπρςστυφχψ'	
	b = 'αβγδεζηθικλμνξοπρςστυφχψ'
	b = list(b)
	b.reverse()
	b = "".join(b)
	test(a,b)	
