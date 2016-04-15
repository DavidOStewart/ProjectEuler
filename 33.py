#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=33
# Brief     : There exist exactly four fractions of the form XY / ZX, YX / ZX, or XY / XZ such that removing the X digit preserves the answer. Find them, then find the lowest common denominator if they are multiplied together.
# Comments  : This problem should be trivial to brute force. On inspection of the print statements at the bottom we find the resulting fraction to be 
#             387296 / 38729600, which is trivial in reduction and therefore I didn't feel the need to write a reduction function. Answer is, for the denominator, 100.
#####

xs = []
ys = []

for x in range(11,100):
    for y in range(11,100):
        #print x/y
        for char in `x`:
            if char in `y` and char != '0':
                new_x = `x`.replace(char,'')
                new_y = `y`.replace(char,'')
                if len(new_x) > 0 and len(new_y) > 0 and new_y != '0' and new_x != '0' and x/y < 1:
                    new_x = float(new_x)
                    new_y = float(new_y)
                    if new_x / new_y == float(x)/float(y):
                        xs.append(x)
                        ys.append(y)

nominator = 1
denominator = 1                        
    
for x in xs:
    nominator *= x
    
for y in ys:
    denominator *= y
    
print nominator, denominator