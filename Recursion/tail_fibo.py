
def fibo(n, n_1=0, n_2=1):
        if n == 0:
                return n_1
        elif n == 1:
                return n_2

        return fibo(n-1, n_2, n_1+n_2 )


def fibonacciterative(n):
        if n == 0:
                return 0
        if n==1 or n==2:
                return 1
        f = 2
        p = 1
        for i in range(2,n):
             f,p = f+p, f 

        return p
          
f = [0,1,1,2,3,5,8,13]
for i in range(1,6):
        assert f[i] == fibonacciterative(i)
        assert f[i] == fibo(i)