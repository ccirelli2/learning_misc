# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:34:29 2017

@author: Chris.Cirelli
"""

#   Natural Language Processing With Python and NLTK p.1 Tokenizing words and Sentences
#https://www.youtube.com/watch?v=FLZvOKSCkxY


#   Step 1: Import NLTK
import nltk

#   Step2: Vocabulary for NLTK

#tokenizing - form of organizing things.  You have word tokenizers and sentence tokenizers
#lexicon - like a dictionary.  The words and their meanings.  Can also thinkof types of meanings, like finance speak versus medical speak.  
#Corpora - group of texts

#   Step3: Basic Tokenizers

from nltk.tokenize import sent_tokenize, word_tokenize      #Imports both modules, sentene and word tokenizers. 

#example_text = 'Hello there, how are you?  I am good.'
#print(sent_tokenize(example_text)) #tokenize by sentence
#print(word_tokenize(example_text)) #note that it also seperates out punctuation. 

