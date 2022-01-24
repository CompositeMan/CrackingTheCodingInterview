SIZE = 100

class Heap:
	def __init__(self, size=SIZE):
		self.heap = [None]*size
	def level_order(self):


	def get_parent(self, i):
		return self.heap[ (i-1)//2 ]
	def get_left_child(self, i):
		return self.heap[ (2*i)+1 ]
	def get_right_child(self, i):
		return self.heap[ (2*i)+2 ]

 
