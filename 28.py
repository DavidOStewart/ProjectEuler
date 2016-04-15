import math
previous = 1
iterator = 0
total = 0
for x in range(9):
    iterator=iterator + 2 if x % 4 == 0 else iterator
    total += previous
    previous += iterator
    
print total
