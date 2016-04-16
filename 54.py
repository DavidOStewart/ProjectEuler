#####
# Author    : David Stewart
# Date      : April 14, 2016
# Problem   : https://projecteuler.net/problem=54
# Brief     : Given 1000 poker hands, how many does player 1 win?
# Comments  : This problem is more tedious than difficult. Parsing input and determining hand strength is annoying but not necessarily tricky.
#####

import time

f = open("poker.txt")
line = f.readline()

for line in f:
    
    player1 = []
    player2 = []
    counter = 0

    for x in line.split():
        if counter < 5:
            player1.append(x)
        else:
            player2.append(x)
        counter+=1

    print sorted(player1), sorted(player2)
    time.sleep(30)
        
