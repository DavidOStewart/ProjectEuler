#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=53
# Brief     : How many values of n choose r, for 1 <= n <= 100 and r <= n, are > 1000000? (not necessarily distinct)
# Comments  : Formula for n choose r is (n!) / ((r!)(n-r)!). Very simple to run and verify, no comments needed.
#####

import math

list = []

for x in range(101):
    for y in range(x+1):
        result = float(math.factorial(x)) / (float(math.factorial(y) * math.factorial(x - y)))
        if result > 1000000:
            list.append(result)
            
print len(list)

