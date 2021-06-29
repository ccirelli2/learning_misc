# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 16:10:49 2017

@author: Chris.Cirelli
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
import matplotlib.pyplot as plt

#   P1 NATURAL LANGUAGE PROCESSING WITH NLTK


#   Import NLTK Book Corpus
#from nltk.book import*

#   Call NLTK Books
#print(text1)

#   Convert list to nltk.text data type
#nltk.Test(list)

#   Concordance function - usage of a word + context
#print(text1.concordance('monstrous'))

#   Call similar words
#print(text1.similar('monstrous'))

#   Common Context One or more words
#print(text2.common_contexts(['monstrous']))
#print(text2.common_contexts(['monstrous', 'size']))

#   Plot Word USage Dispersion
#print(text1.dispersion_plot(['whale', 'ocean', 'sea', 'white', 'Moby', 'Dick']))
#**Note that the dispersion_plot only workds on certain data types.  Apparently this call format will not work with lists. need to find 
#an alternative way. 

#   Call Frequency Distribution to list the frequency of each token
#File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA.txt')
#raw = File.read()
#token = word_tokenize(raw)
#freqdist = nltk.FreqDist(token)
#print(freqdist.most_common(50))

#   Call word in context
#File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA.txt') #data type is a io.TextIOWrapper'
#raw = File.read() #convert data type to str 
#raw_tokenized = word_tokenize(str(raw))
#raw_nltk = nltk.Text(raw_tokenized)
#raw_nltk.concordance('cause')

#   Count Text - Unique words 'set'
#print(len(text1))
#print(len(set(text1))) #number of unique tokens in text
#print(len(sorted(set(text1)))) #will order the list starting with punctuation and then tokens starting with 'a'

#   Lexical richness of text
#Lex_rich = (len(set(text1))) / (len(text1))
#print(Lex_rich*100)

#   Count word appearance as % text (improvised to use list of words)
#List = ['Dick', 'Moby', 'Ahab', 'Sea', 'Ocean', 'Whale']
#for x in List:
#    print(x, (text1.count(x)/ len(set(text1)))*100, '%') #word count as % of total unique words for text

#   Seperate document into Sentences
#File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA.txt') #data type is a io.TextIOWrapper'
#raw = File.read() #convert data type to str 
#token_sent = sent_tokenize(raw)
#Df = pd.DataFrame(token_sent[:1000])
#print(Df)

#   Indexing words and areas of the document
#File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA.txt') #data type is a io.TextIOWrapper'
#raw = File.read() #convert data type to str 
#token_sent = word_tokenize(raw)
#print(token_sent.count('competition'))
#print(token_sent.index('competition'))
#print(token_sent[6300:6500])


#   Search for most frequent words and then look at the context in which they were used
#File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA.txt') #data type is a io.TextIOWrapper'
#raw = File.read()
#token_raw = word_tokenize(raw)
#token_nltk = nltk.Text(token_raw)
#token_freqdist = nltk.FreqDist(token_nltk)
#print(token_freqdist.most_common(100))
#print(token_nltk.common_contexts(['material']))
#print(type(token_nltk.concordance('material')))

#   Plot Frequency Distribution
#text1_freqdist = nltk.FreqDist(text1)
#text1_freqdist.plot(50, cumulative = True)

#   Long words
#Example1
#v = set(text1)
#long_words = []
#for words in v:
#    if len(words) > 15:
#        long_words.append(words)
#print(long_words)

#Example2
#File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA.txt') #data type is a io.TextIOWrapper'
#raw = File.read() #convert data type to str 
#raw_tokenize = word_tokenize(raw)
#long_words2 = []
#for word in raw_tokenize:
#    if len(word) > 15:
#        long_words2.append(word)
#print(long_words2)
        







