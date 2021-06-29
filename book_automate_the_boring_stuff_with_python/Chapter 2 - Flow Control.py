# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:48:20 2017

@author: Chris.Cirelli
"""

#   Chapter 2 - Flow Control

"""
print('Is it raining?\n')
response = input()
if response == 'yes':
    print('Do you have an umbrella?')
    response2 = input()
    if response2 == 'no':
        print('You should wait a while')
        
    else:
        print('Its ok to go outside')
else:
    print('Its ok to go outside')
"""



"""    print('Do you have an umbrella?\n')
    response1 == input()
    if response1 == 'yes':
        print('Ok, you can go outside')
    else:
        print('You should wait a while')
        print('Is it raining now?')
        reponse2 = input()
        while response == 'no':
            print('You should wait a while')
        else:
            print('Ok, you can go outside')
else:
    print()
"""

# Q&A

#response1 = ''
#while response1 != 'yes':
#    print('Is it raining outside?\n')
#    response1 = input()
#print('Thank you')

"""
Is it raining outside?
1. If no, then ok to go outside. 
2. if yes, 
    a. does the person have an umbrella?
        a1. if yes, ok to go outside
        ab. if no, tell to wait a while, 
        ac. as if it is raining outside, repeat loop. 
    b. if yes, ok to go outside. 
"""
question1 = 'Is it raining outside?'
question2 = 'Do you have an umbrella?'
response1 = 'Ok to go outside'
response2 = 'You should wait a while'

print(question1)
answer1 = input()
if answer1 == 'no':
    print(response1)
else:
    while True:
        print(question2)
        answerB = input()
        if answerB == 'yes':
            print(response2)
    else:
        print(response1)
      
    
                
            
            
            
            
    
    
        
        



