# For a palindrome, there are 2 cases : X|X or XcharX where Xs are symmetric to each other horizontally, char is any character.
# Assuming the string is UTF-8 encoded, there are 17*2^16 - 1 possible characters. This is more than 1 million.
# I cannot possibly have such an array, or that many bits to check palindromes. I have to use a hashset.

def palindrome_perm(s):
	if len(s) < 2:
		return True
	space = set()
	for ch in s:
		if ch == " ":
			continue
		ch = ch.lower()
		if ch in space:
			space.remove(ch)
		else:
			space.add(ch)

	return len(space) < 2 
		
def test(s = "Tact Coa", ans=True):
#	print(s, ans)
	r = palindrome_perm(s)
	assert r == ans

if __name__ == "__main__":
	test()
	test("what is si what")
	test("I am unique", False)
	test("ppaalliinnddrroommee")
	test("aeᮈ", False)
	test("aeᮈae", True)
	
	a = "記者鄭啟源羅智堅"
	test(a,False)

	a = "記者鄭啟源羅智堅記者鄭啟源羅智堅"
	test(a,True)

	a = "smile😧smile"
	test(a, True)

	a = "😧"
	test(a) 
	
	a = "源羅a堅記者啟"
	test(a,False)
	
	a = 'ααβγδεζηθικλμνξοπρςστυφχψβγδεζηθικλμνξοπρςστυφχψ'
	test(a)	
