# Implement a method to perform basic string compression using the counts of repeated characters. 
#For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).



def compress(s):
	l = len(s)
	if l == 0:
		return s 
	comp = [""] * l

	left = 0
	ch = s[0]
	comp[0] = s[0]
	counter = 0
	for runner in range(l):
		if s[runner] == ch:
			counter += 1
		if runner < l-1:
			print(F"{runner} -> left: {left}")	
			comp[left] = ch 
			comp[left+1] = str(counter)
			counter = 1
			left += 2
			ch = s[runner]

	if ch == s[-1]:
		print(f"left is{left}")
		comp[left] = counter				
	print(comp)	

	if len(comp) == l:
		return s

	return "".join(comp)		
				


def test(s="aabcccccaaa", c="a2blc5a3"):

	r = compress(s)
	#print(r)
	assert r == c



test()
