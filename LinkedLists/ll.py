class Node:
	def __init__(self, _v, _n=None):
		self.val = _v
		self.next = _n



class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, _v):
		if self.head == None:
			self.head = Node(_v)

		else:
			t = self.head

			while t.next != None:
				t = t.next
			
			t.next = Node(_v)

	
	def remove(self, _v):
		if self.head == None:
			return
		elif self.head.val == _v:
			self.head = self.head.next

		else:
			prev = self.head
			t = self.head.next

			while t.next != None:
				if t.val == _v:
					prev.next = t.next
					return
				t = t.next
				prev = prev.next

			if t.val == _v:
				prev.next = None
	
	def find(self, _v):
		if self.head == None:
			return None

		t = self.head

		while t.next != None:
			if t.val == _v:
				return t
			t = t.next
			
		return t if t.val == _v else None

	def print(self):
		if self.head == None:
			return

		t = self.head 
		while t.next != None:
			print(f"-> {t.val} ", end="")
			t = t.next
		
		print(f"->{t.val}")

def test():
	ll = LinkedList()
	for i in range(10):
		ll.add(i)

	ll.print()
	ll.remove(0)
	ll.remove(8)
	ll.remove(23)

	ll.print()	
	
	e = ll.find(3)
	print(f"3 is found {e != None} ")

	e = ll.find(8)
	print(f"8 is found {e != None}")
	e = ll.find(9)
	print(f"9 is found {e != None}")

if __name__ == "__main__":
	test()
