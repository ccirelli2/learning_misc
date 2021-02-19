# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:08:41 2017

@author: Chris.Cirelli
"""

#   PYTHONG INTRODUCTORY TUTORIAL - WRITING BASIC FUNCTIONS

#   Example of a simple print function. 
"""
def example(): #start with def, then the name of the function, then parenthesis and a colon. 
    z = 3+9
    print(z)
 
example() #call the function by writing out its name.     
"""

#   Example of a function with parameters

"""
def simple_addition(num1, num2):       #note that the num1/2 are names. 
    answer = num1 + num2               #num1 will be whatever we assign to it. 
    print(answer)
    
num1 = 1
num2 = 10

simple_addition(num1, num2)            # no limit to the number of parameters that you can have in your function.  You just need to make sure that you understand the order. 
"""

#   ALtneratively you can pass the values directly to the function:
"""
def simple_addition(num1, num2):        #note that the num1/2 are names. 
    answer = num1 + num2                #num1 will be whatever we assign to it. 
    print(answer)
    
simple_addition(1, 10)                  #works the same
"""

#   Using Default values in your function
"""
def simple_addition(num1, num2 = 5):       #num2 has been given a default value. This means it will always be 5 when you run the function.  
    answer = num1 + num2               
    print(answer)

num1 = 10
simple_addition(num1, num2)
"""

