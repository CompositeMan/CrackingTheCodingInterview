#Write ode to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
#If x is contained within the list, the values of x only need to be after the elements less than x (see below). 
#The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
#EXAMPLE
#Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


#BCR : O(n) : I have to touch all the elements at least once 
"""

#Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] 

stop = *1
if smaller:
	append at head

if bigger:
	append at tail 

I need to remember the first tail I appended to, this way I can know where to stop

Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


"""
from sys import path
path.append("..")
from ll import LinkedList as LL
def partite(head, part):
	if head == None or head.next == None:
		return head

	t = None
	tail = get_tail(head)
	stop = tail
	while head.val >= part:
		t = head
		head = head.next
		tail = append(tail, t)
	prev = head
	t = head.next
	ex = False
	while not ex:
		if t == stop:
			ex = True
		if t.val >= part:
			node = pop_next(prev)
			tail  = append(tail, node)
			t = prev.next
		
		else:
			t = t.next
			prev = prev.next
	return head

def get_tail(head):
	t = head
	while t.next != None:
		t = t.next

	return t

def append(tail, node):
	node.next = None
	tail.next = node
	return tail.next

def pop_next(cur):
	# assuming cur.next is not None 
	
	e = cur.next 
	if cur.next.next == None:
		cur.next = None

	else:
		cur.next = cur.next.next	
	return e

def test(r, k, ans):
	ll = LL()
	for i in r:
		ll.add(i)

	print(f"Partition: {k} , linkedlist: ", end="")
	ll.print()
	ll.head = partite(ll.head, k)
	ll.print()
	print(ans)

if __name__ == "__main__":
	i = [ 14-i for i in range(15) ]
	o = "Output: -> 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> 14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 ->6"
	test(i, 6, o)
	i =  [3,5,8,5,10,2,1]
	p = 5
	a = "Output: -> 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8"
	test(i, p, a)
	i =  [3,5,8,9,10,2,1]
	p = 5
	a = "Output: -> 3 -> 1 -> 2 -> 10 -> 5 -> 8 -> 9"
	test(i, p, a)




