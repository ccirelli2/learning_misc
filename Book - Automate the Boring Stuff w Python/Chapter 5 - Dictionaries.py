# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 07:32:56 2017

@author: Chris.Cirelli
"""

#   CHAPTER 5 - DICTIONARIES

"""
Note that his is very similar if, if not exact, to how NLTK provides the results for tokenization.  
It is a little different in that they are tokenizing words and sentennces into a dictionary.
In any case, this is a very useful tool. 
"""


string_1 = 'Today\'s a good day to code'

count = {}

for character in string_1:
    count.setdefault(character, 0)
    count[character] += 1

#print(count)


#   Chess Board

'''
Chess_board = { 'top-L':' ', 'top-M':'X', 'top-R':' ', 
               'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
               'low-L':' ', 'low-M':' ', 'low-R':' '}

def print_board(board):
    print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
    print('--+--+--')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])    
    print('--+--+--')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])
 

turn = 'X'

for i in range(9):
    print_board(Chess_board)
    print('turn for' + ' ' + turn + '. Move on which space?')
    move = input()
    Chess_board[move] = turn #so you are assigning a value to that key, so when you next print the board you will see this new value.  
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
print(Chess_board)

#   Note that this program does not tell you who one.  Nor does it prohibit the player from selecting the same space as did a prior player. 
'''

#   the below mimics the dictionary get method, but adds a twist where the dictionary will update if the key didnt exist. 
'''
example_dict = {'john': ['apples', 'oranges', 'shit'], 
                'mary': ['shit', 'bannanas', 'shit']}

def key_call_function(dictionary, key, string_1):
    if key in dictionary:
       print('key found')
    else:
        print(string_1)
        dictionary[key] = ''
        print('key added to dictionary')
        print(dictionary)

key_call_function(example_dict, 'steve', 'key not found')
'''













