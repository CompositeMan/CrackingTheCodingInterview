#Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.i


# For that to work, this function should be a member function of the LinkedList or the LinkedList must be circular. 
# I assume that this function should be member function thus will take the head as a parameter too.

from ll import LinkedList as LL

def del_from(head, mid):
	if head == None or head.next == None:
		raise ValueError(f"Head({head == None})or its next({head.next == None}) cannot be None for there to be a middle element")
	if head == mid:
		raise ValueError(f"Node to be deleted cannot be the head")

	t = head.next
	prev = head 

	while t.next != None:	
		if t == mid:
			prev.next = t.next 
			return
		t = t.next
	if t == mid:
		raise ValueError(f"Node to be deleted cannot be the tail")
		
	raise ValueError(f"Middle element cannot be found")



def test():
	ll = LL()
	mid = None
	last = None
	for i in range(15):
		ll.add(i)
		if i == 9:
			mid = ll.find(i)
			print(f"mid : {mid!=None}")
		elif i == 14:
			last = ll.find(i)

	
	ll.print()

	del_from(ll.head, mid)
	print(f"Deleted from the mid ", end="")
	ll.print()
	print(f"Attempting to delete the head ", end="")
	try:
		del_from(ll.head, ll.head)
		 
	except Exception as e:
		print(f"Exception caught: {e}")
	print(f"Attempting to delete the tail ", end="")
	try:
		del_from(ll.head, last)
		 
	except Exception as e:
		print(f"Exception caught: {e}")
	

test()
	

