#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=38
# Brief     : For what P are there the most right triangles with perimeter P <= 1000?
# Comments  : Problem is very simple to brute force, just precompute the squares of the legs and then iterate through to see which combinations give
#             the most right triangles.
#####

import math, time
from bisect import bisect_left

squares = []
triangles = [0]*1000

def binary_search(a, x, lo=0, hi=None):   
    hi = hi if hi is not None else len(a)    
    pos = bisect_left(a,x,lo,hi)          
    return (pos if pos != hi and a[pos] == x else -1)

for x in range(1,1001):
    squares.append(x*x)
start = time.clock()
for leg1 in squares:
    for leg2 in squares[squares.index(leg1):]:
        perimeter = int(math.sqrt(leg1) + math.sqrt(leg2) + math.sqrt(leg1+leg2))
        if perimeter < 1000:
            pos = binary_search(squares, leg1+leg2)
            if pos != -1:
                triangles[perimeter] += 1
print time.clock() - start
print triangles.index(max(triangles))