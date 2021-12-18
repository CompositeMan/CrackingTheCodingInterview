# Design an algorithm to print all permutations of a string. For simplicity, assume all cha r ­ acters are unique

PERMS = []
TEST = False
# Complexity analysis : 
def perms(word, side=""):
	
	if word == "":
		print(side, end=", ") # O(n)
		if TEST:
			global PERMS
			PERMS.append(side)
	l = len(word)
	for c in range(l): # O(n)
		r = word[:c] + word[c+1:] #O(n)->string concatenation takes O(n).  
		perms(r, side+word[c]) # now it gets n-1

# So, n for loop, followed by n-1 for loops (how many? -> n many), then n-2 for loops which are again n-1 many. 
# n(n-1)(n-2)...1 = n! many perms calls. These are the leaves of the call tree. How about the path from the root to that leaf? The length of the path is n. So the number of all nodes in the tree will be the number of all the calls that we make
# So we will have at most n.n! nodes. Printing the string also takes O(n) when we are at the leaves. If we are not in the leaves yet, string concat. takes O(n) too, thus we may now see that every node in our tree takes O(n).
# So to sum up, we are calling perms in total of n.n! times, with O(n) work at each node. Thus the total run time is : O(n^2 . n!).    
# What about space?  We only are on one branch at a time to a leaf, thus we will have the stack space from the calls until the leaf which is O(n). Concatenation may create a new string which will also cost O(n), thus O(n) space in total. 
	
def test():
	from itertools import permutations
	global TEST
	TEST  = True 
	s = "abc"
	perms(s)
	p = list(permutations(s))
	p = [ "".join(tup) for tup in p ]
	
	assert check_sol(p)==False
	#print(f"\npermutations : {p}")
	
def check_sol(ans):
	d_a = set()
	for a in ans:
		d_a.add(a)
	oh_shit = False
	for s in PERMS:
		if s not in d_a:
			print(f"{s} from solution is not in answers {d_a}")		
			oh_shit = True

	return oh_shit


if __name__ == "__main__":
	test()
