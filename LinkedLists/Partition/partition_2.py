#Write ode to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
#If x is contained within the list, the values of x only need to be after the elements less than x (see below). 
#The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
#EXAMPLE
#Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


#BCR : O(n) : I have to touch all the elements at least once 
"""

#Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] 
# Create another LL for smaller ones, then merge the two.

Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


"""
from sys import path
path.append("..")

from ll import LinkedList as LL
from ll import Node

def partite(head, part):
	if head == None or head.next == None:
		return head

	before_start = Node(0) # dummy 
	after_start = Node(0) # dummy 
	b_end = before_start
	a_end = after_start
	
	while head:
		if head.val < part:
			b_end.next = head
			b_end = b_end.next
			head = head.next
			b_end.next = None
		else:
			a_end.next = head
			a_end = a_end.next
			head = head.next
			a_end.next = None
	
	b_end.next = after_start.next

	return before_start.next

def test(r, k, ans):
	ll = LL()
	for i in r:
		ll.add(i)
	print(f"Partition: {k} , linkedlist:", end="")
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
	a = "Output: -> 3 -> 2 -> 1 -> 10 -> 5 -> 5 -> 8"
	test(i, p, a)
	i =  [3,5,8,9,10,2,1]
	p = 5
	a = "Output: -> 3 -> 2 -> 1 -> 10 -> 5 -> 8 -> 9"
	test(i, p, a)




