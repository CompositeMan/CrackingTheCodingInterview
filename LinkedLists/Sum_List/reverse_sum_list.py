from sys import path

path.append("..")
from ll import LinkedList
from ll import Node 
def sum_list(h1, h2)->int:
	if not h1:
		return h2
	elif not h2:
		return h1
	
	p1 = h1
	p2 = h2
	stack1 = []
	stack2 = []
	
	while p1:
		stack1.append(p1.val) 
		p1 = p1.next
	while p2:
		stack2.append(p2.val) 
		p2 = p2.next 

	s_l = None 
	carry = 0
	
	while len(stack1) > 0 and len(stack2) > 0:
		v1 = stack1.pop( len(stack1) - 1 )
		v2 = stack2.pop( len(stack2) - 1 )
		s = v1+v2+carry
		
		carry = s//10
		val = s%10
		n = Node(val, s_l)
		s_l = n

	residues = stack1 if len(stack1) > 0 else stack2
	while len(residues)>0:
		v = residues.pop( len(residues) - 1 )
		s = v+carry
		carry = 0
		val = s%10
		
		n = Node(val, s_l)
		s_l = n
	
	return s_l 
	
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
	print(f"V : {v}")
	print(f"Correct : {correct}")
	#assert correct == val 

if __name__ == "__main__":
	l1 = [6,1,7]
	l2 = [2,9,5]

	test(l1,l2, 912)
	l1.insert(0,1)

	test(l1,l2, 1912)
	
	
