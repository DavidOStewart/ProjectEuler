#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=32
# Brief     : Find the sum of all products X * Y = Z such that the digits 1-9 are contained exactly once across X, Y, and Z.
# Comments  : As there are 9 digits involved, our search is somewhat limited and we can be smart about it. This problem was fairly
#             simple to solve using a semi-intelligent brute force algorithm. Not a whole lot to explain here, likely could be optimized 
#             but this result was quick and dirty enough to get done in 5 minutes.
#####

sums = set()

def check_product(x,y):
    digits = [1,2,3,4,5,6,7,8,9]
    result = x*y
    string = `x` + `y` + `result`
    if len(string) == 9:
        for char in string:
            if int(char) in digits:
                digits.remove(int(char))
        if len(digits) == 0:
            sums.add(result)

for x in range(1,1001):
    for y in range(999,10000):
        check_product(x,y)

for x in range(10,1001):
    for y in range(99,10000):
        check_product(x,y)
        
#check_product(39,186)
        
print sum(sums)