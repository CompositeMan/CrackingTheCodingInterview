#Given two sorted arrays, find the number of elements in common. The arrays are the same length and each has all distinct elements
#using the BCR : BCR is O(N) since we have to "touch" all the elements in the arrays.

#Complexity Analysis : time : O(n), space : O(1)
def commons(a, b):
	# for each element in a, since we know that both are sorted, we can have a linear look up, and remember where we stoppped, to continue afterwards from that point
	if len(a) == 0 or len(b) == 0:
		return 0
	num_coms = 0
	#coms = []
	stopped_at= 0
	l_b = len(b)
	for e_a in a:
		for i in range(stopped_at, l_b):
			if e_a == b[i]:
				num_coms += 1
				#coms.append(e_a)
			elif e_a < b[i]:
				stopped_at = i
				break
	return num_coms




def test( a = [13, 27, 35, 40, 49, 55, 59], b = [17, 35, 39, 40, 55, 58, 60], ans=3 ):
	#print(f"a:{a}\nb:{b}")
	c = commons(a,b)
	assert c == ans

if __name__ == "__main__":
	test()
	test([10, 13, 23,45,49], [10, 11, 13, 24,25, 26, 44, 49])
	
