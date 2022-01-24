#  Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Solving with additional data structure is easy -> hashset or array(counting sortish w/ booleans) DONE
#There is also a catch, we can return False immediately if the length of the string is greater than the number of available chars

CHAR_SPACE = 128 # ASCII

def is_unique(s):
	l = len(s)
	if l > CHAR_SPACE:
		return False
	arr = [False]*CHAR_SPACE

	for ch in s:
		o = ord(ch)
		if arr[o]:
			return False
		else:
			arr[o] = True

	return True

def test(s, a=True):
	r = is_unique(s)
	assert a == r

if __name__ == "__main__":
	test("main")
	from string import printable
	test(printable)
	test(printable+ "a", False)
	test("")
	test("aa", False)
	test("12")
	test("  ", False)

	 
# what about no additional data structure?
# it is same as finding a duplicate integer in a list -> chars are basically ord(ch) integers.

# without additional memory I can sort it, quicksort -> space O(logn)
# then go through the list


