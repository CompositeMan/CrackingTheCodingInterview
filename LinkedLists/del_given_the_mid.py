#Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

from ll import LinkedList as LL

def del_given(mid):
	if not mid:	
		raise ValueError(f"Node is None.")
	if not mid.next:
		raise ValueError(f"Node to be deleted cannot be the tail")
	mid.val = mid.next.val
	mid.next = mid.next.next
		

def test():
	ll = LL()
	last = None
	for i in range(15):
		ll.add(i)
		if i == 14:
			last = ll.find(i)

	ll.print()
	for i in range(5,10):
		mid = ll.find(i)
		del_given(mid)

	print(f"Deleted from the mid ", end="")
	ll.print()
		 
	print(f"Attempting to delete the tail ", end="")
	try:
		del_given(last)
		 
	except Exception as e:
		print(f"Exception caught: {e}")
	

test()
	

