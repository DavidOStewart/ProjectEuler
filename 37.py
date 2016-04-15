#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=37
# Brief     : There are 11 primes such that the number remains prime when removing numbers left to right as well as right to left. Find their sum.
# Comments  : This problem was fairly easy. To start, I generate a list of primes smaller than one million. Then I iterate through the list of primes
#             and check for left to right / right to left primality using a binary search function to look through the list of primes. The prime generation
#             has been optimized as much as possible, generating the primes < 100000 in ~.06 seconds.
#####

import math,time
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   
    hi = hi if hi is not None else len(a)    
    pos = bisect_left(a,x,lo,hi)          
    return (pos if pos != hi and a[pos] == x else -1)
    
def primes2(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

    
both_ways = True
start = time.clock()
primes = primes2(1000000)
print time.clock() - start
total = 0
for prime in primes:
    if prime < 10:
        continue
    for x in range(1,len(`prime`)):
        if binary_search(primes, int(str(prime)[x:])) == -1 or binary_search(primes, int(str(prime)[:x])) == -1:
            both_ways = False
            break
    if both_ways == True:
        total += prime
    both_ways = True
print total
