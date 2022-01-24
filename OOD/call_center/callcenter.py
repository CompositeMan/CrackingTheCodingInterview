from enum import Enum
from typing import List

from collections import deque

class Rank(Enum):
	Respondent = 0
	Manager = 1
	Director = 2

class Call:
	def __init__(self, _t, _r:Rank, _e=None, *args, **kwargs):
		self.time = _t 
		self.min_rank = _r
		self.handled_by = _e
	def set_handled(self, _e):
		self.handled_by = _e

class Employee:
	def __init__(self, _id:int, _n:str, _add:str, _a:bool , _r:Rank):
		self.id = _id
		self.name = _n
		self.address = _add
		self.is_available = _a
		self.rank = _r

	def handle_call(self, c:Call):
		self.is_available = False
		# etc

class Respondent(Employee):
	def __init__(self, _id:int, _n:str, _add:str, _a:bool=True):
	        super().__init__(_id, _n, _add, _a, Rank.Respondent)

class Manager(Employee):
	def __init__(self, _id:int, _n:str, _add:str, _a:bool=True):
	        super().__init__(_id, _n, _add, _a, Rank.Manager)

class Director(Employee):
	def __init__(self, _id:int, _n:str, _add:str, _a:bool=True):
	        super().__init__(_id, _n, _add, _a, Rank.Director)

class CallCenter:
        hierarchy_levels = 3 
        def __init__(self, _e:List[List[Employee]], _c:List[Call]):
                self.employees = _e # separate lists of employees according to hierarchy as well
                self.employee_queues_by_hierarchy = [None]*self.hierarchy_levels
                self.form_queues()
                #calls queue
                self.call_queue = deque(_c)
        def form_queues(self):
                for i,l in enumerate(self.employees):
                        self.employee_queues_by_hierarchy[i] = deque(l)
                # print(f"Employee queues are formed :")
                # for d in self.employee_queues_by_hierarchy:
                #         print(d)

        def update_queues(self): #updates queues regularly 
                pass
        def add_employee(self, e:Employee):
                self.employees[e.rank].append(e)
                
        def find_apropriate_handler(self, r:Rank):
                e = None
                for i in range(r.value, self.hierarchy_levels):
                        q = self.employee_queues_by_hierarchy[i]
                        if len(q) != 0:
                                e = q.popleft()
                                break
                return e
		
        def dispatchCall(self, c:Call):
                e = self.find_apropriate_handler(c.min_rank)
                if not e:
                        # handle all busy scenario, for now add to queue
                        self.call_queue.append(c)
                else:
                        print(f"Type of e {type(e)}")
                        e.handle_call(c)
                        c.set_handled(e) 



