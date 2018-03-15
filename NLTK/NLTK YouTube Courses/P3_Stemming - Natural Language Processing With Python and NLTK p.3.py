# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:07:53 2017

@author: Chris.Cirelli
"""

#   STEMMING - NATURAL LANGUAGE PROCESSING WITH PYTHON - PART 3

#   Step1: Vocabulary:
#Stemming - take the root stem of the word.  Example: Riding, ridden, = Ride. The point is that you can have a lot of variations of a word, but the intended meaning is the same. 
#Stemming (purpose) - simplify database of words and how to approach large corporate more efficiently. 

#   Step2:  Import stemming processor 

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ['Python', 'Pythoner', 'Pythoning', 'Pythoned', 'Pythonly']

for w in example_words:
    print(ps.stem(w))
    
new_text = 'it is very import to be pythonly why you are pythoning with python.  All pythoners are have pythoned poorly at least once'

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
