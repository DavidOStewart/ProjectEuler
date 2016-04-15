#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=29
# Brief     : How many unique numbers are there for, where 2 <= x,y <= 100, x^y?
# Comments  : This one was a fun one. I thought of a couple different ways to approach it. 
#             First approach used a dictionary, simply adding a new key for each new number.
#             After iterating through each number, I simply counted up the unique keys and got my answer.
#             Average time for the dictionary: ~.042 seconds.
#
#             Next approach was to use a list which I append each number to, then calling len(set(list))
#             Calling set() first removed any duplicates which allowed len to count the unique elements.
#             Average time for the list      : ~.042 seconds
#             
#             Last approach used a set() instead of a list, which natively removes duplicates.
#             Average time for set           : ~.042 seconds
#
#             I found no discernable difference between the three approaches. Only way I could potentially see speeding this up is through multiple threads, which I will visit at a later date.
#####

import math, time

#dictionary approach
def dict_trial():
    dict = {}
    for x in range(2,101):
        for y in range(2,101):
            dict[math.pow(x,y)] = '.'
    unique = len(dict)

#list approach
def list_trial():
    list = []
    for x in range(2,101):
        for y in range(2,101):
            #num = math.pow(x,y)
            list.append(math.pow(x,y))
    unique = len(set(list))

#set approach
def set_trial():
    list2 = set()

    for x in range(2,101):
        for y in range(2,101):
            list2.add(math.pow(x,y))
        
    unique = len(list2)

start = time.clock()
dict_trial()    
print time.clock() - start
time.sleep(.5)
start = time.clock()
list_trial()
print time.clock() - start
time.sleep(.5)
start = time.clock()
set_trial()
print time.clock() - start
