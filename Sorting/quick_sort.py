
def quick_sort(arr, left, right):
	index = partition(arr, left, right)
	if left < index-1:
		quick_sort(arr, left, index-1)	
	if index < right:
		quick_sort(arr, index, right)

def partition(arr, left, right):
	pivot = arr[(left+right)//2] 
	while left <= right:
		while arr[left] < pivot:
			left += 1
		while arr[right] > pivot:
			right -= 1


		if left <= right:
			swap(arr, left, right)
			left += 1
			right -= 1

	return left



def swap(arr, l ,r):
	t = arr[l]
	arr[l] = arr[r]
	arr[r] = t

	

def test():
	from random import randint
	SIZE = 200
	l = [None]*SIZE
	for i in range(SIZE):
		l[i] = randint(-SIZE, SIZE)
	print(l)	
	quick_sort(l,0, SIZE-1)
	print(l)	
	
	for i in range(1,SIZE):
		if l[i-1] > l[i]:
			print(f"Merge sort does not work.")

	
if __name__ == "__main__":
	test()
