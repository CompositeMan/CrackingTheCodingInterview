
def mergesort(arr):
	l = len(arr)
	helper = [None]*l 
	merge_sort(arr, helper, 0, l-1)

def merge_sort(arr, h, low, high):
	if low < high:
		mid = (low+high)//2
		merge_sort(arr, h, low, mid) 
		merge_sort(arr, h, mid+1, high)
		merge(arr, h, low, mid, high)

def merge(arr,h, low, mid, high):
	for i in range(low, high+1):
		h[i] = arr[i]

	h_left = low
	h_right = mid+1
	current = low

	while h_left <= mid and h_right <= high:
		if h[h_left] <= h[h_right]:
			arr[current] = h[h_left]
			h_left += 1

		else:
			arr[current] = h[h_right]
			h_right += 1

		current += 1

	#Copy the rest of the left side 
	remaining = mid - h_left
	for i in range(remaining+1):
		arr[current+i] = h[h_left+i]
	

def test():
	from random import randint
	SIZE = 200
	l = [None]*SIZE
	for i in range(SIZE):
		l[i] = randint(-SIZE, SIZE)
	#print(l)	
	mergesort(l)
	#print(l)	
	
	for i in range(1,SIZE):
		if l[i-1] > l[i]:
			print(f"Merge sort does not work.")

	
if __name__ == "__main__":
	test()
