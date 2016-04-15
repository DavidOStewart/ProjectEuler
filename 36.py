#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=36
# Brief     : Find all numbers < 1000000 that are palindromes in both base 10 and base 2.
# Comments  : This is a trivial problem, I simply check if the string is the same moving forwards as it is backwards. The binary string starts at char 2 because it is represented as 0b10101010, and we need to remove the '0b' part.
#####

total = 0

for x in range(1000000):
    if str(bin(x))[2:] == str(bin(x))[:1:-1]:
        if str(x) == str(x)[::-1]:
            total+=x

print total