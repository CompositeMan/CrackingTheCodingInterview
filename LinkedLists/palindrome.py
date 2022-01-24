from sys import path
path.append("..")

from ll import LinkedList, Node

def pal_ll(head)->bool:
	if not head:
		raise ValueError("Linkedlist is empty!")
	if not head.next:
		return True

	t = head
	r = head
	stack = []
	while r and r.next:
		r = r.next.next
		stack.append(t.val)	
		t = t.next
	
	if r:
		t = t.next
	#print(f"Stack : {stack}")	
	while len(stack) > 0 and t :
		v = stack.pop( len(stack) - 1 )
		#print(f" t.val {t.val} , v {v}")
		if t.val != v:
			return False
		t = t.next

	return (len(stack) == 0)&(not t)


def test(l, a=True):
	ll = LinkedList()
	for e in l:
		ll.add(e)

	#ll.print()
	r = pal_ll(ll.head)
	assert r == a
	#print(f"TEST Passed ")
	

if __name__ == "__main__":
	l = [1,2,3,0,3,2,1]
	test(l)	
	l = [1,2,3,3,2,1]
	test(l)	
	l = [1,2]
	test(l, False)	
	l = [1]
	test(l)	
	l = []
	try:
		test(l)	
	except Exception as e:
		print(f"Exception caught : {e}")
