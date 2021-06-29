# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:46:12 2017

@author: Chris.Cirelli
"""

##Random Numbers

# Step1: import numpy and the randoms package.  Inside the randoms package we find the ran function

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# for x in range(10):
#     for y in range(10):
#         x = np.random.rand()
#         y = np.random.rand()
#     z= (x,y)
#     #print(z)
#     #print(x)
#     #print(y)
#     #plt.scatter(x,y) 
#==============================================================================
    
#==============================================================================
# # Not very clear, but you can change the base value that Python uses to generate the randome numbers so that each 
# #iteration of the random generation generates the same number.  Apparently you use this for algorythms. 
# 
# np.random.seed(123)
# s = np.random.rand()
# 
# print(s)
#==============================================================================


#==============================================================================
# ##Simulate a coin toss
# 
# 
# #to have the generate generate a number of 1 or 2, we use two arguments, (0,2).  Assuming this is like the range of an index where 0 up to but not including 2. 
# 
# np.random.seed(123)
# for coin in range(10):
#     coin = np.random.randint(0,2)
#     if coin == 1:
#         print('heads')
#     else:
#         print('tails')
# 
# for x in range(10):
#     x = x +1
#     print(x)
#     
#     
# for x in range(10):
#     print(x,"shit")
#==============================================================================
    
#==============================================================================
# ##Random walk building a list. 
# 
# import numpy as np
#  
# np.random.seed(123)
# outcomes = []
# 
# for x in range (10): #nothing changes when you replace x with coin.  I guess Python knows the next define variable is x. 
#     coin = np.random.randint(0,2) #0 or 1. 
#     if coin == 0:
#         outcomes.append('heads')
#     else:
#         outcomes.append('tails')
#     print(outcomes)
#==============================================================================

# ##Random walk building a list. 

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

#==============================================================================
# Y = [1]
# 
# for y in range(20):
#     Y.append(y +1)
#     print(Y)
#==============================================================================


tails = [0] #list tails

final_tails = []

for x in range(1000):
    tails = [0]    
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin) #if we append coin, wont that give us both heads and tails as opposed to just tails?
    final_tails.append(tails[-1])
plt.hist(final_tails, bins = 10)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    