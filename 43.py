#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=43
# Brief     : Find the sum of all pandigital numbers (containing 0-9 exactly once, no leading zeroes) whose 2nd-4th digit substring is divisible by 2, 3rd-5th by 3, 4th-6th by 5, 5th-7th by 7, 6th-8th by 11, 7th-9th by 13, and 8th-10th by 17. Example is 1406357289, 406 % 2 == 0; 063 % 3 == 0...etc.
# Comments  : With the discovery of itertools.permutations, this problem got markedly easier. All that was necessary is a cute little check_subs() function to 
#           : verify the substrings function as necessary.
#####
import time, random, itertools

primes = [2,3,5,7,11,13,17]

def check_subs(num):
    num = str(num)
    counter = 1
    for prime in primes:
        if int(num[counter:counter+3]) % prime != 0:
            return False
        counter+=1
    return True

digits = [9,8,7,6,5,4,3,2,1,0]    

list = itertools.permutations(digits, 10)
total = 0
    
for num in list:
    num = ''.join(map(str,num))
    if num[0] == '0':
        continue
    num = int(num)
    if check_subs(num) == True:
        total+= num
print total

