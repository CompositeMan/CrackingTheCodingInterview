#Write code to remove duplicates from an unsorted linked list.

from ll import LinkedList
"""
-> 3 -> 3 -> 0 -> 2 -> 3 -> 3 -> 2 -> 3 -> 2 -> 1 -> 1 -> 2 -> 1 -> 0

prev = 2
t = 2

"""

def remove_dup(head):
	if head == None or head.next == None:
		return  head

	buffer = set()

	buffer.add(head.val)
	t = head.next # this exists because we checked that above
	prev = head
	while t.next != None:
		v = t.val
		if not v in buffer:
			buffer.add(v)
			prev = prev.next
		else:
			prev.next = t.next
		
		t = t.next
			
	if t.val in buffer:
		prev.next = None

	
				
	return head

from random import randint, seed

def test_random():
	ll = LinkedList()
	for i in range(15):
		ll.add(randint(0,3))	

	ll.print()
	ll.head = remove_dup(ll.head)
	ll.print()
	s = "*" * 100
	print(s)
def test(r):
	ll = LinkedList()
	for i in r:
		ll.add(i)

	ll.print()
	ll.head = remove_dup(ll.head)
	ll.print()
	s = "*" * 100
	print(s)
		

if __name__ == "__main__":
	seed(0)
	test_random()
	test_random()
	
	r = [9,8,7,7,8,9,1,2,3,2,2,2,2,3,3,3]
	test(r)
	r = []
	test(r)

	r = [1, 1]
	test(r)

	r = [1,2,3]
	test(r)












