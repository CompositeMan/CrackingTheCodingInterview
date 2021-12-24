#Write a method to return all subsets of a set.
i

# Proper Subsets - excluding itself except array is empty
# Buttom-Up
def power_set(s): # Assuming it is a set, no set checks
	n = len(s)
	# using None as the empty set
	elif n <= 1:
		return [None] 

	subsets = [None] * ( (2**n)-1)
	i = None
	for i in range(n):
		subset[i+1] = s[i]

	 
		
		
		
