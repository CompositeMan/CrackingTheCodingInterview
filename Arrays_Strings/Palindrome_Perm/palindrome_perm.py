""" 
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

# For a palindrome, I need some characters occuring at least twice in the string. There are 2 cases: len(palindrome) % 2 = 0 or 1. In case 0, there should be no chars such that its occurence is an odd number (1 or 3 ... 2k+1. In case 1, there should only be one character that has the occurence 1. 

def palindrome_perm(s):
	characters = dict()

	for ch in s:
		ch = ch.lower()
		if ch == " ":
			continue
		add_mod_2(characters, ch)

	if len(characters.keys()) > 1:
		return False
	return True
		
		

def add_mod_2(d, ch):
	if ch in d.keys():
		if d[ch] == 1:
			d.pop(ch)
	else:
		d[ch] = 1



def test(s = "Tact Coa", ans=True):
	r = palindrome_perm(s)
	assert r == ans

if __name__ == "__main__":
	test()
	test("what is si what")
	test("I am unique", False)
	test("ppaalliinnddrroommee")
