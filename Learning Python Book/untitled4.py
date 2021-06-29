# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:16:03 2017

@author: Chris.Cirelli
"""

def mysum(L):
   if not L:
       return 0
   else:
       return L[0] + mysum(L[1:])

mysum([1,2,3,4,5])

