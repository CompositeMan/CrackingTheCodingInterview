#Implement an algorithm to find the kth to last element of a singly linked list.
from sys import path
path.append("..")

from ll import LinkedList as LL

# I solved this problem with a stack before. Now I want to try runner method to solve it O(n) time AND O(1) space
def kth_last(head, k):
	if head == None:
		raise ValueError("Head is None")
	if k == 0:
		raise ValueError(f"k must be at least 1 : k={k}")	
	far = 0
	near = 0
	
	s = head 
	m = head
	r = head

	while r.next != None and r.next.next != None:
		r = r.next.next
		m = m.next		
		far += 2
		near += 1
		
	if far < k:
		raise ValueError(f"LinkedList is shorter than {k}")

	start = None
	diff = 0
	if k < near:
		start = m
		diff = near - k 
	elif k == near:
		return m.val
	else:
		start = s 
		diff = far - k 
	
	while diff > 0:
		start = start.next
		diff -= 1

	return start.val
	
def test(k=10):
	ll = LL()
	r = 15
	for i in range(r):
		ll.add(i)

	ll.print()

	e = kth_last(ll.head, k)
	print(f"{k}th element : {e}")
	assert e == r-k-1

if __name__ == "__main__":
	test()
	test(3)
	test(13)
	test(1)
	test(14)
	try:
		test(15)
	except Exception as e:
		print(f"Exception is caught: {e}")


	try:
		test(0)
	except Exception as e:
		print(f"Exception is caught: {e}")


