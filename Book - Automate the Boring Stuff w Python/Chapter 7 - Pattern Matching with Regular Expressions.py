# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 19:00:51 2017

@author: Chris.Cirelli
"""

#   PATTER MTCHING WITH REGULAR EXPRESSIONS

import re

string_1 = 'My phone number is 404-201-0861.  My mom\'s phone number is 608-709-3696.'
'''
for i in range(len(string_1)):
    chunk = string_1[i:i+12]
    if re.search('\d{3}-\d{3}-\d{4}', chunk):
        print('match found')

if re.search('\d{3}-\d{3}-\d{4}',string_1):
    print('match found')

phoneNumRex = re.compile(r'\d{3}-\d{3}-\d{4}') 
#note that you need to create a regex object to use the library.  That's why this step is important

#print(re.findall(phoneNumRex,string_1)) #use of findall function
mo = phoneNumRex.search('404-201-0861')

print(re.findall(phoneNumRex, string_1))
print('Phone number' + str(mo) + 'match found') 
print(mo.group())   #will return the value of the match
'''

#   Grouping With Parenthesis
