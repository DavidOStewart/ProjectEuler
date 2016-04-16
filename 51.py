#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=51
# Brief     : By replacing part of a prime number with the same digit (56003 -> 56113 -> 56333...) more primes are made. Find the smallest prime that begins an 8-part chain of primes.
# Comments  : Code isn't exactly clear, but basically I did a couple tests. First I tried all 5 digit primes, replacing all permutations of 2 digits looking for 8 primes in total. When that didn't work, I tried all permutations of 3 digits in all 5 digit primes. Moving forwards I tried the same iterations with 6 digit primes and eventually found my answer.
#####
import time, itertools
from bisect import bisect_left

p = set()
for list in itertools.permutations([1,1,1,0,0,0], 6):
    p.add(list)
    
p = sorted(p)
    
def primes2(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
    
def binary_search(a, x, lo=0, hi=None):   
    hi = hi if hi is not None else len(a)    
    pos = bisect_left(a,x,lo,hi)          
    return (pos if pos != hi and a[pos] == x else -1)
       

primes = primes2(1000000)

def counting_chamber(num):

    digits = [9,8,7,6,5,4,3,2,1,0]
    for list in p:
        list_of_primes = [num]
        prime_count = 1
        num2 = str(num)
        for digit in digits:
            for x in range(len(num2)):
                if list[x] == 1:
                    num2 = num2[:x] + `digit` + num2[x+1:]
            if binary_search(primes, int(num2)) != -1:
                if num2[0] != '0':
                    if int(num2) != num:
                        prime_count+=1
                        list_of_primes.append(num2)
        if prime_count == 9:
            print num2
        
for prime in primes:
    if len(str(prime))==6:
        counting_chamber(prime)

