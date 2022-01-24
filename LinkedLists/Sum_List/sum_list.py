from sys import path

path.append("..")
from ll import LinkedList
from ll import Node 
def sum_list(h1, h2)->int:
	if not h1:
		return h2
	elif not h2:
		return h1
	
	carry = 0
	p1 = h1
	p2 = h2
	start = Node(-1) # Dummy 
	s_l = start
	prev = None	
	while p1 and p2:
		s = (p1.val + p2.val) + carry
		#print(f"sum : {s} w/ carry : {carry} ")
		carry = s//10
		#print(f"new carry  {carry} ")
		val = s%10
		#print(f"new val : {val} ")
		prev = s_l	
		s_l.next = Node(val)	
		s_l = s_l.next	
		p1 = p1.next
		p2 = p2.next 
		
	while p1:
		s = (p1.val) + carry
		carry = s//10
		val = s%10
		prev = s_l	
		s_l.next = Node(val)
		s_l = s_l.next	
		p1 = p1.next
	while p2:
		s = (p1.val) + carry
		carry = s//10
		val = s%10 
		prev = s_l	
		s_l.next = Node(val)
		s_l = s_l.next	
		p2 = p2.next 
	
	#prev.val += carry 
	return start.next 
	
def extract(h):
	l = []
	t = h
	while t:
		l.append(t.val)
		t = t.next
	return l

def test(l1, l2, correct):
	h1 = LinkedList()
	h2 = LinkedList()
		
	for e in l1:
		h1.add(e)
	h1.print()
	for e in l2:
		h2.add(e)
	h2.print()

	sum_ll = sum_list(h1.head, h2.head)
	new_ll = LinkedList()
	new_ll.head = sum_ll
	new_ll.print()
	v = extract(sum_ll)
	v.reverse()
	print(f"V : {v}")
	print(f"Correct : {correct}")
	#assert correct == val 

if __name__ == "__main__":
	l1 = [6,1,7]
	l2 = [2,9,5]

	l1.reverse()
	l2.reverse()
	
	test(l1,l2, 912)
	l1.append(1)

	test(l1,l2, 1912)
	l1 = [1,0,2]
	l2 = [9]
	test(l1,l2, 210)
	
	
