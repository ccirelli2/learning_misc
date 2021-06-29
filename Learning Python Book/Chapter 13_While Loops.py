# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:32:02 2017

@author: Chris.Cirelli
"""

####  Chapter 13 - While Loops

#==============================================================================
#While loop ex: 1
# 
# a= 0
# b = 10
# 
# while a < b: #The while loop will continue so long as a is less than b
#     print('a is less than b', end=', ') #the while loop will print shit and add a space at the end of the str
#     a = a+1 #a equals a + 1.  0+1, 1+1, 2+1, etc. 
#==============================================================================

#LEARN ABOUT BREAK, CONTINUE, PASS, AND LOOP ELSE STATEMENTS

#Loop Operators==============================================================================
# break= jump out of the closest enclosing loop (past the entire loop statement)
# continue = jumps to the top of the closest enclosing statement (to teh loop's header line)
# pass = Does nothing at all. Its an empty placement holder
# loop else block = Runs if and only if the loop is existed normally (i.e. without hitting a break)
#==============================================================================

#General Loop Structure=====================================================
# while test:
#     statements
#     if test: break
#     if test: continue
# else:
#     statements

#usually the break statement follows the if statement. 
#==============================================================================

#Continue Statements==============================================================


# x = 10
# while x: #simply pointing to x. below it will be defined. 
#     x = x-1 #defining x as 10-1, 9-1, etc. 
#     if x%2 !=0: rerun the loop statement and do not print. So if an odd number, repeat loop statement and do not print.  
#     print(x, end = ',' )
# 
# x1 = 9/2
# print(x1) repeat loop and do not print. 
#     
# x2 = 9/2
# print(x2) do not repeat loop and continue to print. 
#==============================================================================


#Break statement=============================================================
# 
# while True:
#     name = input('Enter name:  ') #define object name
#     if name == 'stop': break #if the name input == stop, break loop and do nothing. 
#     age = input('Enter age:  ') #if the name != stop, proceed to input age. 
#     print('Hello', name, '=>', int(age)**2) #once age is input, print this statement. 
#==============================================================================
    

#Loop else statement============================================================
# 
# x = y//2
# while x > 1:
#     if y%x == 0:
#         print(y, 'has factor', x)
#         break
#     x-= 1 #same as x = x-1
# else:
#     print(y, 'is prime')
# 
# Loop else is not clear at all. 
#==============================================================================
    
    
#for loops===================================================================
# 
##Format
# 
#
# for target in object:
#     statements
# else:
#     statements
#     
# for target in object:
#     statements
#     if test: break
#     if test: continue
# else:
#     statements
# 
# Examples:
# 
# 
# for x in ['spam', 'eggs', 'ham']: #essentially assigning each of these strings to x from left to right. 
#     print(x, end = ',') #telling the compiler to print each name followed by a ,
# 
# for x in [1,2,3,4,5]:
#     y = x+2 #only difference here is we are adding a calculation to each item in x[]
#     print(y, end = ',')
#     
#
#Other Data Types==============================================================
#
# 
# S = "Shit head"
# T= "Dick fuck"
# 
# for x in S: 
#     print(x, end = ',')
# for x in T: 
#     print(x, end = 'xxxx')
#==============================================================================




    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    