# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

#EXAMPLE
#Input: "Mr John Smith ", 13 
# Output: "Mr%20John%20Smith"

# With the replacement of " " with "%20", the array size will be growing with an increase of num_of_spaces*2. 
# First I will count the spaces. I thought of storing them but it will increase my space commplexity, rather that that, after I make my array bigger, I will start to shift them
# If I  see a space I will insert %20 instead and continue. 

# PS
#  In python, list is already an arraylist i.e. a growable array, I will treat it as it is not and perform operations accordingly.

from typing import List

SPACE = " "

def replace_spaces( s:List[str], w="%20"):
	if not isinstance(s, list):
		raise ValueError(f"s should be a list, not {type(s)}")

	if len(s) == 0:
		return s

	space_count = 0

	for i in s:
		if i == SPACE:
			space_count += 1

	# I will grow by space_count*3 - space_count (since I am removing the spaces, I will lose space_count of length)
	# Every time a list reaches its limits, python grows the list by its old size * 2. I am not going to do that, I will just allocate enough space

	replaced = [""] * (len(s)+space_count*2) 
	index = -1
	l_w = len(w)
	while len(s) > 0:
		ch = s.pop(-1)
		if ch == SPACE:
			for i in range(1, l_w+1):
				replaced[index]	= w[-i]
				index -=1

		else:
			replaced[index] = ch
			index -= 1 


	return replaced


def test(s = "Mr John Smith ", w = "%20"):
	r = replace_spaces(list(s),w)
	assert "".join(r) == s.replace(SPACE, w)
if __name__ == "__main__":
	test()
	test("", "%20")
	test("   ", "%20")
	test("CemTunaboylu", "%20")



