#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=55
# Brief     : For all n < 10000, count how many n don't create a palindrome when summing their own palindrome in 50 iterations. As in, 47 + 74 = 121.
# Comments  : Simple problem, python makes the code quite nice due to the string reversal [::-1].
#####

def check_lychrel(num):
    for iterations in range(50):
        result = num + int(str(num)[::-1])
        if is_palindrome(result):
            return True
        else:
            num = result
    return False
        
        
def is_palindrome(num):
    return str(num) == str(num)[::-1]
    
lychrel_counter = 0

for x in range(10000):
    if not check_lychrel(x):
        lychrel_counter += 1

print lychrel_counter