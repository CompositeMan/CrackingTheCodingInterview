

class PermIn:
    def __init__(self, small, big):
        self.small = small
        self.big = big
        self.d = self.prepare()

    def prepare(self):
        # time : O( len(small) ), space: O( 2*(len(small))  )
        d = dict()
        for ch in self.small:
            add(d, ch)

        return d

    def small_perm_in(self):
        opts = self.d.copy() # O( len(d.keys()) ) -> O(len(small)) worst case
        took = []

        perms = []
        perm_count = 0

        for i in range(len(self.big)):
            b = self.big[i]

            if b not in self.d.keys(): # a foreign character
                if len(opts.keys()) != len(self.d.keys()):
                    opts = self.d.copy()
                took.clear()
                continue

            while b not in opts:
                add(opts, took.pop(0))

            pop(opts, b)
            took.append( b )

            if len(took) == 4 and len(opts.keys()) == 0:
                perms.append( "".join(took))
                perm_count += 1

        return perm_count, perms

def add(d, e):
    try:
        d[e] += 1
    except:
        d[e] = 1

def pop(d, e):
    d[e] -= 1
    if d[e] == 0:
        d.pop(e)
    return e

def test(s, b):
    #b = "cbbabbcb"
    pin = PermIn(s, b)
    r, ps = pin.small_perm_in()
    print(f"s:{s}, b:{b}")
    print(f"perms: {ps}\n size:{r}")
    cor_res = 7
    #print(r==cor_res)

if __name__ == '__main__':
    s = "abbc"
    b = "cbabadcbbabbcbabaabccbabc"
    test(s,b)
    b = "abbbbcbabaabccbabc"
    test(s,b)
    b = "dabbbbcbabaabccbabc"
    test(s,b)
