#Given two strings,write a method to decide if one is a permutation of the other.

def if_perm(s, b):
	l_s, l_b = len(s), len(b)
	if l_s == 0 or l_b == 0:
		return False
	opts = dict()
	long, short = (s,b) if l_s > l_b else (b,s)
	taken = []

	for s in short:
		add(opts,s)
	for l in long:
		while not l in opts.keys() and len(taken) > 0:
			add(opts, taken.pop(0))	

		if not l in opts.keys():
			continue
		else:
			pop(opts, l)
			taken.append(l)

		if len(taken) == len(short) and len(opts.keys()) == 0:
			return  True

	return False
	 	

def add(d, ch):
	if ch in d.keys():
		d[ch] += 1
		return
	d[ch] = 1


def pop(d, ch):
	if ch in d.keys():
		d[ch] -= 1
		if d[ch] == 0:
			d.pop(ch)
		
		
def test(s = "morning", b = "good morning", ans = True):
	assert if_perm(s,b) == ans

if __name__ == "__main__":
	test()
	test("morn", "norm", True)
	test("norm", "moumormno", True)
	test("norm", "nope", False)
