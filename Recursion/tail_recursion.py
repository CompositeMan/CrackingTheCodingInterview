from typing import List

def dump_list(l:List, add=""):
	s = []
	for i,elm in enumerate(l):
		if isinstance(elm, List):
			s.extend( dump_list(elm, add+str(i)+".") )
		else:
			s.append( "Dumplist: " + add + str(i) + ". " + elm + "\n")
	
	return s
def test(s=['a string', ['a','b','c'], 'spam', ['eggs'], [[["DEEP"]]] ]):
	p = dump_list(s)
	p = "".join(p)
	print(p)

test()