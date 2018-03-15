# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:55:03 2017

@author: Chris.Cirelli
"""

#   STOP WORDS - NATURAL LANGUAGE PROCESSING WITH PYTHON AND NLTK - PART 2

#   Vocabulary 
# Stop words - fluff words that can be pulled out of text.  Filler words. 

#   Step1: Import stop words

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = 'this is an example sentence of stop word functionality using nltk.'

stop_words = set(stopwords.words('english')) 

#print(stop_words) #You can append additional stop_words to this list. 

words = word_tokenize(example_sentence)

filtered_sentence = []
for x in words:
    if x not in stop_words:
        filtered_sentence.append(x)

print(stop_words)