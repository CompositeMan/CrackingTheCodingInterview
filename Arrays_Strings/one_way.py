# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
#Given two strings, write a function to check if they are one edit (or zero edits) away.


# Just like the permutation examples, one edit away is actually len(opts) <= 1 check. 

def one_or_zero_edit_away(a, b):
	l_a, l_b = len(a), len(b)
	
	if abs(l_a - l_b) > 1:
		return False
	
	l,s = (a,b) if l_a > l_b else (b,a)
	diff = False
	
	l_s = min(l_a, l_b)
	# if they are of same length, this does not work.
	for i in range(l_s):
		if s[i] != l[i+diff]:
			if diff:
				return False
			else:
				diff = True
	
	return True	


def test(a="pale", b="ple", ans=True):
	r = one_or_zero_edit_away(a,b)
	print(r)
	assert r == ans	


if __name__ == "__main__":
	test()
	test("pales", "pale")
	test("pale", "bale")	
	test("pale", "bake", False)
	
	


