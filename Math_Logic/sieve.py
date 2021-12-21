from math import sqrt

def sieve(mx:int):
	s = (mx+1)//2
	primes = [True] * s
	prime = 3
	sqrt_max = sqrt(mx) 
	while prime <= sqrt_max and prime < s:
		cross_off(primes, prime)
		prime = get_next_prime(primes, prime)

	return primes

2
#[ True, True, True, True, True ]
#1,3,5,7,9



# Cross off remaining multiples of prime. We can start with (prime*prime),
# because if we have a k * prime, where k < prime, this value would have
# already been crossed off in a prior iteration. 
def cross_off(pr, p):
	i = p*p
	l = len(pr)
	while i < l:
		if p % 2 == 1:
			pr[ get_index(p) ] = False
		i += p


def get_next_prime(pr, p):
	l = len(pr)
	p += 2 
	while not pr[get_index(p)] and p<l:
		p += 2

	return p

def get_prime(i):
	return (i*2)+1


def get_index(i):
	return int((i-1)/2)

def test():
	primes = sieve(100)
	print(primes)	
	l = len(primes)
	for i in range(1, l):
		if primes[i]:
			print( get_prime(i), end=" ")

	print()


test()

