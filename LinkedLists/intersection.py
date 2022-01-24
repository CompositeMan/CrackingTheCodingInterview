from ll import LinkedList

def intersection(head_1, head_2):
	if not head_1 or not head_2:
		raise ValueError(" one of the heads are null!")

	len_1, len_2 = 0,0
	last_1 = head_1
	last_2 = head_2

	while last_1:
		last_1 = last_1.next
		len_1 += 1
	while last_2:
		last_2 = last_2.next
		len_2 += 1

	if last_1 != last_2:
		return None

	trim = None
	if len_1 != len_2:
		long, short, l,s = (head_1, head_2, len_1, len_2) if len_1 > len_2 else (head_2, head_1, len_2, len_1)
	
	while l != s:
		long = long.next
		l -= 1

	while long != short:
		long = long.next
		short = short.next

	return short

DEBUG = False #True	
	
def test(l1, l2, l3):
	h_1 = LinkedList()
	h_2 = LinkedList()
	h_3 = LinkedList()
	for e in l1:
		h_1.add(e)

	for e in l2:
		h_2.add(e)

	for e in l3:
		h_3.add(e)

	t_1 = h_1.head
	t_2 = h_2.head
	
	while t_1.next:
		t_1 = t_1.next
	while t_2.next:
		t_2 = t_2.next

	t_1.next = h_3.head
	t_2.next = h_3.head

	if DEBUG:
		h_1.print()
		h_2.print()

	r = intersection(h_1.head, h_2.head)
	if DEBUG:
		print(F"PASSED : {r == h_3.head}")
	assert r == h_3.head

if __name__ == "__main__":
	l1 = list(range(6,12))
	l1.reverse()

	l2 = list(range(6,9))
	l2.reverse()
	
	l3 = list(range(6))
	l3.reverse()

	test(l1,l2,l3)
	
		
		
