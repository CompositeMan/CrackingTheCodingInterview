#Given an array of positive integers, remove the duplicates without additional data structures, with O(1) space 
# there are couple of solutions :
# 1) if the biggest element in the array is always smaller than the length of the array
# We can check if this is the case in O(n), find max and check if the length of the array is bigger than it. 
def rem_dups(arr):
	mod = len(arr)
	if mod <2:
		return 
	dup_val = arr[0]

	for i in range(mod):
		index = abs(arr[i])
		if arr[index] > 0:
			arr[index] *= -1
		else:
			#duplicate found, for now it is just going to be equal to the first elm of the array
			arr[i] = dup_val
	
	# We can merge the sign reversing and shifting 
	for i in range(mod):
		arr[i] = abs(arr[i])
	
	shift(arr)

def shift(arr):
	here = 1
	dup_marker = arr[0]
	for i in range(1, len(arr)):
		if arr[i] != dup_marker:
			if here != i:
				arr[here] = arr[i]
			here += 1
			
	while here < len(arr):
		arr[here] = None			
		here += 1			
	

def test(r = 100):
	from random import randint, seed
	seed(9)
	l = [None]*r
	for i in range(r):
		l[i] = randint(0,r-1)
	print(f"List before removing duplicates : {l}")
	rem_dups(l)
	print(f"List after removing duplicates : {l}")
	
	
test(10)




	
