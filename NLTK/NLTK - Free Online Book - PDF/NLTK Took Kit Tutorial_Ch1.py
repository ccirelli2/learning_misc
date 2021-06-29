# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 06:58:08 2017

@author: Chris.Cirelli
"""
#Look up www.Sendex.com 


#   Natural Language Processing:  NLTK Book

#Purpose is to have computers read and understand natural human written language. 

#   Terms

#Tokenizing - its a form of grouping things. You will have word tokenizers and sentence tokenizers. 
#Corporas -  Corpora is a body of text, ex medical journals. all around the same subject. Another example, body of law. 
#Lexicon - words and their names.  An example is investor speak.  Example is Bull = means something diff in investor speak versus normal english. 


#   Import nltk
import nltk
from nltk.book import*
import pandas as pd
import matplotlib.pyplot as plt

nltk.

#   SEARCH SAMPLE TEXT: 

#   Concordance - shows ever occurance of a given word together with some context. 
#   Concordance - lets you allow to understand the word in the context in which it was used

#text1.concordance("monstrous") #basically call the text, then concordance and then in paranthesis the word you want to find in the text. 
#text1.concordance('sea')

#   Find similar words used in a like context:
#text1.similar('monstrous') #odd results. 

#   Compare the meaning of words used in different texts using common_contexts
#text2.common_contexts(['monstrous', 'very'])

#   Graph the dispersion of words across a text (apparently you need to import numpy and matplotlib)
#text4.dispersion_plot(["citizens", "Democracy", "freedom", "duties", "America"])

#   Plot frequency of word useage through time using 
#http://books.google.com/ngrams



#   COUNT SAMPLE TEXT

#   Length of text
#print(len(text3))

#   Token:
# technical name for a sequence of characters - such as hairy, his, or - that we want to treat as a group. 

#   Show all of the tokens used in a particular text
#print(set(text3))

#   Organize all of the tockens used in a particular text
#print(sorted(set(text3)))

#   Count number of distinct "WORDS" in a given text 
#print(len(set(text3))) so while text3 has over 40k tokens, it only has 2789 words. 

#   Text lexical richness
#print(len(set(text3)) / len(text3))

#   Count specific number of words in a text
#print(text3.count('the'))


#   INDEXING LISTS 

#[Note:  It appears that any functions or methods applicable to lists will work in nltk for parsing data and words]


#   Call the xth word  
#print(text4[100]) #which apparently is the word the in text4. 

#   First occurance
#print(text4.index('day'))

#   Call range of words
#print(text5[100:200])


#   STRING METHODS

#   Mutliplication
#String1 = 'aachoo '
#print(String1*4)

#   Join two strings
#''.join(['shit', 'ass'])

#   Split
#('shit ass').split()


#   COMPUTING WITH LANGUAGE - STATISTICS

#   Frequency Distribution
#fdist1 = FreqDist(text1)
#print(fdist1.most_common(50))
#print(fdist1['whale'])

#   Cumulative Frequency Plot
#fdist1 = FreqDist(text1)
#fdist1.plot(50, cumulative = True) #will show the cumulative frequency, adding up each words frequency through the list.  Looking for change in curve
#fdist1.plot(50, cumulative = False) #will show actual frequency of each word#

#   Hapaxes (words that only occur once)
#print(len(fdist1.hapaxes()) / len(fdist1)) #46% of text is made of of words used only once.  

#   Find words of a particular lenght
#List1 = []
#for x in text1:
#    if len(x) > 15:
#        List1.append(x) 
#print(len(List1))

#   Find frequent but longer words
#fdist5 = FreqDist(text1)
#result = sorted(w for w in set(text5) if len (w) > 7 and fdist5[w] > 7)
#print(result)


#   COLLOCATIONS AND BIGRAMS

# Collocation is a sequence of words that occur together usually often. 
# Ex: red wine
# Use bigrams() function to identify collocations. 

#   Bigrams
#from nltk import bigrams
#List1 = list(bigrams(['more', 'is', 'said', 'than', 'done']))
#print(List1)

#   Collocation Function
# find biograms that occur 'more often than we would expect'
#print(text1.collocations())

#   Counting frequency of word length in text
#[len(w) for w in text1]
#fdist = FreqDist(len(w) for w in text1)
#print(fdist.most_common())

#   Frequency Distribution Functions

#fdist = FreqDist(sample): create a frequency distribution
#fdist[sample] +=1: increase distribution by 1
#fdist['monstrous']: count the number of times a given sample occured
#fdist.plot(): plot the frequency distribution
#fdistr.most_common(): the n most common samples and their frequencies
#for sample in fdist: iterate over sample
#fdist.max(): sample with the greaterst count
#fdist.tabulate(): tabulate the frequency distr
#fdist.plot(cumulative = True): cumulative plot of the freq dist


#   MAKING DECISIONS AND TAKING CONTROL

#   Conditionals
#[w for w in sent7 if len(w) < 4]

#   Word comparison functions:
# s.startswith(t): test if s starts with t
# s.endswith(t): test if s endds with t

#   Operating on Every Element
# [len(w) for w in text1]


#   AUTOMATIC NATURAL LANGUAGE UNDERSTANDING

#   Vador
#https://www.safaribooksonline.com/library/view/natural-language-text/9781491976487/video294968.html


























