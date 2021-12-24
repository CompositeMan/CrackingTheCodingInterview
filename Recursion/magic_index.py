#A magic index in an array A[ 0 ... n -1] is defined to be an index such that A[ i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.


def magic_index(arr):
	n = len(arr)
	if n == 0:
		raise ValueError("Array is empty!")

	if n == 1:
		return 0 if arr[0] == 0 else -1

	for i in range(n):
		elm = arr[i]
		if elm == i:
			return i
		elif elm > i:
			#i = arr[i] # if they are not distinct 
			i = elm + 1

	return -1


def test():
	l = list(range(-10,20,2))
	#print(l)
	i = magic_index(l)
	assert i == 10
	#print(i)

def e_test():
	l = []
	try:
		i = magic_index(l)
	except Exception as e:
		print(e)

def z_test():
	l = [0]	
	i = magic_index(l)
	assert i == 0

	l = list(range(10))
	i = magic_index(l)
	assert i == 0

if __name__ == "__main__":
	test()
	e_test()
	z_test()
