# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:05:18 2017

@author: Chris.Cirelli
"""

"""
#   REGULAR EXPRESSIONS - REGEX
 Apply to a string of text. 
 REGEX is its own language. 

#   Examples
 Parse data away from HTML data. 
 Find specific information, like dates, 

#   Identifiers
\d = any number
\D = anything but a number
\s = space
\S anything but a space
\w = any character
\W = anything but a character
. = whatever character you want to look for.  add character after period except for a new line
\b = the white space around words
\. = a period

#   Modifiers = looking for the amount of an identifier

[1,3] we're expecting 1-3 digits = \d(1-3)
+ = Means match 1 or more (it will only match if there are one ore more identifiers
? = Match 0 or 1
* = Match 0 or more
$ = Match the end of a string 
^ = Matching the beginning of a string
| = either or \d(1-3) | \d(4-5) looking for a number in length from 1-3 or 4-5
{} = range or variance
(X) = expecting X amount (number of instances)

#   White Space Characters
\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = return 

#   Example of Range
[A-Z] = range of A to Z case sensitive
[1-5a-qA-Z] looking for a nmber of 1-5 and a letter a-q and A-Q
"""

#   IMPORT REGULAR EXPRESSIONS

import re
#how to make a multiline string
exampleString = """ 
Jessica is 15 years old, and Daniel is 27 years old. 
Edward is 97, and his grandfather, Oscar, is 107. 
"""

#   Pull all names and ages. 
#ages = re.findall(r'\d{1,3}', exampleString) #pull from example string
#names = re.findall(r'[A-Z][a-z]*', exampleString) 
#print(ages)
#print(names)

# r tells python that this is a regular express.  
# Note no space between the two. the * tells python that we want to find 0 or more, or as many as possible. 

#   Second Example

expression_String2 = """
Milena will be 4 years ols in October, and Giuliana just turned 3. 
Chris will turn 35 in September. 
"""

#lettersCaps = re.findall(r'[A-Z]', expression_String2)
#print(lettersCaps)
#
#names = re.findall(r'[A-Z][a-z]*', expression_String2) #how does it know when it hits a white space to stop?
#print(names)
#
#months = re.findall(r'[A-Z][a-z][.,]', expression_String2) #how does it know when it hits a white space to stop?
#print(months)
#
#ages = re.findall(r'\d{1,3}', expression_String2)
#print(ages)









