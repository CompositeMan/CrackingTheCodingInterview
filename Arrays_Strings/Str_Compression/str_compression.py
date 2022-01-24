# Implement a method to perform basic string compression using the counts of repeated characters. 
#For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).



def compress(s):
	l = len(s)
	if l == 0:
		return s 
	comp = [""] * l

	left = 0
	comp[0] = s[0]
	counter = 1
	for runner in range(1,l):
		
		if s[runner] == comp[left]:
			counter += 1

		else:
			if left >= l-2:
				return s
			comp[left+1] = str(counter)
			comp[left+2] = s[runner]
			left +=2
			counter = 1

	if comp[left] == s[-1]:
		comp[left+1] = str(counter)	
			
	return "".join(comp)		
				

def test(s="aabcccccaaa", c="a2b1c5a3"):

	# print(s)
	r = compress(s)
	# print(r, len(r), "==", c, len(c))
	assert r == c

from string import ascii_lowercase

if __name__ == "__main__":
	test()
	test(ascii_lowercase, ascii_lowercase)
