import sys
sys.path.append("..")
from ll import LinkedList

def rem_dup_no_buffer(head):
	if not head or not head.next:
		return head

	cur = head
	while cur:
		runner = cur.next
		prev = cur
		while runner:
			if runner.val == cur.val:
				prev.next = runner.next
				runner = prev.next
			else:
				if runner.next:
					prev = runner
					runner = runner.next
				else: # runner.next = None
					break
		if not cur.next:
			break
		cur = cur.next

	return head


from random import randint, seed

def test_random():
	ll = LinkedList()
	for i in range(15):
		ll.add(randint(0,3))	

	ll.print()
	ll.head = rem_dup_no_buffer(ll.head)
	ll.print()
	s = "*" * 100
	print(s)

def test(r):
	ll = LinkedList()
	for i in r:
		ll.add(i)

	ll.print()
	ll.head = rem_dup_no_buffer(ll.head)
	ll.print()
	s = "*" * 100
	print(s)

if __name__ == "__main__":
	seed(0)
	test_random()
	test_random()
	
	r = [9,8,7,7,8,9,1,2,3,2,2,2,2,3,3,3]
	print(r)
	test(r)
	r = []
	print(r)
	test(r)

	r = [1, 1]
	print(r)
	test(r)

	r = [1,2,3]
	print(r)
	test(r)



