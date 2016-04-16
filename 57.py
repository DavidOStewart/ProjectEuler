#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=56
# Brief     : For a,b < 100, what is the maximal digital sum of a^b?
# Comments  : Again, easy program. Do note that int(math.pow(a,b)) != a**b as math.pow is using a float()
#####

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        total = sum([int(char) for char in str(a**b)])
        if total > max_sum:
            max_sum = total
print max_sum
