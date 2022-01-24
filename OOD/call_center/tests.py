from callcenter import *
from random import choice, randint
from string import ascii_uppercase



R_NUM = 10
M_NUM = 4
D_NUM = 1
GLOBAL_ID = 0
NAME_LEN = 7

def generator():
        rs, ms, ds = [],[],[]
        global GLOBAL_ID
        for i in range(R_NUM):
                rs.append( Respondent(GLOBAL_ID, 
                                      "".join( choice(ascii_uppercase) for i in range(randint(0, NAME_LEN) ) ),
                                      "address",
                                        ))
                GLOBAL_ID += 1

        for i in range(M_NUM):
                ms.append( Manager(GLOBAL_ID, 
                                      "".join( choice(ascii_uppercase) for i in range(randint(0,NAME_LEN) ) ),
                                      "address",
                                        ))
                GLOBAL_ID += 1

        for i in range(D_NUM):
                ds.append( Director(GLOBAL_ID, 
                                      "".join( choice(ascii_uppercase) for i in range(randint(0,NAME_LEN) ) ),
                                      "address",
                                        ))
                GLOBAL_ID += 1
        return rs,ms,ds

def test():
        num_calls = 10
        rs,ms,ds = generator()
        es = [rs,ms,ds]
        from datetime import datetime
        cs = [ Call( datetime.now(), Rank(randint(0, len(Rank)-1) ) ) for i in range(10) ]
        center = CallCenter(es, cs)

        center.dispatchCall(cs[0])
        print(f"Call w/ {cs[0].min_rank} is handled by {cs[0].handled_by.name} w/ id {cs[0].handled_by.id}")

test()
