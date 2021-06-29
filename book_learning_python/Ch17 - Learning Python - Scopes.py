# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 08:48:22 2017

@author: Chris.Cirelli
"""

'''Names

- by default, all names inside a function are associated with that function's namespace and no other
- This means that names inside a def can only be seen by that def. 

Three Different Scopes:
- if a variable is assigned inside a def, it is local to that function. 
- if a variable is assigned in an enclosed def, it is nonlocal to nested functions. 
- if a variable is assigned outside all defs, it is global to the entire file. 

Global Scopes
- Span a single file only.  This is why objects associated with modules need to be imported before they can be referenced. 

Calling a function:
- each time you call a function you create a new local scope, that is, a namespace in which the names created inside that function will live. 



'''
    
#   Conjoining two functions
'''
def addfunction(a,b):
    c = a + b
    return c

a = 15
b = 10
c = addfunction(a,b)
'''

#   Creating a global object inside a function
'''
def addfunction(a,b):
    global c
    c = (a+b)
    return (c)
addfunction(1,2)

print(c)

#note that Steve says this is generally fround upon by programmers. 
'''

#   Example of Scope of Variables - Global vs Local
'''
L = [5]

def crapfunction(a,b):
    L = a+b
    print(L)

crapfunction(1,2)
'''

#   LEGB Rule

'''When you use an unqualified name inside a function, python searches up to four scopes
    1. local scope, 
    2. local scopes of any enclosing (E) defs and lambdas
    3. global scopes
    4. built in scopes
    LEGB
    *Python stops searching at the first instance of finding the variable. 
    
'''

#   Check Defined Terms in Doc
'''
import builtins
* Builins will give you access to all the builtin functions of Python. 


print(dir(builtins))

#Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

'''









































