#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=41
# Brief     : What is the largest N digit prime such that it contains digits 1 through N exactly once?
# Comments  : This problem seems simple at first; it's when I tried to generate a list of primes < 1 billion that I ran into memory and time issues.
#             First attempt was a naive brute force attempt where I assumed the largest two digits would be '98'. After struggling with that for a while,
#             I took some time off to look at it another way. Turns out there's a very simple rule that makes the problem much more manageable - if the sum
#             of the digits of a number are divisible by 3, the number itself is divisible by 3. Adding up digits 1-9 is divisible by 3, as is 1-8. The first
#             'large' pandigital prime, then, would be using 1-7 digits, much more manageable. It's with this set of numbers that I could generate the primes
#             and correctly solve it.
#####

import math,time
from bisect import bisect_left

    
def primes2(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = primes2(8000000)

for prime in primes[::-1]:
    digits = range(1,len(`prime`))
    for char in `prime`:
        if int(char) in digits:
            digits.remove(int(char))
    if digits == []:
        break
print prime
