#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=42
# Brief     : Triangle numbers are defined as t-sub-n = .5n(n+1). The first 10 triangle numbers are 1,3,6,10,15,21,28,36,45,55
#             Given a list of 2000 english words (supplied at the problem link), sum them by the alphabetical position of each letter (A = 1, B = 2, etc)  
#             How many of the sums are triangle numbers?
# Comments  : Problem is extremely straightforward, little to no comments on the problem.
#####
    
from bisect import bisect_left
    
tri_nums = []
    
def triangles(n):
    for x in range(1,n+1):
        tri_nums.append(int(.5*x*(x+1)))
        
def binary_search(a, x, lo=0, hi=None):   
    hi = hi if hi is not None else len(a)    
    pos = bisect_left(a,x,lo,hi)          
    return (pos if pos != hi and a[pos] == x else -1)
        
triangles(100)
print tri_nums
    
f = open("42words.txt")
words = f.read()
word_list = words.replace('"', '').split(',')
word_count = 0

for word in word_list:
    counter = 0
    for char in word:
        counter+= ord(char) - 64
    if binary_search(tri_nums, counter) != -1:
        word_count+=1

print word_count