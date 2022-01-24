# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
#Given two strings, write a function to check if they are one edit (or zero edits) away.


# Just like the permutation examples, one edit away is actually len(opts) <= 1 check. 

def one_or_zero_edit_away(a, b):
	l_a, l_b = len(a), len(b)
	
	if abs(l_a - l_b) > 1:
		return False
	
	l,s = (a,b) if l_a > l_b else (b,a)
	i_1 = 0
	i_2 = 0
	diff = False	

	while i_1 <  len(s) and i_2 <  len(l):
		if s[i_1] != l[i_2]:
			if diff:
				return False
			else:
				diff = True
				if l_a == l_b:
					i_1 += 1
		else:
			i_1 += 1
		i_2 += 1
	
	return True		

def test(a="pale", b="ple", ans=True):
	r = one_or_zero_edit_away(a,b)
	#print(r)
	assert r == ans	


if __name__ == "__main__":
	test()
	test("pales", "pale")
	test("pale", "bale")	
	test("pale", "bake", False)
	test("pake", "bake")
	test("pake", "bak", False)
	
	


